from datetime import datetime


def generate_profile(birth):

    if 0 <= birth <= 12:
        return "Child"
    elif 13 <= birth <= 19:
        return "Teenager"
    elif birth >= 20:
        return "Adult"
    
    return 'Error'


user_name = input("Enter your full name?: ")
birth_year_str = input("Enter your birth year?: ")
birth_year = int(birth_year_str)
current_age =  datetime.now().year - birth_year
hobbies = list()

while (True):
    hobby = input("Enter a favorite hobby: or type 'stop' to finish: ")
    if hobby.lower() == "stop":
        break
    
    hobbies.append(hobby)

life_stage = generate_profile(current_age)

user_profile = {
    "Name": user_name,
    "Age": current_age,
    "Life Stage": life_stage,
    "Favorite Hobbies": hobbies
}

print("---\nProfile Summary:")
print(f"Name:  {user_profile.get('Name')}")
print(f"Age: {user_profile.get('Age')}")
print(f"Life stage: {user_profile.get('Life Stage')}")


if len(hobbies) > 0:
    print(f"Favorite Hobbies({len(hobbies)}): ")
    [print(f"- {hobby}") for hobby in user_profile.get('Favorite Hobbies')]
else:
    print("You didn't mention any hobbies.")
    
print("---")