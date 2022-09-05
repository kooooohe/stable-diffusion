#!/bin/bash

set -eu
cd $(dirname $0)

git clone https://github.com/CompVis/stable-diffusion.git app
mkdir -p app
cp sample.py ./app/sample.py
