#!/bin/bash
# SPDX-License-Identifier: BSD-3-Clause
#
# Copyright (c) Qualcomm Technologies, Inc. and/or its subsidiaries.
#
# Build the Debian packages for the checked out source tree using the
# packaging from the pkg-audioreach-conf repository, so that packaging
# breakage is caught before a release is imported there.
#
# Usage: ci/debian_build.sh <source-dir> <out-dir>
# Env:   PKG_REPO (default qualcomm-linux/pkg-audioreach-conf)
#        PKG_REF  (default qli/debian/latest)
#        PKG_DIR  local packaging checkout, overrides PKG_REPO/PKG_REF

set -euo pipefail

SRC=$(readlink -f "${1:?source dir}")
OUT=$(readlink -m "${2:?output dir}")
PKG_REPO=${PKG_REPO:-qualcomm-linux/pkg-audioreach-conf}
PKG_REF=${PKG_REF:-qli/debian/latest}

export DEBIAN_FRONTEND=noninteractive
apt-get update -qq
apt-get install -y -qq --no-install-recommends \
    build-essential debhelper dh-autoreconf autoconf automake libtool \
    pkgconf git ca-certificates lintian fakeroot devscripts

WORK=$(mktemp -d)
mkdir -p "$OUT"

# Fetch the packaging.
if [ -n "${PKG_DIR:-}" ]; then
    cp -r "$PKG_DIR" "$WORK/pkg"
else
    git clone -q --depth 1 -b "$PKG_REF" "https://github.com/${PKG_REPO}.git" "$WORK/pkg"
fi

# Version comes from the source tree being validated.
VER=$(sed -n 's/^AC_INIT(\[audioreach-conf\],\s*\([0-9.]*\)).*/\1/p' "$SRC/configure.ac")
[ -n "$VER" ] || { echo "cannot read version from configure.ac"; exit 1; }
echo "Validating audioreach-conf $VER with packaging from $PKG_REPO@$PKG_REF"

# Upstream tarball from the tree under test (no CI/packaging leftovers).
TREE="$WORK/audioreach-conf-$VER"
mkdir -p "$TREE"
git -C "$SRC" archive HEAD | tar -x -C "$TREE"
rm -rf "$TREE/debian" "$TREE/.github"
tar -C "$WORK" -czf "$WORK/audioreach-conf_$VER.orig.tar.gz" "audioreach-conf-$VER"

# Add debian/ and align the changelog version with the source version.
cp -r "$WORK/pkg/debian" "$TREE/debian"
sed -i "1s/^audioreach-conf ([^)]*)/audioreach-conf ($VER-0qli1~)/" "$TREE/debian/changelog"

cd "$TREE"
dpkg-buildpackage -us -uc -b 2>&1 | tee "$OUT/build.log"

cd "$WORK"
cp ./*.deb ./*.buildinfo ./*.changes "$OUT/"

echo "=== Package contents ==="
for d in "$OUT"/*.deb; do
    echo "--- $(basename "$d")"
    dpkg -c "$d" | awk '{print $1, $6}'
done

echo "=== lintian ==="
lintian --no-tag-display-limit --display-info "$OUT"/*.changes | tee "$OUT/lintian.log" || true
# Only errors fail the job; warnings are informational.
! grep -q '^E:' "$OUT/lintian.log"

# CI test: trigger the Debian build validation
