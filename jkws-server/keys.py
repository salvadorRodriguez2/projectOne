# Libraries
from cryptography.hazmat.primitives.asymmetric import rsa

# Key Generation
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Key Information
keyToWorkWith = {
    "kid" : "something",
    "private_key" : private_key,
    "public_key" : "function that derives public from private",
    "expiresAt" : "something about the expiry"
}