"""
Root entrypoint for Kalakriti Web Service on Render / Cloud platforms.
Allows running with either:
  uvicorn main:app --host 0.0.0.0 --port $PORT
or
  uvicorn backend.main:app --host 0.0.0.0 --port $PORT
"""
import os
import sys

# Ensure root and backend are in sys.path
root_dir = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.join(root_dir, "backend")

if root_dir not in sys.path:
    sys.path.insert(0, root_dir)
if os.path.exists(backend_dir) and backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

try:
    from backend.main import app
except ImportError:
    from main import app

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
