import base64
import cryptography.exceptions
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_public_key

# Load the public key
with open('public.pem', 'rb') as key_file:
    # Read the public key from the file
    public_key = load_pem_public_key(key_file.read())


# Load the contents of the PDF file and the signature
with open('Sample_PDF.pdf', 'rb') as pdf_file:
    pdf_contents = pdf_file.read()
with open('signature.sig', 'rb') as signature_file:
    # Read the signature from the file and decode it from base64
    signature_bytes = base64.b64decode(signature_file.read())