import random
import secrets
import string

# 1. Non-cryptographic operations using random (simulations, gaming, shuffling)
items = ["Task A", "Task B", "Task C", "Task D"]
random.shuffle(items)
print("Shuffled:", items)
print("Random pick:", random.choice(items))
print("Random sample without replacement:", random.sample(items, 2))

# 2. Cryptographically secure random tokens using secrets (CSRF, session tokens, OTPs)
csrf_token = secrets.token_hex(16)
url_safe_token = secrets.token_urlsafe(16)
otp_code = "".join([str(secrets.randbelow(10)) for _ in range(6)])

print("Secure CSRF token:", csrf_token)
print("URL-safe token:", url_safe_token)
print("6-digit secure OTP:", otp_code)

# 3. Generating strong passwords
alphabet = string.ascii_letters + string.digits + string.punctuation
password = "".join(secrets.choice(alphabet) for _ in range(16))
print("Generated strong password:", password)