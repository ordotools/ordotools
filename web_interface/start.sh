#!/bin/bash
# Startup script for Ordotools Web Interface

cd "$(dirname "$0")"
source ../env/bin/activate
python app.py

