#!/usr/bin/env bash

# $ docker run --rm --name omf-grip-run -p 5100:5100 nreca/omf
# $ docker stop omf-grip-run
# $ docker rm omf-grip-run

cwd="$(pwd)"
cd "$(dirname "${BASH_SOURCE[0]}")"
build_context="$(pwd)"/../../..
docker build -f grip.Dockerfile -t nreca/omf "$build_context"
cd "$cwd"
