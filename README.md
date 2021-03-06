# Cryptographic utility package

An easy and simplified cryptographic utility package (fernet, RSA, hashes...) with some
common encryption stuff already programmed (very simple and with common secure parameters by default). 
It uses the 'cryptography' module

### Installation
```
pip install crypt-utilities
```
### Modules 

#### Symmetric
```
def encrypt ...
def encrypt_file ...
def decrypt_file ...
```

#### Hashes
```
def derive(data:bytes, salt:bytes, length:int=32, iterations=400000) -> bytes:...
```

#### Asymmetric
```
def rsa_encrypt (...
def generate_rsa_key_pairs (...
def generate_private_key (...
def serialize_pem_public_key (...
def load_pem_private_key (...
```
### Usage Example

```
# Encrypt with RSA (asymmetric)
# -- John
secret_msg = "Very secret msg to send"
public_key = load_pem_public_key(file_path="./public_key")
encrypted:bytes = rsa_encrypt(secret_msg.encode(), public_key)
...
# Decrypt with RSA (asymmetric)
# -- Michael
private_key_path = str(input(" -> Introduce your private key file path: "))
password = str(input(" -> Introduce the private key password (blank if None was used): "))
if password == "":
    password = None
try:
    private_key = load_pem_private_key(file_path=private_key_path, password=password)
except :
    print("[!] Wrong Password"); exit(1)
secret_msg_sent_by_john = rsa_decrypt(encrypted, private_key).decode()
```
