from des.user.helpers.hash_helper import hash_password, hash_compare

plaintext_pass = "thisisapassword".encode('utf-8')
hashed_pass = "$2y$12$3wP6b3aIxTnGej7Y7G6CauzOAGcsmIeeOFoM13/vWzQ/CeXqnpIqm".encode('utf-8')

def test_hash_compare():
    do_passwords_match = hash_compare(plaintext_pass, hashed_pass)
    assert do_passwords_match == True
    
def test_hash_password():
    generated_hashed_pass = hash_password(plaintext_pass)
    assert generated_hashed_pass != plaintext_pass
    assert hash_compare(plaintext_pass, generated_hashed_pass) == True
