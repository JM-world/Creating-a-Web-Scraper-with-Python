from random import randint

user_choice = int(input("choose number."))
pc_choice = randint(1,50)

if user_choice == pc_choice:
    print("You Won!")
elif user_choice > pc_choice:
    print("Lower! Computer chose", pc_choice)
elif user_choice < pc_choice:
    print("Higher! Computer chose", pc_choice) 