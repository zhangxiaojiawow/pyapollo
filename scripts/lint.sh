#!/bin/sh

set -e
set -x

mypy pyapollo
flake8 pyapollo
balck pyapollo tests
isort pyapollo tests --check-only