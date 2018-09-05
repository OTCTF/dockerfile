#!/bin/bash

THIS_DIR="$(cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd)"

# zsteg, one_gadget, seccomp-tools requires Ruby version >= 2.1.0.
$THIS_DIR/../src/main.py --template Dockerfile.j2 --name all-14.04 --params os=14.04 ignore_zsteg=1 ignore_one_gadget=1 ignore_seccomp_tools=1

# php5 is only supported on ubuntu-14.04
$THIS_DIR/../src/main.py --template Dockerfile.j2 --name all-16.04 --params os=16.04 ignore_php5=1

# php5 is only supported on ubuntu-14.04
$THIS_DIR/../src/main.py --template Dockerfile.j2 --name all-18.04 --params os=18.04 ignore_php5=1