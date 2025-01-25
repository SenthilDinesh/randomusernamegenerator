import csv
import random
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

with open('adjective_noun_dataset.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['adjective', 'noun']) 
    writer.writerows(random_pairs)  

print("CSV file 'adjective_noun_dataset.csv' generated successfully.")
