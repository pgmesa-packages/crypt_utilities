# Cryptographic utility package

An easy and simplified cryptographic utility package (fernet, RSA, hashes...) with some
common encryption stuff already programmed (very simple and with common secure parameters by default). 
It uses the 'cryptography' module

### Instalation
```pip install crypt-utilities```

### Usage Examples

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
