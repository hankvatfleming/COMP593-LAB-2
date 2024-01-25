def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {
        'full_name': 'Hendrik Michael Vandesteeg',
        'student_id': 10312929,
        'pizza_toppings': [
            'PEPPERONI',
            'BACON STRIPS',
            'HOT PEPPERS'
        ],
        'movies': [
            {'title': 'Interstellar',
             'genre': 'Sci-Fi'},
            {'title': 'Good Will Hunting',
             'genre': 'Drama'}
        ]
    }

    # TODO: Step 3 - Add another movie to the data structure
    about_me['movies'].append({'title': 'TED', 'genre': 'Comedy'})
    print_pizza_toppings(about_me)
    print_student_name_and_id(about_me)
    return
# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(data_struct):
    full_name = data_struct['full_name']
    first_name = (full_name.split(' '))[0]
    student_id = data_struct['student_id']

    print(f"My name is {full_name}, but you can call me Sir {first_name}.")
    print(f"My student ID is {student_id}")
    return
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    
    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    pizza_toppings = about_me['pizza_toppings']
    for i in pizza_toppings:
        print(f"- {i}")

    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    return
    
if __name__ == '__main__':
    main()