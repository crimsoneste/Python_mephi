import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]


def average_rating(movies):

    if not movies:
        return 0.0
    
    total_rating = sum(movie["rating"] for movie in movies)
    avg = total_rating / len(movies)
    
    return round(avg, 1)


def catalog_age_stats(movies, current_year=2026):

    if not movies:
        return tuple() 
    
    ages = [current_year - movie["year"] for movie in movies]
    
    oldest = max(ages)
    newest = min(ages)
    average = math.ceil(sum(ages) / len(ages))
    
    return tuple([oldest, newest, average])


def duration_in_hours(minutes):

    hours = minutes // 60       
    mins = minutes % 60        
    
    return f"{hours}ч {mins}м"

def rating_tier(rating):
    if rating >= 9:
        # Тернарный оператор
        return "шедевр высшего класса" if rating > 9.5 else "шедевр"
    elif 7 <= rating <= 8.9:
        return "хорошо"
    elif 5 <= rating <= 6.9:
        return "средние"
    else:
        return "слабо"


def decade_label(year):
    match year:
        case y if y > 2020:
            return "новые"
        case y if 2015 <= y <= 2020:
            return "недавние"
        case _:
            return "старые"


""" print("--- Фильмы не в жанре comedy ---")
for movie in movies:
    if "comedy" in movie["genres"]:
        continue  
    print(movie["title"])


print("\n--- Поиск шедевра (рейтинг > 9.0) ---")
index = 0
found = False 

while index < len(movies):
    if movies[index]["rating"] > 9.0:
        print(f"Найден шедевр: {movies[index]['title']}")
        found = True
        break  
    index += 1
else:
    print("Шедевров не найдено") """

def count_long_movies(movies, threshold=120):
    count = 0  
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count


def normalize_title(title):
    words = title.split()
    normalized_words = []
    
    for word in words:
        normalized_words.append(word[0].upper() + word[1:])
        
    return " ".join(normalized_words)


def make_slug(title):
    slug = title.lower()
    slug = slug.replace(" ", "-")
    return slug


def format_report_line(movie):
    duration = duration_in_hours(movie["duration_min"])
    sorted_genres = ", ".join(sorted(movie["genres"]))
    
    # Собираем итоговую строку. 
    return f'"{movie["title"]}" ({movie["year"]}) — {movie["rating"]}/10, {duration}, жанры: {sorted_genres}'


if __name__ == "__main__":
    print("--- Проверка этапа 4 ---")
    
    print(normalize_title("silent hours"))        # Ожидается: Silent Hours
    print(normalize_title("midnight in oslo"))    # Ожидается: Midnight In Oslo
    
    print(make_slug("Silent Hours"))              # Ожидается: silent-hours
    print(make_slug("The Quiet Algorithm"))       # Ожидается: the-quiet-algorithm
    
    print(format_report_line(movies[7]))          
    # Ожидается: "The Quiet Algorithm" (2024) — 9.2/10, 1ч 58м, жанры: drama, sci-fi