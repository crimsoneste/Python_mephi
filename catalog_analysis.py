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
        return tuple() # Возвращаем пустой кортеж, если список пуст
    
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
        # Тернарный оператор: если оценка 9.5, вернет "шедевр высшего класса", иначе "шедевр"
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
            # Сюда попадут все остальные годы (раньше 2015)
            return "старые"

        
if __name__ == "__main__":
    print("--- Проверка rating_tier ---")
    for r in [9.8, 9.0, 8.5, 7.0, 6.9, 5.0, 4.9]:
        print(f"Оценка {r}: {rating_tier(r)}")

    print("\n--- Проверка decade_label ---")
    for y in [2025, 2021, 2020, 2018, 2015, 2014, 1990]:
        print(f"Год {y}: {decade_label(y)}")