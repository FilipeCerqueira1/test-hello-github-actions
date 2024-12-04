import os

def main():
    name = os.getenv("USER_NAME")
    email = os.getenv("USER_EMAIL")
    print(f"Name: {name}")
    print(f"Email: {email}")
    # Add your logic here

if __name__ == "__main__":
    main()