movies = []


def add_movie():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")
    movies.append({
        'title': title,
        'director': director,
        'year': year
    })


def print_movies(movies_to_print):
    for movie in movies_to_print:
        print(f"The movie {movie['title'].capitalize()} was released in {movie['year']} by {movie['director'].capitalize()}")


def find_movie():
    choice = input("Enter how you want to find movie: 't' by title, 'd' by director, or 'y' by release year: ")
    if choice == 't':
        value = input("Enter movie title: ")
        return filter_data(movies, "title", value)
    elif choice == 'd':
        value = input("Enter movie director: ")
        return filter_data(movies, "director", value)
    elif choice == 'y':
        value = input("Enter movie released: ")
        return filter_data(movies, "year", value)
    else:
        print('Unknown command. Please try again.')


def filter_data(data, field_name, value):
    filtered_data = [item for item in data if value == item[field_name]]
    return filtered_data


menu_prompt = "a) add a movie\n" \
              "l) see your movies\n" \
              "f) find a movie\n" \
              "q) quit\n"

selection = input(menu_prompt)


while selection != 'q':
    if selection == 'a':
        add_movie()
    elif selection == 'l':
        print_movies(movies)
    elif selection == 'f':
        found_movies = find_movie()
        print_movies(found_movies)
    else:
        print('Unknown command. Please try again!')
    selection = input(menu_prompt)
