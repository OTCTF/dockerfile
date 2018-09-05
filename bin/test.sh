#!/bin/bash

THIS_DIR="$(cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd)"

$THIS_DIR/build-all.sh

docker build - < generated/$1/Dockerfile