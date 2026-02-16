# Libraries
from cryptography.hazmat.primitives.asymmetric import rsa
from datetime import datetime, timedelta

# Valid Key Generation
valid_key = rsa.generate_private_key(
    public_exponent = 65537,
    key_size = 2048,
)

# Expired Key Generation
expired_key = rsa.generate_private_key(
    public_exponent = 65537,
    key_size = 2048,
)

# Valid Key Information
validKey = {
    "kid" : "abc123",
    "private_key" : valid_key,
    "public_key" : valid_key.public_key(),
    "expiresAt" : datetime.now() + timedelta(minutes = 1)
}

# Expired Key Information
expiredKey = {
    "kid" : "abc124",
    "private_key" : expired_key,
    "public_key" : expired_key.public_key(),
    "expiresAt" : datetime.now() - timedelta(minutes = 1)
}

# Keys List
keys = [validKey, expiredKey]