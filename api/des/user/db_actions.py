from ..common.database import db
from .models import User
from .helpers.hash_helper import hash_password

def user_exists(**user):
    if not 'username' in user:
        user_to_find = User.query.filter_by(email=user["email"]).first() 
    elif not 'email' in user:
        user_to_find = User.query.filter_by(username=user["username"]).first() 
    else:
        user_to_find = User.query.filter((User.username==user["username"])
                                         | (User.email==user['email'])).first()
    if user_to_find == None:
        return {'result': False, 'matching_user': None}
    else:
        return {'result': True, 'matching_user': user_to_find}

def create_user(**user):
    new_user = User(email=user['email'], 
                    username=user['username'], 
                    password=user['password'])
    
    user_already_exists = user_exists(**user)['result']
        
    if not user_already_exists:
        plaintext_pass = new_user.password
        new_user.password = hash_password(plaintext_pass)
        db.session.add(new_user)
        db.session.commit()
        return {'msg': 'User Created', 'status': 201}
    else:
        return {'msg': 'User Already Exists', 'status': 409}

def update_user_role(username, role, allowOverwrite=False):
    user_to_update_exist = user_exists(username=username)

    if not user_to_update_exist['result']:
        return {'msg': 'User not found', 'status': 404}
    else:
        user_to_update = user_to_update_exist['matching_user']

    if not allowOverwrite and user_to_update.role != None:
        return {"msg": 'Role already set', 'status': 409}

    if role != 'c' and role != 'b' and role != 'm':
        return {"msg": 'Invalid role', 'status': 422}

    # SOME ROLES ARE CURRENTLY NOT DEVELOPED
    if role == 'c' or role == 'm':
        return {"msg": 'Role currently not available', 'status': 403}
 
    user_to_update.role = role
    db.session.commit()
    return {'msg': 'Role set', 'status': 200}
