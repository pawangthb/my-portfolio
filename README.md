# 🚀 My-Portfolio
A production-ready, full-stack portfolio with a React frontend and Express backend contact form.
## 🗂️ Directory Structure
```
portfolio/
├── frontend/                 ← React + Vite + Tailwind
│   ├── src/
│   │   ├── components/
│   │   │   ├── Navbar.jsx    ← Sticky nav with mobile menu
│   │   │   ├── Hero.jsx      ← Animated hero + type animation
│   │   │   ├── About.jsx     ← Stats + traits grid
│   │   │   ├── Skills.jsx    ← Animated progress bars
│   │   │   ├── Projects.jsx  ← Filterable project cards
│   │   │   ├── Experience.jsx← Timeline (work + education)
│   │   │   ├── Contact.jsx   ← Form → hits backend API
│   │   │   └── Footer.jsx
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css         ← Tailwind + custom utilities
│   ├── vercel.json           ← Vercel SPA routing fix
│   ├── .env.example          ← VITE_API_URL
│   ├── tailwind.config.js
│   ├── vite.config.js
│   └── package.json
│
├── backend/                  ← Node.js + Express
│   ├── src/
│   │   ├── routes/
│   │   │   └── contact.js    ← POST /api/contact (rate-limited + validated)
│   │   ├── controllers/
│   │   │   └── contact.controller.js ← Nodemailer (notify you + auto-reply)
│   │   └── index.js          ← Express app (CORS, Helmet, Morgan)
│   ├── render.yaml           ← One-click Render.com deploy
│   ├── .env.example
│   └── package.json
│
└── README.md
```

## ⚡ Quick Start (Local)

### Backend
```bash
cd backend
npm install
cp .env.example .env        # Fill in Gmail credentials
npm run dev                 # Runs on :5000
```

### Frontend
```bash
cd frontend
npm install
cp .env.example .env.local  # Set VITE_API_URL=http://localhost:5000
npm run dev                 # Runs on :3000
```

## 🌐 Deploy to Production

### 1. Deploy Backend → Render.com (Free)
1. Push to GitHub
2. Go to **render.com** → New Web Service → connect repo
3. Root Directory: `backend`
4. Set env vars from `.env.example`
5. Deploy — get your URL: `https://portfolio-backend.onrender.com`

### 2. Deploy Frontend → Vercel (Free)
1. Go to **vercel.com** → Import project
2. Root Directory: `frontend`
3. Add env var: `VITE_API_URL=https://portfolio-backend.onrender.com`
4. Deploy → live in ~60 seconds!

## 📧 Gmail Setup (for contact form)
1. Enable 2-Factor Authentication on your Google account
2. Go to **Google Account → Security → App Passwords**
3. Create an App Password for "Mail"
4. Paste it into `GMAIL_APP_PASSWORD` in your `.env`

## 🛡️ Security Features
- Rate limiting (5 req / 15 min per IP)
- Input validation & sanitization
- CORS whitelist
- Helmet HTTP headers
- Body size limits (10KB)

## 🎨 Customization
- Edit `frontend/src/components/` to update content
- Replace project data in `Projects.jsx`
- Update socials/links in `Navbar.jsx` and `Hero.jsx`
- Colors in `tailwind.config.js`
