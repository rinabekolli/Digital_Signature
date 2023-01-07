
# RSA Key Generation and Signature Verification

This repository contains Python code for generating RSA keys and signing/verifying PDF files using the private/public key pair.


## Requirements

 - Python 3
 - cryptography module

## Generating RSA Keys

To generate an RSA key pair, run the Key_Generation.py script. It will generate a 4096-bit RSA private key with a public exponent of 65537 and save it to a file called private.key in PEM format. The public key will be saved to a file called public.pem in PEM format.
## Signing a File
To sign a file using the private key, run the sign.py script. It will read the contents of the file to be signed (e.g. Sample_PDF.pdf) and the private key from the private.key file. It will then write the signature to a file called signature.sig in base64-encoded format.
## Signing a File
To sign a file using the private key, run the sign.py script. It will read the contents of the file to be signed (e.g. Sample_PDF.pdf) and the private key from the private.key file. It will then write the signature to a file called signature.sig in base64-encoded format.
## Verifying the Signature
To verify the signature of a file, run the verify.py script. It will read the contents of the file (e.g. Sample_PDF.pdf) and the signature from the signature.sig file. It will then use the public key from the public.pem file to verify the signature. If the verification is successful, it will print a success message. If it fails, it will print an error message.
## Notes
- The key_generation.py, sign.py, and verify.py scripts are independent of each other and can be used separately.
- The sign.py and verify.py scripts are currently hardcoded to use the Sample_PDF.pdf file and the private.key/public.pem key pair. You can modify the code to use different files and/or keys as needed.