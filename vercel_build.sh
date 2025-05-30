#!/bin/bash
set -e

# Install Python dependencies
pip install --upgrade pip
pip install -r requirements-vercel.txt

# Create a vercel.json file if it doesn't exist
if [ ! -f vercel.json ]; then
    echo '{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    },
    {
      "src": "templates/*",
      "use": "@vercel/static"
    },
    {
      "src": "static/*",
      "use": "@vercel/static"
    }
  ],
  "routes": [
    {
      "src": "/static/(.*)",
      "dest": "/static/$1"
    },
    {
      "src": "/(.*)",
      "dest": "/app.py"
    }
  ]
}' > vercel.json
fi
