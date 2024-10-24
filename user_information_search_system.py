# Ask the user for their name and age. Make room for added input categories if possible. Edit: Make sure that the first letter on each name parts are capitalized
# Account for the error if the user failed to comply with the prompt while maintaining the inputs already given
# Store the information into an array for information logging. Each user must have their own storage
# Give the user an option to add a category and a value if desired
# Give the user the option to continue with the program or exit
# The usernames will be stored in an array as well so that the user can navigate to the different profiles already existed
# Edit: Let the user view the information so far logged and provides option for further edits or proceed to exit
# Once the user decided to exit, display the profile of the oldest person logged
# Edit: Filter the inputted information to keys name, age and its values to be uploaded in the csv file
# Edit: Add all the filtered information inputted to a csv file
import csv

main_list = []
number_list = []

# Allows multiple inputs to be included in the name
# Converts the name to a list to accommodate multiple word inputs, then make it a single word so that the .isalpha can be activated
def get_user_name():
    while True:
        user_name = input("Enter your name: ")
        user_name = user_name.split()
        name = (''.join(user_name))
        letter_count = len(name)
        if name.isalpha() and letter_count >= 2:
            name = (' '.join(user_name))
            # Makes the first letters of the words capitalized
            name = name.title()
            return name
        else:
            print("Enter a valid name")

# Asks for the user age
# Will only limit the inputs to greater than zero since there are animals that can live for a thousand years
def get_user_age():
    while True:
        try:
            user_age = int(input("Enter your age: "))
            if user_age > 0:
                return user_age
            else:
                print("Please enter a valid age")
        except ValueError:
            print("Enter a numerical input only")

# Create an individual user dictionary and appends the user age to the number_list
def create_user_dictionary():
    name_of_user = get_user_name()
    age_of_user = get_user_age()
    number_list.append(age_of_user)
    # Creates a dictionary for the given inputs
    user_dictionary = dict(name=name_of_user, age=age_of_user)
    return user_dictionary

# Adds a new feature to the dictionary
def add_dictionary_feature():
    user_dictionary = create_user_dictionary()
    while True:
        new_feature = input("Do you want to add another feature to your dictionary (type 'y' or 'yes' to proceed, 'n' or 'no' to exit): ").lower()
        if new_feature == "y" or new_feature == "yes":
            while True:
                dictionary_key = input("Enter a key: ")
                dictionary_value = input("Input the value of the key you provided: ")
                if len(dictionary_value) >= 2 and len(dictionary_key) >= 2:
                    user_dictionary.update({dictionary_key: dictionary_value})
                    break
                else:
                    print("Please input a value and key that's greate than or equal to two letters (numbers are accepted regardless)")
        elif new_feature == "n" or new_feature == "no":
            break
        else:
            print("Please respond with words/characters specified only")

    return user_dictionary

# Uploads the contents in the main list to a csv file
def csv_upload():
    # The block of code used in this function is sourced from www.geeksforgeeks.org. I just tailored it according to my needs
    file_path = 'user_information_log.csv'
    with open(file_path, 'w', newline='') as csvfile:
        fieldnames = ['name', 'age']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        # This is my own version of the same block I committed previously. I just want to do this so I can call it my own
        # Filter keys name, age and its values, to be uploaded in the file
        filtered_list = []
        for items in main_list:
            for items in main_list:
                name_key = items['name']
                age_key = items['age']
                dictionary = dict(name= name_key, age= age_key)
                filtered_list.append(dictionary)
        writer.writerows(filtered_list)

    return f"Data uploaded to {file_path} successfully"

# Prints the users with oldest age and shows their profiles at user's choice
def oldest_age_printer():
    display_upload_successfully = csv_upload()
    profile_information_storage = []
    print(f"Profile with oldest age:")
    highest_age = max(number_list)
    for dictionaries in main_list:
        if dictionaries["age"] == highest_age:
            name = dictionaries["name"]
            age = dictionaries["age"]
            profile_information_storage.append(dictionaries)
            print(f'Name: {name}, Age: {age}')

    print(display_upload_successfully)

    while True:
        profile_viewing = input("View profile? (type 'y' or 'yes' to proceed, 'n' or 'no' to exit): ").lower()
        if profile_viewing == "y" or profile_viewing == "yes":
            break
        elif profile_viewing == "n" or profile_viewing == "no":
            quit()
        else:
            print("Please respond using the specified")

    for profiles in profile_information_storage:
        print(profiles)

# Adds new dictionary to the main list
def edit_main_list():
    while True:
        new_user_dictionary = input(
            "Do you want to create a dictionary for another user (type 'y' or 'yes' to proceed, 'n' or 'no' to exit): ").lower()
        if new_user_dictionary == "y" or new_user_dictionary == "yes":
            new = add_dictionary_feature()
            main_list.append(new)
        elif new_user_dictionary == "n" or new_user_dictionary == "no":
            return None
        else:
            print("Enter an input using the characters/words provided")

# Handle all the program functionalities
def main_system():
    dictionary_created = add_dictionary_feature()
    main_list.append(dictionary_created)
    while True:
        appended_dictionary = edit_main_list()
        if appended_dictionary == None:
            break

    while True:
        view_all_profiles = input(
            "Before exiting, do you want to see all the profiles you've logged in? (type 'y' or 'yes' to proceed, 'n' or 'no' to exit): ").lower()
        if view_all_profiles == "y" or view_all_profiles == "yes":
            print(main_list)
            to_exit = input("Please press 'n' to exit or 'e' if you want to add a user profile (This is the last time you can edit): ")
            if to_exit == 'e':
                while True:
                    # Provide's the user with option to add a user dictionary while viewing all inputted information
                    final_edit_option = edit_main_list()
                    if final_edit_option == None:
                        break
            elif to_exit == 'n':
                oldest_age_printer()
                break
            else:
                print("please respond using only what's specified")
        elif view_all_profiles == "n" or view_all_profiles == "no":
            oldest_age_printer()
            break
        else:
            print("Enter an input using the characters/words provided")

main_system()

