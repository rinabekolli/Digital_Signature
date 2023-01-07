# Import necessary modules from the cryptography library
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

# Generate a 4096-bit RSA private key with a public exponent of 65537
rsa_private_key = rsa.generate_private_key(
    public_exponent = 65537,
    key_size = 4096,
    backend = default_backend(),
)


# Save the private key to a file in PEM format
with open('private.key', 'wb') as key_file:
    # Write the private key to the file in PEM format
    # with no encryption
    key_file.write(
        rsa_private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption(),
        )
    )
    
    
    # Save the public key to a file in PEM format
with open('public.pem', 'wb') as key_file:
    # Write the public key to the file in PEM format
    key_file.write(
        rsa_private_key.public_key().public_bytes(
            encoding = serialization.Encoding.PEM,
            format = serialization.PublicFormat.SubjectPublicKeyInfo,
        )
    )
    