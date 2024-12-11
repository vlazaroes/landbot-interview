#!/usr/bin/env bash

set -e
set -x

ruff check src tests --fix
ruff format src tests
