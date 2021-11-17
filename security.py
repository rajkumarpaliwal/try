# from werkzeug.security import safe_str_cmp
# from user import User

# users = [
#     User(1, 'user1', 'abcxyz'),
   
# ]

# username_maping = {u.username: u for u in users}
# userid_maping = {u.id: u for u in users}

# def authenticate(username, password):
#     user = username_maping.get(username, None)
#     if user and safe_str_cmp(user.password, password):
#         return user

# def identity(payload):
#     user_id = payload['identity']
#     return userid_maping.get(user_id, None)


from werkzeug.security import safe_str_cmp
from user import User

def authenticate(username, password):
    user = User.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return User.find_by_id(user_id)