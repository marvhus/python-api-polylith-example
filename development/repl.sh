#!/usr/bin/env bash

if [[ -z "$1" ]]; then
    echo "Usage: $0 <env name>"
    exit 1
fi

pushd $(dirname $0)

CHOSEN_ENV=$1
if [[ ! -f ${CHOSEN_ENV} ]]; then
    echo "Unable to find file: ${CHOSEN_ENV}"
    exit 1
fi

uv sync
source ../.venv/bin/activate
ipython -i ${CHOSEN_ENV}
deactivate

popd
