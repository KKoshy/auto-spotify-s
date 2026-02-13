#!/bin/bash
set -e

echo "Running autoflake..."
autoflake --remove-all-unused-imports \
          --remove-unused-variables \
          --recursive \
          --check .

echo "Running isort..."
isort --profile black --check-only .

echo "Running black..."
black --check . --line-length 80

echo "All lint checks passed."
