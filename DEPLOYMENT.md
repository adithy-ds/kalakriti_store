# Deployment Guide — KALAKRITI Full-Stack Website

This guide walks you through deploying your **React Frontend + FastAPI Backend** full-stack website to **Render** or **Railway** for free/low-cost with automatic SSL and continuous deployment.

---

## Option 1: Deploy on Render (Recommended & Easiest)

Render can build your React frontend and run your FastAPI backend as a single unified web service.

### Step 1: Push your project to GitHub
1. Initialize git and commit your files (if not already done):
   ```bash
   git init
   git add .
   git commit -m "Deploy Kalakriti full-stack site"
   ```
2. Create a new repository on [GitHub](https://github.com/new) and push your code:
   ```bash
   git remote add origin https://github.com/<your-username>/<your-repo-name>.git
   git branch -M main
   git push -u origin main
   ```

### Step 2: Deploy on Render
1. Go to [dashboard.render.com](https://dashboard.render.com/) and sign in with GitHub.
2. Click **New +** → **Web Service**.
3. Select your repository from GitHub.
4. Fill in the following settings:
   - **Name**: `kalakriti-boutique` (or your choice)
   - **Region**: Closest to you (e.g., Singapore or Frankfurt)
   - **Branch**: `main`
   - **Runtime**: `Python`
   - **Build Command**:
     ```bash
     npm --prefix frontend install && npm --prefix frontend run build && pip install -r requirements.txt
     ```
   - **Start Command**:
     ```bash
     uvicorn backend.main:app --host 0.0.0.0 --port $PORT
     ```
5. Under **Environment Variables**, add:
   - `GEMINI_API_KEY`: *(Optional: Your Google Gemini API Key if you want server-side AI key)*
6. Click **Create Web Service**.

Render will automatically build your frontend, start your FastAPI backend, and give you a live URL like `https://kalakriti-boutique.onrender.com`.

---

## Option 2: Deploy on Railway (1-Click Docker)

Railway automatically detects the included [`Dockerfile`](./Dockerfile) and deploys both frontend and backend seamlessly.

1. Go to [railway.app](https://railway.app/) and login with GitHub.
2. Click **New Project** → **Deploy from GitHub repo**.
3. Select this repository.
4. Railway will automatically detect the `Dockerfile`, build the React UI, and launch the server.
5. In your project settings, click **Generate Domain** to get your public `.up.railway.app` URL.

---

## Option 3: Deploy via Vercel (Frontend) + Render (Backend)

If you prefer Vercel for the frontend:
1. **Deploy Backend**: Deploy the backend folder to Render or Railway using `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`.
2. **Deploy Frontend**: Import the `frontend` directory into [Vercel](https://vercel.com/), configure `/api` rewrites in `vercel.json` pointing to your deployed backend URL.

---

## Testing Your Live Deployment

Once deployed:
1. Visit your live URL in the browser.
2. Test browsing the collection, viewing garment details, adding to bag, and interacting with the AI Stylist.
