import hashlib

def hash_password(password):
    # Nous selectionons l'algorithme de hashage
    sha256_hash = hashlib.new("SHA256")
    # Encode nous servira transformer le UNICODE en en chaine d'octets UTF-8
    # Update créer le hashage
    sha256_hash.update(password.encode())
    return sha256_hash.hexdigest()
    