import os
import sys

def main():
    # Get the repository secret
    secret_key = os.getenv("SECRET_KEY")
    if not secret_key:
        print("Error: SECRET_KEY is not available!")
        sys.exit(1)

    # Check if sufficient arguments are provided
    if len(sys.argv) < 7:
        print("Usage: python main.py <script_argument1> <script_argument2> <script_argument3> <script_argument4> <email> <name>")
        sys.exit(1)

    # Get the arguments
    script_argument1 = sys.argv[1]
    script_argument2 = sys.argv[2]
    script_argument3 = sys.argv[3]
    script_argument4 = sys.argv[4]
    email = sys.argv[5]
    name = sys.argv[6]

    # Print the arguments (obfuscate sensitive info)
    print(f"Secret Key: {secret_key[:5]}****")  # Obfuscate for safety
    print(f"Capability: {script_argument1}")
    print(f"Days Back: {script_argument2}")
    print(f"PR Status: {script_argument3}")
    print(f"PR Date Type: {script_argument4}")
    print(f"User Email: {email}")
    print(f"User Name: {name}")

if __name__ == "__main__":
    main()
