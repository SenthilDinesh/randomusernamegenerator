import random
import string
import csv
import os  

adjectives = ["Cool", "Happy", "Brave", "Fast", "Sneaky", "Fierce", "Calm", "Wise", "Jolly", "Clever",
              "Vigorous", "Mighty", "Swift", "Bold", "Loyal", "Serene", "Graceful", "Noble", "Quiet", "Cunning",
              "Energetic", "Strong", "Majestic", "Diligent", "Fearless", "Mysterious", "Brilliant", "Dashing",
              "Determined", "Curious", "Playful", "Inventive", "Vibrant", "Radiant", "Shy", "Confident", "Optimistic",
              "Resilient", "Eager", "Generous", "Reliable", "Cheerful", "Adventurous", "Courageous", "Witty",
              "Persistent", "Resourceful", "Tough", "Humble"]

nouns = ["Tiger", "Dragon", "Eagle", "Knight", "Wizard", "Panther", "Pirate", "Phoenix", "Shark", "Samurai",
         "Lion", "Elephant", "Falcon", "Unicorn", "Wolf", "Peacock", "Swan", "Cheetah", "Horse", "Fox", "Raven",
         "Hawk", "Bear", "Jaguar", "Beaver", "Leopard", "Octopus", "Whale", "Jaguar", "Shark", "Turtle", "Koala",
         "Dragonfly", "Panda", "Butterfly", "Fawn", "Goose", "Pelican", "Monkey", "Dolphin", "Otter", "Squirrel",
         "Chipmunk", "Kangaroo", "Buffalo", "Parrot", "Beagle", "Sparrow", "Eagle", "Alligator", "Lynx"]

random_pairs = [(random.choice(adjectives), random.choice(nouns)) for _ in range(1000)]

with open('./adjective_noun_dataset.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['adjective', 'noun']) 
    writer.writerows(random_pairs)  

print("CSV file 'adjective_noun_dataset.csv' generated successfully.")
def load_data(filename):
   
    adjectives = []
    nouns = []
    with open(filename, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            adjectives.append(row['adjective'])
            nouns.append(row['noun'])
    
    return adjectives, nouns

def generate_username(include_numbers, include_specials, length, adjectives, nouns):
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    username = adjective + noun

    if include_numbers:
        username += str(random.randint(0, 999))  
    if include_specials:
        special_char = random.choice(string.punctuation)
        username += special_char  

    if length and len(username) > length:
        username = username[:length]  

    return username

def save_usernames_to_file(usernames, folder_path, filename="usernames.txt"):
   
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    file_path = os.path.join(folder_path, filename)
    
    with open(file_path, "w") as file:
        file.write("\n".join(usernames))
    print(f"Usernames saved to {file_path}")

def main():
    print("Welcome to the Random Username Generator!")
    usernames = []

    adjectives, nouns = load_data('adjective_noun_dataset.csv')
    
    while True:
        try:
            include_numbers = input("Include numbers in usernames? (yes/no): ").strip().lower() == "yes"
            include_specials = input("Include special characters in usernames? (yes/no): ").strip().lower() == "yes"
            length = input("Set a maximum length for usernames (or press Enter to skip): ").strip()
            length = int(length) if length.isdigit() else None

            num_usernames = int(input("How many usernames would you like to generate? "))
        except ValueError:
            print("Invalid input. Please try again.")
            continue

        for _ in range(num_usernames):
            usernames.append(generate_username(include_numbers, include_specials, length, adjectives, nouns))

        print("\nGenerated Usernames:")
        print("\n".join(usernames))

        save_folder = 'PROJECT/pro1' 
        
        save_usernames_to_file(usernames, save_folder)

        another_round = input("\nGenerate more usernames? (yes/no): ").strip().lower()
        if another_round != "yes":
            print("Thank you for using the Random Username Generator!")
            break

if __name__ == "__main__":
    main()
