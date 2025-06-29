# Business Card Extractor

Fully open-source business card extraction app using:
- Python (Flask + spaCy + pytesseract)
- JavaScript frontend (GitHub Pages)
- Free hosting (Render.com)

## 🛠 Setup Instructions

### Backend Deployment (Render)

1. Create free Render account: https://render.com
2. New Web Service → Connect your GitHub Repo → Choose `backend/` folder.
3. Render auto-detects `render.yaml` and deploys your backend.

### Frontend Deployment (GitHub Pages)

1. Host `frontend/` on GitHub.
2. Enable GitHub Pages (Settings → Pages → deploy from branch).

### 🔧 Update Frontend

- After backend deploy, replace `BACKEND_URL` in `index.html` with your Render backend URL.

🚀 Done.
