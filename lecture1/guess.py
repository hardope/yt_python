from random import randint

def get_user_input():

    while True:

        user_inp = input("Guess: ")
        try:
            return int(user_inp)
        except:
            print("That is not a number!")

def generate_random_number():

    return randint(1, 20)

random_number = generate_random_number()
user_value = -1

for i in range(5):

    user_value = get_user_input()

    if user_value == random_number:

        break

    else:

        if user_value < random_number:

            print("Higher")
        
        else:

            print("Lower")

if user_value == random_number:

    print("Correct")