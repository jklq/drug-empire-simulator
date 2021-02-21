import bcrypt

salt = bcrypt.gensalt()

def hash_password(plaintext):
    return bcrypt.hashpw(plaintext,salt)

def hash_compare(plaintext, hashed):
    return bcrypt.checkpw(plaintext, hashed)
