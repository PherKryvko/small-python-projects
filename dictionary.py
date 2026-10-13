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


"""
Add "Jordan" with a rating of 78, pace of 91 and shooting of 84.

Increase Alex's rating by 5.

Print the names of all players whose pace is greater than 85.

Safely print Morgan's rating, displaying "Player not found" if Morgan doesn't exist.
"""

dictionary["Jordan"] = {
    "Rating": 70,
    "Pace": 91,
    "Shooting": 84
}

dictionary["Alex"]["Rating"] = 5

for key, value in dictionary.items():
    if value["Pace"] > 85:
        print(f"{key}")

if dictionary.get("Morgan"):
    print(dictionary["Morgan"]["Rating"])
else:
    print("Player not found")



"""
LIST DICTIONARY

Print Sam's rating.
Add a new player, Casey, with a rating of 82.
Loop through the list and print the names of every player with a rating of 85 or higher.
"""


players = [
    {"Name": "Alex", "Rating": 88},
    {"Name": "Sam", "Rating": 90},
    {"Name": "Jordan", "Rating": 78}
]

# 1. Print Sam's rating
print(players[1]["Rating"])

# 2. Add Casey
players.append({"Name": "Casey", "Rating": 82})

# 3. Print players rated 85 or higher
for player in players:
    if player["Rating"] >= 85:
        print(player["Name"])