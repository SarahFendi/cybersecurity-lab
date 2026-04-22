import bcrypt

password = b"securepassword"

hashed = bcrypt.hashpw(password, bcrypt.gensalt())

print("Hashed:", hashed)

# verify
print(bcrypt.checkpw(password, hashed))
