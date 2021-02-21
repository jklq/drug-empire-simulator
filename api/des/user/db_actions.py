from ..common.database import db
from .models import User
from .helpers.hash_helper import hash_password

def user_exists(**user):
    if not 'username' in user:
        user_to_find = User.query.filter_by(email=user["email"]).first() 
    else:
        user_to_find = User.query.filter((User.username==user["username"])
                                         | (User.email==user['email'])).first()
    if user_to_find == None:
        return False, None
    else:
        return True, user_to_find

def create_user(user):
    new_user = User(email=user['email'], 
                    username=user['username'], 
                    password=user['password'])
    
    user_already_exists = user_exists(**user)[0]
        
    if not user_already_exists:
        plaintext_pass = new_user.password
        new_user.password = hash_password(plaintext_pass)
        db.session.add(new_user)
        db.session.commit()
        return "created", 201
    else:
        return "user already exists", 409


