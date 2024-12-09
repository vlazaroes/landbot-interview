#!/usr/bin/env bash

set -e
set -x

ruff check src --fix
ruff format src
