import os

def generate_secret_key(length=32):
    return os.urandom(length).hex()

if __name__ == '__main__':
    secret_key = generate_secret_key()
    print(secret_key)

