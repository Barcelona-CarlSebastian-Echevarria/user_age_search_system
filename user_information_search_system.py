# Ask the user for their name and age. Make room for added input categories if possible. Edit: Make sure that the first letter on each name parts are capitalized
# Account for the error if the user failed to comply with thr prompt while maintaining the inputs already given
# Store the information into an array for information logging. Each user must have their own storage
# Give the user an option to add a category and a value if desired
# Give the user the option to continue with the program or exit
# The user names will be stored in an array as well so that the user can navigate to the different profiles already existed
# Once the user decided to exit, display the profile of the oldest person logged



# Allows multiple inputs to be included in the name 
def get_user_name():
    while True:
        user_name = input("Enter your name: ")
        user_name = user_name.split()

        name = list(user_name)
        for parts in name:
            for part in parts: 
                if part.isalpha():
                    try:
                     return (" ".join(name))
                    except:
                     return (user_name[0])
                else:
                   print("Please enter a valid name")
            
def get_user_age():
    while True:
       user_age = int(input("Enter your age: ")) 
       if user_age > 0:
          return user_age
       else:
          print("Please enter a valid age")

name = get_user_name()
age = get_user_age()
print(name, age)








    



