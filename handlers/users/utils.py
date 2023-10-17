import os


def user_checker(chat_id: int):
    if not os.path.exists('users.txt'):
        with open('users.txt', 'x') as create_file:
            pass

    with open('users.txt', 'r') as read_file:
        users_data = read_file.readlines()
        for user_data in users_data:
            user_split = user_data.split(',')
            user_chat_id = user_split[1].strip()

            if int(user_chat_id) == chat_id:
                return user_split
    return False


def write_user(data):
    full_name = data['full_name']
    phone_number = data["phone_number"]
    chat_id = data["chat_id"]
    gender_name = data["gender"]
    location = data["location"]

    try:
        with open('users.txt', 'a') as write_file:
            write_file.write(f"{full_name}, {chat_id}, {phone_number}, {gender_name}, {location}")
        return True
    except BaseException as exc:
        print(exc)
        return False


def phone_validator(user_phone: str):
    if len(user_phone) != 9:
        return False
    else:
        try:
            return str(int(user_phone))
        except Exception as exc:
            print(exc)
            return False