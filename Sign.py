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
    
# Load the contents of the file to be signed
with open('Sample_PDF.pdf', 'rb') as pdf_file:
    pdf_contents = pdf_file.read()


# Sign the PDF contents
signature = base64.b64encode(
    private_key.sign(
        pdf_contents,
        # Use PSS padding with MGF1 and SHA-256 hash function
        padding.PSS(
            mgf = padding.MGF1(hashes.SHA256()),
            salt_length = padding.PSS.MAX_LENGTH,
        ),
        hashes.SHA256(),
    )
)

# Write the signature to a file
with open('signature.sig', 'wb') as signature_file:
    signature_file.write(signature)