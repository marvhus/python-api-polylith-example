#!/usr/bin/env bash

echo "=============== Building project ==============="
uv export --no-emit-project --output-file requirements.txt
uv build --out-dir ./dist

sudo docker rm api_foo_container || echo "=============== No existing container ==============="

echo "=============== Building container ==============="
sudo docker build -t api_foo .

echo "=============== Running container ==============="
sudo docker run --name api_foo_container -p 8000:8000 api_foo
