import json

def open_json():
    with open('passwords.json', 'r') as f:
            data = json.load(f)
    return data
    
def save_password(web, user_passwords):
    data = open_json()
    data[web] = user_passwords
    with open('passwords.json', 'w') as f:
        json.dump(data, f)