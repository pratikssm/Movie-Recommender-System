from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import os
import pickle
import numpy as np
import json
import pandas as pd

app = FastAPI()

# Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# === Paths ===
BASE_DIR = os.path.dirname(__file__)
FRONTEND_DIR = os.path.join(BASE_DIR, "../frontend")
STATIC_DIR = os.path.join(FRONTEND_DIR, "static")

# Mount static folder at /static
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# Serve index.html at root
@app.get("/")
async def get_index():
    return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))

# === Load models ===
movies, tfidf, similarity = pickle.load(open(os.path.join(BASE_DIR, "model_recommender.pkl"), "rb"))
clf = pickle.load(open(os.path.join(BASE_DIR, "model_classifier.pkl"), "rb"))
reg = pickle.load(open(os.path.join(BASE_DIR, "model_revenue.pkl"), "rb"))

# === Recommendation logic ===
def get_recommendations(movie_name: str):
    if movie_name not in movies['title'].values:
        return {"error": "Movie not found!"}

    idx = movies[movies['title'] == movie_name].index[0]
    distances = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda x: x[1])[1:6]

    recommendations = []
    feature_names = ['vote_average', 'vote_count', 'budget', 'revenue']  # Matches updated training features
    for i in distances:
        movie = movies.iloc[i[0]]
        X_input = pd.DataFrame([[movie['vote_average'], movie['vote_count'], movie['budget'], movie['revenue']]],
                              columns=feature_names)
        predicted_class = clf.predict(X_input)[0]
        predicted_revenue = reg.predict(X_input)[0]

        recommendations.append({
            "title": movie['title'],
            "avg_rating": round(movie['vote_average'], 2),
            "likes_percent": round((movie['vote_count'] / movies['vote_count'].max())*100, 2),
            "box_office": f"${int(predicted_revenue):,}",
            "classification": predicted_class,
            "similarity": round(float(similarity[idx][i[0]])*100, 2),
            "production_companies": movie['production_companies_clean'],
            "production_countries": movie['production_countries_clean'],
            "release_date": movie['release_date'],
            "revenue": f"${int(movie['revenue']):,}",
            "spoken_languages": movie['spoken_languages_clean'],
            "budget": f"${int(movie['budget']):,}",
            "genres": movie['genres_clean']
        })

    return {"input_movie": movie_name, "recommendations": recommendations}

# === WebSocket endpoint ===
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        try:
            data = await websocket.receive_text()
            data_json = json.loads(data)
            movie_name = data_json.get("movie_name", "").strip()
            result = get_recommendations(movie_name)
            await websocket.send_text(json.dumps(result))
        except Exception as e:
            await websocket.send_text(json.dumps({"error": str(e)}))