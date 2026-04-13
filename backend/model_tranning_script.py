import pandas as pd
import numpy as np
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
import ast, os

print("📥 Loading dataset...")
movies = pd.read_csv("D:/ML project/backend/movies.csv", low_memory=False)

print(f"✅ Loaded {len(movies)} movies")

# -------- CLEAN TEXT FIELDS --------
def safe_parse(text):
    """Convert stringified JSON list to a space-separated list of names or values"""
    try:
        items = ast.literal_eval(text)
        if isinstance(items, list):
            if items:  # Check if list is not empty
                result = " ".join([d.get('name', str(d)) for d in items if isinstance(d, dict)])
                print(f"Parsed {text} -> {result}")  # Debug print
                return result
            return ""
        return str(text)
    except Exception as e:
        print(f"Error parsing {text}: {e}")
        return ""

movies['genres_clean'] = movies['genres'].astype(str).apply(safe_parse)
movies['keywords_clean'] = movies['keywords'].astype(str).apply(safe_parse)
movies['production_companies_clean'] = movies['production_companies'].astype(str).apply(safe_parse)
movies['production_countries_clean'] = movies['production_countries'].astype(str).apply(safe_parse)
movies['spoken_languages_clean'] = movies['spoken_languages'].astype(str).apply(safe_parse)
movies['overview'] = movies['overview'].fillna("")

# Debug: Print a sample of cleaned data
print("Sample cleaned data:")
print(movies[['title', 'genres_clean', 'production_companies_clean', 'production_countries_clean', 'spoken_languages_clean']].head())

movies['combined'] = (
    movies['genres_clean'] + " " +
    movies['keywords_clean'] + " " +
    movies['production_companies_clean'] + " " +
    movies['production_countries_clean'] + " " +
    movies['spoken_languages_clean'] + " " +
    movies['overview']
)

# Remove empty titles or zero budgets
movies = movies.dropna(subset=['title', 'vote_average', 'vote_count', 'budget', 'revenue', 'release_date'])
movies = movies[movies['title'].notna() & (movies['budget'] > 0)]

print("✅ Cleaned and combined text features")

# -------- TF-IDF SIMILARITY MODEL --------
print("🔧 Building TF-IDF similarity matrix (this may take a bit)...")
tfidf = TfidfVectorizer(stop_words='english', max_features=5000)
tfidf_matrix = tfidf.fit_transform(movies['combined'])
similarity = cosine_similarity(tfidf_matrix, tfidf_matrix)
print("✅ Similarity matrix ready")

# -------- CLASSIFYING MOVIES BASED ON REVENUE --------
def classify_movie(row):
    if row['revenue'] >= 1_000_000_000:
        return 'Blockbuster'
    elif row['revenue'] >= 500_000_000:
        return 'Hit'
    elif row['revenue'] >= 200_000_000:
        return 'Average'
    else:
        return 'Flop'

movies['category'] = movies.apply(classify_movie, axis=1)
print("✅ Classified movies into categories")

# -------- TRAIN CLASSIFIER --------
X = movies[['vote_average', 'vote_count', 'budget', 'revenue']].fillna(0)
y = movies['category']

clf = RandomForestClassifier(n_estimators=120, random_state=42)
clf.fit(X, y)
print("✅ Classification model trained")

# -------- TRAIN REVENUE PREDICTOR --------
reg = RandomForestRegressor(n_estimators=120, random_state=42)
reg.fit(X, movies['revenue'])
print("✅ Revenue regression model trained")

# -------- SAVE MODELS --------
print("💾 Saving models...")
with open("model_recommender.pkl", "wb") as f:
    pickle.dump((movies, tfidf, similarity), f)
with open("model_classifier.pkl", "wb") as f:
    pickle.dump(clf, f)
with open("model_revenue.pkl", "wb") as f:
    pickle.dump(reg, f)

print("🎉 All models saved successfully!")
print("Files created:", [f for f in os.listdir('.') if f.endswith('.pkl')])