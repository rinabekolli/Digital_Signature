import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding

# Load the private key 
with open('private.key', 'rb') as key_file: 
    # Read the private key from the file
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password = None,
        backend = default_backend(),
    )