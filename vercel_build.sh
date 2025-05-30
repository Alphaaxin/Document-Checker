#!/bin/bash
# Install Python dependencies
pip install -r requirements.txt

# Install system dependencies needed for python-docx
apt-get update && apt-get install -y \
    python3-dev \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev \
    gcc
