#!/usr/bin/env bash
# exit on error
set -o errexit

echo "==> Building Frontend..."
if [ -d "frontend" ] && [ -f "frontend/package.json" ]; then
  echo "Found frontend/ directory, building inside frontend/..."
  cd frontend
  npm install
  npm run build
  cd ..
elif [ -f "package.json" ]; then
  echo "Found package.json in root, building in root..."
  npm install
  npm run build
else
  echo "Warning: No package.json found."
fi

echo "==> Installing Python Dependencies..."
if [ -f "requirements.txt" ]; then
  pip install --upgrade pip
  pip install -r requirements.txt
elif [ -f "backend/requirements.txt" ]; then
  pip install --upgrade pip
  pip install -r backend/requirements.txt
fi

echo "==> Build completed successfully!"
