import os
import sys

def main():
    # Get the repository secret
    secret_key = os.getenv("SECRET_KEY")
    if not secret_key:
        print("Error: SECRET_KEY is not available!")
        sys.exit(1)

    # Get the other arguments
    if len(sys.argv) < 5:
        print("Usage: python main.py <script_argument1> <script_argument2> <script_argument3> <script_argument4>")
        sys.exit(1)

    script_argument1 = sys.argv[1]
    script_argument2 = sys.argv[2]
    script_argument3 = sys.argv[3]
    script_argument4 = sys.argv[4]

    # Print the arguments and the secret (don't do this in production for secrets!)
    print(f"Secret Key: {secret_key[:5]}****")  # Obfuscate for safety
    print(f"Capability: {script_argument1}")
    print(f"Days Back: {script_argument2}")
    print(f"PR Status: {script_argument3}")
    print(f"PR Date Type: {script_argument4}")

if __name__ == "__main__":
    main()
