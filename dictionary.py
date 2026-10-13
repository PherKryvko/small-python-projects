players = {
    "Alex": 85,
    "Sam": 90,
    "Jordan": 78
}

# 1. Print Sam's rating
print(players.get("Sam"))

# 2. Add a player called Casey with a rating of 82
players["Casey"] = 82

# 3. Update Alex's rating to 88
players["Alex"] = 88

print(players)

# 4. Safely retrieve Taylor's rating,
#    returning "Not found" if absent

if "Taylor" in players:
    print(players["Taylor"])
else:
    print("Not found")

# 5. Print every player's name and rating

for key, value in players.items():
    print(f"{key} - {value}")



"""
Create two players, each with rating, pace and shooting.
[ ] Print Alex's pace.
[ ] Change Sam's shooting to 96.
[ ] Add a player called Casey with rating 82, pace 87 and shooting 79.
[ ] Loop through every player and print their name and overall rating.
[ ] Safely handle a lookup for a player called Taylor who does not exist.
"""

dictionary = {
    "Alex": {
        "Rating": 10,
        "Shooting": 10,
        "Pace": 30
    },
    "Sam": {
        "Rating": 40,
        "Shooting": 60,
        "Pace": 43
    }
}

print(dictionary["Alex"]["Pace"])

dictionary["Sam"]["Shooting"] = 96

dictionary["Casey"] = {
    "Rating": 82,
    "Pace": 87,
    "Shooting": 79
}

for key, value in dictionary.items():
    print(f"{key} - {value['Rating']}")


if "Taylor" in dictionary:
    print("Yes")
else:
    print("NO")