import random

def play_pro_game():
    # High level: Dynamic difficulty
    secret_number = random.randint(1, 100)
    lives = 5 # Limit laga di
    
    print(f"--- Level 3: Pro Mode (Sirf {lives} lives hain) ---")
    
    for i in range(1, lives + 1):
        try:
            guess = int(input(f"Attempt {i}: Guess karein 1 to 100 : "))
            
            if guess == secret_number:
                print("Legendary! Aapne computer ko hara diya.")
                return # Game khatam
            
            # Hint logic
            diff = abs(guess - secret_number)
            if diff <= 5:
                print("Aap bilkul paas hain! (Very Hot)")
            elif guess < secret_number:
                print("Thoda aur bada number...")
            else:
                print("Thoda aur chota number...")
                
        except ValueError:
            print("Error: Number hi valid hai.")
            
    print(f"Game Over! Sahi number {secret_number} tha.")

play_pro_game()