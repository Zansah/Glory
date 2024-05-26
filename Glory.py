import time

title = None
Level = 0

def welcome():
    print("[Welcome player to the game Glory.]")
    print('Greetings! I am Maya, your helpful fairy virtual assistant. I will be introducing you to the four main categories and the 3 main jobs that come with them.')
    print("Please choose the category that suits you the most.")

def roles():
    print("[Warrior]\n-Shield Warrior\n-Guardian Knight\n-Berserker")
    time.sleep(2)
    print("[Weapon Specialist]\n-Swordsman\n-Assassin\n-Ranger")
    time.sleep(2)
    print("[Healer]\n-Cleric\n-Druid\n-Oracle")
    time.sleep(2)
    print("[Mage]\n-Elementalist\n-Summoner\n-Cursemancer")
    select = input("Select: ").lower()
    return select

welcome()
role = roles()

if role == "warrior":
    print("You have selected Warrior.")
    sel = input("Select one of the jobs that come with it: ").lower()
    if sel == "shield warrior":
        pass
    elif sel == "guardian knight":
        pass
    elif sel == "berserker":
        pass
elif role == "weapon specialist":
    print("You have selected Weapon Specialist.")
    sel = input("Select one of the jobs that come with it: ").lower()
    if sel == "swordsman":
        pass
    elif sel == "assassin":
        pass
    elif sel == "ranger":
        pass
elif role == "healer":
    print("You have selected Healer.")
    sel = input("Select one of the jobs that come with it: ").lower()
    if sel == "cleric":
        pass
    elif sel == "druid":
        pass
    elif sel == "oracle":
        pass
elif role == "mage":
    print("You have selected Mage.")
    sel = input("Select one of the jobs that come with it: ").lower()
    if sel == "elementalist":
        pass
    elif sel == "summoner":
        pass
    elif sel == "cursemancer":
        pass
else:
    print("There has been an error. You haven't selected a class.")

name = input("Job selection complete. Please designate a name for your character: ")

def city():
    locations = {
        "america": "Federation",
        "asia": "Dragon Kingdom",
        "antartica": "Wasteland",
        "europe": "Demacia",
        "south america": "Amazon Empire",
        "australia": "Lucky Kingdom"
    }
    continent = input("Enter the continent you currently live on: ").lower()
    if continent in locations:
        print(f"You are in {locations[continent]}.")
        return locations[continent]
    else:
        print("Invalid continent entered.")

home = city()

def panel(User, Kingdom, Title, Job, Level):
    print(f"Character: {User} (Human)")
    print(f"Affiliated Kingdom: {Kingdom}")
    print(f"Title: {Title}")
    print(f"Job: {Job}")
    print(f"Level: {Level}")

panel(name, home, title, sel, Level)
