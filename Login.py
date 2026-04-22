import hashlib

# Function to hash password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Store user (in real life this would be a database)
stored_username = "admin"
stored_password_hash = hash_password("Secure123")

# Login system
print("=== Login System ===")

username = input("Enter username: ")
password = input("Enter password: ")

if username == stored_username and hash_password(password) == stored_password_hash:
    print("Login successful ✅")
else:
    print("Login failed ❌")
