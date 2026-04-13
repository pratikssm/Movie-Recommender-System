# 🚀 Quick Start Guide

**5 minutes mein project run kren!**

---

## Step 1: Virtual Environment Setup (1 minute)

```bash
# Navigate to project folder
cd "Movie Recommendar System"

# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate
```

You should see `(venv)` in terminal.

---

## Step 2: Install Dependencies (1 minute)

```bash
pip install -r requirements.txt
```

---

## Step 3: Download Dataset (Optional but Recommended)

- Download from: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata
- Extract `tmdb_5000_movies.csv` 
- Place it in `backend/` folder as `movies.csv`
- OR rename any existing CSV file in backend/

---

## Step 4: Start Backend Server (1 minute)

```bash
cd backend
python server.py
```

**Expected output:**
```
INFO:     Started server process [1234]
INFO:     Uvicorn running on http://127.0.0.1:8000
```

---

## Step 5: Open in Browser (1 minute)

1. Open **http://localhost:8000** in your web browser
2. You should see the Movie Recommender interface

---

## Step 6: Test It! (1 minute)

1. Type a movie name: **"The Matrix"** or **"Inception"**
2. Click **"Recommend"** button
3. See 5 similar movie recommendations!

---

## ✅ All Done!

Your Movie Recommender System is now running! 🎉

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `ModuleNotFoundError` | Run: `pip install -r requirements.txt` |
| Port 8000 in use | Run: `uvicorn server:app --port 8001` |
| "Movie not found" | Check spelling or try famous movies |
| models not loading | Train them: `python model_tranning_script.py` |

---

## What Next?

- Read [README.md](README.md) for detailed documentation
- Check [backend/README.me](backend/README.me) for backend details
- Modify `static/style.css` to customize UI
- Edit `static/script.js` to add new features

---

**Happy Coding! 💻**
