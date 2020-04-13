#!/bin/sh

export USER_DIR=${USER_DIR:="/usbdrive"}
# PATCH_DIR=${PATCH_DIR:="/usbdrive/Patches"}
# FW_DIR=${FW_DIR:="/root"}
# SCRIPTS_DIR=$FW_DIR/scripts

# should be run from motherhost package installer

mkdir -p $USER_DIR/media/orac/captures
mkdir -p $USER_DIR/media/orac/usermodules/sampler

cp -r $USER_DIR/Patches/capture $USER_DIR/media/orac/usermodules/sampler
rm -r $USER_DIR/Patches/capture

exit 0
