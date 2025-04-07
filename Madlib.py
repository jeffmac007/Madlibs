# Madlib.py
print("Welcome to my Madlib! Lets create a military-themed story.\n")
# This is a Madlib script that prompts the user for inputs to create a military-themed story.
# It uses string formatting to insert user inputs into a predefined story template.
# The script begins by printing a welcome message and then prompts the user for various inputs.

print("Please fill in the following prompts:\n")

# Prompt the user for inputs
military_base = input("Military Base (e.g., Twentynine Palms, or make one up: ")
adj = input("Adjective: ")
military_rank = input("Military Rank (e.g. General, Corporal, Private, etc.): ")
noun1 = input("Noun: ")
verb = input("Verb: ")
noun2 = input("Noun: ")

madlib = f"\nAt {military_base}, a {adj} {military_rank}, led a mission with their {noun1}. They faced a {verb}-ing challenges and triumped under the {noun2} sky!"

print(madlib)
# The script ends by printing the completed Madlib story.
input("\nPress Enter to exit.")