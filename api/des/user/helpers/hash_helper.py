import bcrypt

salt = bcrypt.gensalt()

def hash_password(plaintext):
    hashed_password = bcrypt.hashpw(plaintext,salt)
    return hashed_password

def hash_compare(plaintext, hashed):
    return bcrypt.checkpw(plaintext, hashed)
