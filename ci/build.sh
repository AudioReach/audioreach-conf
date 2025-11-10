#!/bin/bash
# SPDX-License-Identifier: BSD-3-Clause-Clear
#
# Copyright (c) 2025 Qualcomm Innovation Center, Inc. All rights reserved.
set -ex
echo "Running build script..."

# Build/Compile audioreach-conf
# make sure we are in the right directory
cd ${GITHUB_WORKSPACE}
source ${GITHUB_WORKSPACE}/install/environment-setup-armv8-2a-poky-linux
mkdir ${GITHUB_WORKSPACE}/build
mkdir ${GITHUB_WORKSPACE}/build/etc
mkdir ${GITHUB_WORKSPACE}/build/etc/acdbdata
mkdir ${GITHUB_WORKSPACE}/build/etc/acdbdata/qcm6490_rb3
mkdir ${GITHUB_WORKSPACE}/build/etc/acdbdata/qcs8300
mkdir ${GITHUB_WORKSPACE}/build/etc/acdbdata/qcs9075
mkdir ${GITHUB_WORKSPACE}/build/etc/acdbdata/qcs9100

cp -r qcom/qcm6490/card-defs.xml ${GITHUB_WORKSPACE}/build/etc/
cp -r qcom/qcm6490/acdbdata/* ${GITHUB_WORKSPACE}/build/etc/acdbdata/qcm6490_rb3/
cp -r qcom/qcs8300/acdbdata/* ${GITHUB_WORKSPACE}/build/etc/acdbdata/qcs8300/
cp -r qcom/qcs9100/acdbdata/* ${GITHUB_WORKSPACE}/build/etc/acdbdata/qcs9100/
cp -r qcom/qcs9075/acdbdata/* ${GITHUB_WORKSPACE}/build/etc/acdbdata/qcs9075/

# sample test
# second commit
