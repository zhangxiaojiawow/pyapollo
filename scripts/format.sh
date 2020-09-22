#!/bin/sh -e
set -x

autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place pyapollo --exclude=__init__.py
black pyapollo
isort pyapollo