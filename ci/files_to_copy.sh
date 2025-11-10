#!/bin/bash
# SPDX-License-Identifier: BSD-3-Clause-Clear
#
# Copyright (c) 2025 Qualcomm Innovation Center, Inc. All rights reserved.

# Move outside the github workspace to avoid conflicts
cd ..

# copy the build artifacts to a temporary directory
cp -R build/etc/* /tmp/rootfs/etc/
cp -R build/etc/acdbdata/qcm6490_rb3/* /tmp/rootfs/etc/acdbdata/qcm6490_rb3/
cp -R build/etc/acdbdata/qcs8300/* /tmp/rootfs/etc/acdbdata/qcs8300/
cp -R build/etc/acdbdata/qcs9100/*  /tmp/rootfs/etc/acdbdata/qcs9100/
cp -R build/etc/acdbdata/qcs9075/*  /tmp/rootfs/etc/acdbdata/qcs9075/


