#!/bin/bash

set -e
set -x
artiq_compile -o idle.elf repository/idle.py
artiq_compile -o startup.elf repository/startup.py

if true; then
  artiq_mkfs storage.img \
    -s mac 54:10:ec:aa:09:72 \
    -s ip 10.0.16.118 \
    -s startup_clock e \
    -f startup_kernel startup.elf \
    # -f idle_kernel idle.elf
  artiq_flash -t kasli -V opticlock -f storage.img storage start
else
  artiq_coreconfig erase
  artiq_coreconfig write \
    -s mac 54:10:ec:aa:09:72 \
    -s ip 10.0.16.118 \
    -s startup_clock e \
    -f startup_kernel startup.elf \
    # -f idle_kernel idle.elf
fi
