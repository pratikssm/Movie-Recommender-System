# 🎬 Movie Recommender System

A machine learning-powered web application that recommends movies based on user input. The system uses content-based filtering with TF-IDF vectorization and cosine similarity to find similar movies from a comprehensive movie database.

---

## 📋 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [Project Components](#project-components)
- [API Endpoints](#api-endpoints)
- [Troubleshooting](#troubleshooting)

---

## ✨ Features

- **Movie Search & Recommendations**: Search for any movie and get similar recommendations
- **Content-Based Filtering**: Uses TF-IDF vectorization and cosine similarity
- **Multiple ML Models**:
  - Movie Recommendation Model (similarity-based)
  - Genre Classification Model (predicts movie type)
  - Revenue Prediction Model (estimates box office)
- **Fast API Backend**: Built with FastAPI for high performance
- **Interactive Frontend**: Clean, responsive web interface
- **Real-time Processing**: Instant recommendations without page reload

---

## 📁 Project Structure

```
Movie Recommender System/
├── backend/
│   ├── server.py                    # FastAPI server (main backend)
│   ├── model_tranning_script.py    # ML model training script
│   ├── model_recommender.pkl       # Trained recommendation model
│   ├── model_classifier.pkl        # Trained genre classifier
│   ├── model_revenue.pkl           # Trained revenue predictor
│   ├── movies.csv                  # Movie dataset (add this file)
│   ├── .gitignore                  # Git ignore for model files
│   └── README.me                   # Backend-specific notes
├── frontend/
│   ├── index.html                  # Main page
│   ├── static/
│   │   ├── style.css              # Styling
│   │   ├── script.js              # Frontend logic
│   │   └── tempCodeRunnerFile.js  # Temporary file (can delete)
├── .gitattributes                  # Git configuration
└── README.md                       # This file
```

---

## 🔧 Prerequisites

Before starting, make sure you have:

- **Python 3.8 or higher** - [Download here](https://python.org/)
- **pip** (usually comes with Python)
- **Git** (optional, for version control) - [Download here](https://git-scm.com/)
- **Windows/Mac/Linux** operating system

### Check Your Python Installation:

```bash
python --version
pip --version
```

---

## 💾 Installation

### Step 1: Clone or Download the Project

```bash
# Using Git
git clone https://github.com/pratikssm/Movie-Recommender-System.git
cd "Movie Recommendar System"

# OR manually download and extract the ZIP file
```

### Step 2: Create a Virtual Environment (Recommended)

Create a virtual environment to keep dependencies isolated:

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` at the beginning of your terminal line.

### Step 3: Install Python Dependencies

```bash
pip install fastapi uvicorn python-multipart pandas numpy scikit-learn
```

Or install from a requirements file (if you have one):

```bash
pip install -r requirements.txt
```

### Step 4: Prepare the Dataset

You need the `movies.csv` file in the `backend/` folder:
- Download it from [The Movie Database (TMDb) Kaggle dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- Or use any CSV file with movie data containing columns like: `title`, `genres`, `keywords`, `overview`, etc.
- Place it in: `backend/movies.csv`

---

## 🚀 How to Run

### **Option 1: Quick Start (Recommended)**

#### Step 1: Start the Backend Server

Open a terminal and navigate to the project folder:

```bash
# Windows
cd backend
python server.py

# Mac/Linux
cd backend
python3 server.py
```

You should see:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
```

#### Step 2: Open the Frontend

- Open your web browser
- Go to: **http://localhost:8000**
- You should see the Movie Recommender interface

#### Step 3: Use the Application

1. Type a movie name in the search box (e.g., "The Matrix")
2. Click **"Recommend"** button
3. Get 5 similar movie recommendations!

---

### **Option 2: Using FastAPI Development Server**

If you want more control:

```bash
# Navigate to backend folder
cd backend

# Run with custom port (optional)
uvicorn server:app --host 127.0.0.1 --port 8000 --reload
```

The `--reload` flag automatically restarts the server when you change code.

---

## 📚 Project Components

### **Backend (`backend/server.py`)**

**What it does:**
- Loads pre-trained ML models from pickle files
- Serves a REST API with recommendation endpoints
- Provides static files (frontend) to users
- Handles CORS (Cross-Origin Resource Sharing)

**Key features:**
```python
- FastAPI web framework
- 3 ML models loaded:
  - model_recommender.pkl: Recommendation engine
  - model_classifier.pkl: Genre classification
  - model_revenue.pkl: Revenue prediction
```

### **Frontend (`frontend/index.html` + `static/`)**

**What it does:**
- User interface for searching movies
- Displays recommendations in real-time
- Communicates with backend API

**Files:**
- `index.html`: Main HTML structure
- `style.css`: Visual styling (colors, layout, responsive design)
- `script.js`: JavaScript logic (handles user input, API calls)

### **ML Models**

**Recommendation Model:**
- Uses TF-IDF vectorization to convert movie descriptions to numerical vectors
- Calculates cosine similarity between movies
- Returns top 5 most similar movies

**Genre Classifier:**
- Random Forest model trained to predict movie genre
- Takes movie features as input

**Revenue Predictor:**
- Random Forest regressor to estimate box office revenue
- Based on budget, vote count, and other factors

---

## 🔌 API Endpoints

### **GET `/`**
- Serves the main HTML page
- Response: HTML file

### **GET `/static/*`**
- Serves CSS, JavaScript, and other static files
- Response: Static assets

### **GET `/api/recommend?movie={movie_name}`**
*(If implemented in backend)*
- Returns 5 movie recommendations
- Response: JSON with movie data

**Example request:**
```bash
curl "http://localhost:8000/api/recommend?movie=The%20Matrix"
```

---

## 🔧 Training New Models

If you want to retrain the models with a different dataset:

```bash
# Update the CSV path in model_tranning_script.py first
cd backend
python model_tranning_script.py
```

This will:
1. Load the movie dataset
2. Clean and preprocess the data
3. Train the TF-IDF vectorizer
4. Train Random Forest classifier and regressor
5. Save models as pickle files

---

## 📊 Environment Variables (Optional)

You can set custom configurations:

```bash
# Windows
set FASTAPI_ENV=production
set DATABASE_URL=your_database_url

# Mac/Linux
export FASTAPI_ENV=production
export DATABASE_URL=your_database_url
```

---

## ❌ Troubleshooting

### **Problem: "ModuleNotFoundError: No module named 'fastapi'"**
```bash
# Solution: Install dependencies
pip install fastapi uvicorn
```

### **Problem: "Port 8000 already in use"**
```bash
# Solution: Use a different port
uvicorn server:app --port 8001
```

### **Problem: "Model file not found: model_recommender.pkl"**
- Check that all `.pkl` files are in the `backend/` folder
- Retrain models using `model_tranning_script.py`

### **Problem: "Movie not found!"**
- Make sure the movie name is spelled correctly
- Try a more famous movie (e.g., "The Matrix", "Inception")

### **Problem: CORS errors in browser console**
- Backend handles CORS, but check that server is running
- Try scrolling down to see network errors in browser DevTools

---

## 🛠️ Development Tips

### **Using VS Code:**
1. Open the project folder in VS Code
2. Install Python extension
3. Select the virtual environment interpreter
4. Use F5 to debug

### **Testing API endpoints:**
```bash
# Use PowerShell or curl to test
curl "http://localhost:8000/"
```

### **Enable Debug Mode:**
Edit `server.py` and add:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

---

## 🚀 Deployment

To deploy this project:

1. **Heroku:**
   ```bash
   heroku login
   heroku create your-app-name
   git push heroku main
   ```

2. **AWS/Azure/Google Cloud:**
   - Containerize with Docker
   - Deploy using their platforms

3. **Local Network:**
   ```bash
   uvicorn server:app --host 0.0.0.0 --port 8000
   ```
   Access from other machines: `http://your-ip:8000`

---

## 📝 License

This project is open source. Feel free to use, modify, and distribute.

---

## 👨‍💻 Author

**Pratik Kumar**  
👤 GitHub: [pratikssm](https://github.com/pratikssm)

---

## 📧 Support

For issues or questions:
1. Check the [Troubleshooting](#troubleshooting) section
2. Create a GitHub issue
3. Email: pratikssm8551@gmail.com

---

## 📚 Learning Resources

- **FastAPI Docs:** https://fastapi.tiangolo.com/
- **Scikit-learn ML:** https://scikit-learn.org/
- **TF-IDF Vectorization:** https://en.wikipedia.org/wiki/Tf%E2%80%93idf
- **Cosine Similarity:** https://en.wikipedia.org/wiki/Cosine_similarity

---

## 🎯 Future Improvements

- [ ] Add database for storing user preferences
- [ ] Implement user authentication
- [ ] Add collaborative filtering
- [ ] Create mobile app
- [ ] Add more filtering options (genre, year, rating)
- [ ] Implement WebSocket for real-time recommendations

---

**Happy recommending! 🍿**
