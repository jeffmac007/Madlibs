# Madlib.py - Military-Themed Mad Libs Game

print("Welcome to my Military-Themed Madlib! Let's create an epic story.\n")

print("Please fill in the following prompts:\n")

# Prompt the user for inputs
military_base = input("Military Base (e.g., Camp Pendleton, Twentynine Palms): ")
adj1 = input("Adjective (describing a Marine): ")
military_rank = input("Military Rank (e.g., General, Sergeant, Corporal): ")
noun1 = input("Noun (e.g., platoon, rifle, humvee): ")
verb = input("Verb ending in -ing (e.g., charging, marching): ")
noun2 = input("Noun (e.g., stars, battlefield, flag): ")
adj2 = input("Adjective (e.g., heroic, intense): ")

# Improved story template with more inputs and fixed typos
madlib = f"""
\nAt {military_base}, a {adj1} {military_rank} led a mission with their {noun1}. 
They faced {verb} challenges and triumphed under the {noun2} sky. 
It was a truly {adj2} day for the Corps!
"""

print(madlib)

# Allow replay
while True:
    replay = input("\nWant to play again? (y/n): ").strip().lower()
    if replay != 'y':
        print("\nThanks for playing! Semper Fi! 💪")
        break
    else:
        print("\n--- New Story ---\n")
        # Re-prompt for replay
        military_base = input("Military Base: ")
        adj1 = input("Adjective: ")
        military_rank = input("Military Rank: ")
        noun1 = input("Noun: ")
        verb = input("Verb -ing: ")
        noun2 = input("Noun: ")
        adj2 = input("Adjective: ")
        madlib = f"""
At {military_base}, a {adj1} {military_rank} led a mission with their {noun1}. 
They faced {verb} challenges and triumphed under the {noun2} sky. 
It was a truly {adj2} day for the Corps!
"""
        print(madlib)

input("\nPress Enter to exit.")
