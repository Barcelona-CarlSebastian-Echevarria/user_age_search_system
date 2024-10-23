# Ask the user for their name and age. Make room for added input categories if possible. Edit: Make sure that the first letter on each name parts are capitalized
# Account for the error if the user failed to comply with thr prompt while maintaining the inputs already given
# Store the information into an array for information logging. Each user must have their own storage
# Give the user an option to add a category and a value if desired
# Give the user the option to continue with the program or exit
# The user names will be stored in an array as well so that the user can navigate to the different profiles already existed
# Once the user decided to exit, display the profile of the oldest person logged


main_list = []
# Allows multiple inputs to be included in the name
# Converts the name to a list to accomodate multiple inputs, then make it a single word so that the .isalpha can be activated
def get_user_name():
    while True:
        user_name = input("Enter your name: ")
        user_name = user_name.split()
        name = (''.join(user_name))
        if name.isalpha():
            name = name.title()
            # Makes the first letters of the words capitalized
            return name
        else:
            print("Enter a valid name")

# Asks for the user age      
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

# Create an individual user dictionaru
def create_user_dictionary():
    name_of_user = get_user_name()
    age_of_user = get_user_age()
    user_dictionary = dict(name=name_of_user, age=age_of_user)
    # Creates a dictionary for the given values
    return user_dictionary

def add_dictionary_feature():
    user_dictionary = create_user_dictionary()
    while True:
        new_feature = input("Do you want to add another feature to your dictionary (press 'y' for proceed, 'n' to exit): ")
        if new_feature  == "y" or new_feature == "yes":
            while True:
                dictionary_key = input("Enter a  key: ")
                dictionary_value = input("Input the value ot the key you provided: ")
                return user_dictionary.update({dictionary_key: dictionary_value})
        elif new_feature  == "n" or new_feature == "no":
            break
        else:
            print("Please respond with words/characters specified only")

    return user_dictionary
    
def main_system():
    dictionary_created = add_dictionary_feature()
    main_list.append(dictionary_created)
    while True:
        new_user_dictionary = input("Do you want to create a dictionary for another user (type 'y' or 'yes' to proceed, 'n' or 'no' to exit): ")
        if new_user_dictionary == "y" or new_user_dictionary == "yes":
            new = add_dictionary_feature()
            main_list.append(new)
        elif new_user_dictionary == "n" or new_user_dictionary == "no":
            break
        else:
            print("Enter an input using the characters/words provided")

    return main_list

res = main_system()
print(res)



    











    



