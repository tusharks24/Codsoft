# Simple Content-Based Recommendation System

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Sample dataset (Movies with genres)
movies = [
    {"title": "The Matrix", "genre": "Action Sci-Fi"},
    {"title": "Inception", "genre": "Action Sci-Fi Thriller"},
    {"title": "Interstellar", "genre": "Adventure Drama Sci-Fi"},
    {"title": "The Dark Knight", "genre": "Action Crime Drama"},
    {"title": "Titanic", "genre": "Romance Drama"},
    {"title": "The Notebook", "genre": "Romance Drama"},
]

# Extract movie titles and genres
titles = [movie["title"] for movie in movies]
genres = [movie["genre"] for movie in movies]

# Convert genres to feature vectors using TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(genres)

# Function to recommend movies based on a given title
def recommend_movie(title):
    if title not in titles:
        return "Movie not found in database."

    # Get index of the movie
    idx = titles.index(title)

    # Compute cosine similarity
    cosine_sim = linear_kernel(tfidf_matrix[idx], tfidf_matrix).flatten()

    # Get top 3 similar movies (excluding itself)
    related_indices = cosine_sim.argsort()[-4:-1][::-1]

    recommendations = [titles[i] for i in related_indices]
    return recommendations

# Example usage
print("Recommendations for 'Inception':")
print(recommend_movie("Inception"))
