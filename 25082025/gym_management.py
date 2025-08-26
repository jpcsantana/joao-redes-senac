import json

def format_object(name, age, height, active, grades):
    return {"name": name, "ageInNumber": age, "height": height, "active": active, "grades": grades}

def create_member(name, age, height, active, grades):
    data = format_object(name, age, height, active, grades)
    with open('gym_management.json', 'r') as file:
        print(json.load(file))
    return data

def calculate_grade_media_by_member_id(id):
    with open('gym_management.json', 'r') as file:
        members = json.load(file)
    member = 0
    for member in members:
        for key, value in member.items():
            if key=='id' and value == id:
                test = member
    if(member == 0):
        print('User not found.')
        return
    else:
        return sum(member['grades']) / len(member['grades'])

def return_only_active_members(members):
    return [member for member in members if members['active']]

def get_all_members():
    with open('gym_management.json', 'r') as file:
        print(json.load(file))

print(calculate_grade_media_by_member_id(0))