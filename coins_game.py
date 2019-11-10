user_coins = 0

print("You currently have:", user_coins, "coins.")
while True:
    user_answer = input("Do you want another? ")
    print(user_answer)
    if user_answer == "yes":
        user_coins += 1
        print(f"You currently have:", user_coins, "coins.")
    else:
        print("Bye!")
        break