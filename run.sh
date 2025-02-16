#!/usr/bin/env bash

# Exit on error
set -e

# Check for argument
if [ -z "$1" ]; then
    echo "Usage:  $0 <project>"
    exit 1
fi

PROJECT=$1

#Check if project exits
PROJECT_DIR="projects/${PROJECT}"
if [ ! -d "$PROJECT_DIR" ]; then
    echo "Unable to find project:  $PROJECT_DIR"
    exit 1
fi

echo "=============== Running project ==============="
pushd ${PROJECT_DIR}
uv sync
uv run uvicorn marvhus.${PROJECT}.core:app --reload || { popd; exit 1; }
popd
