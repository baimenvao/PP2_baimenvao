# ==========================================
# List of movies from the task
# ==========================================
movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]


# ==========================================
# Task 1: Check if a single movie score is above 5.5
# ==========================================
# Here is a function that checks if a movie has an IMDB score above 5.5
def is_high_rated(movie):
    return movie["imdb"] > 5.5


# ==========================================
# Task 2: Sublist of movies with score above 5.5
# ==========================================
# Here is a function that returns all movies with an IMDB score above 5.5
def get_high_rated_movies(movie_list):
    return [movie for movie in movie_list if movie["imdb"] > 5.5]


# ==========================================
# Task 3: Filter movies by category
# ==========================================
# Here is a function that filters movies under a specific category
def get_movies_by_category(movie_list, category_name):
    return [movie for movie in movie_list if movie["category"].lower() == category_name.lower()]


# ==========================================
# Task 4: Average IMDB score of a list of movies
# ==========================================
# Here is a function to calculate the average IMDB score of a given movie list
def calculate_average_imdb(movie_list):
    if not movie_list:
        return 0.0
    total_score = sum(movie["imdb"] for movie in movie_list)
    return round(total_score / len(movie_list), 2)


# ==========================================
# Task 5: Average IMDB score for a specific category
# ==========================================
# Here is a function to calculate the average IMDB score of a specific category
def calculate_category_average_imdb(movie_list, category_name):
    category_movies = get_movies_by_category(movie_list, category_name)
    return calculate_average_imdb(category_movies)


# ==========================================
# Testing all 5 tasks
# ==========================================
if __name__ == "__main__":
    print("--- Task 1: Is 'Hitman' score above 5.5? ---")
    print(is_high_rated(movies[1]))  # Hitman (6.3) -> True

    print("\n--- Task 2: High rated movies count ---")
    high_rated = get_high_rated_movies(movies)
    print(f"Total high-rated movies (>5.5): {len(high_rated)}")

    print("\n--- Task 3: Movies in category 'Romance' ---")
    romance_movies = get_movies_by_category(movies, "Romance")
    for m in romance_movies:
        print(f"- {m['name']} ({m['imdb']})")

    print("\n--- Task 4: Average IMDB score of all movies ---")
    print("Average IMDB:", calculate_average_imdb(movies))

    print("\n--- Task 5: Average IMDB score of 'Suspense' movies ---")
    print("Suspense Average IMDB:", calculate_category_average_imdb(movies, "Suspense"))