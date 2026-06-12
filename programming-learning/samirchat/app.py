import random

print("\n--- Welcome to Level 2: Guess the Number ---")

# 1 se 10 ke beech ek random number
secret_number = random.randint(1, 10)
attempts = 0

# Loop chalana taki user baar-baar guess kar sake
while True:
    guess = int(input("1 se 10 ke beech ek number guess karein: "))
    attempts += 1
    
    if guess < secret_number:
        print("Thoda bada number sochiye!")
    elif guess > secret_number:
        print("Thoda chota number sochiye!")
    else:
        print(f"Badhai ho! Aapne {attempts} koshishon mein sahi guess kiya.")
        break # Sahi guess milne par loop rok dena