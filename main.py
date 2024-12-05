import sys

def main():
    # Check if sufficient arguments were provided
    if len(sys.argv) < 3:
        print("Usage: python main.py <script_argument1> <script_argument2>")
        sys.exit(1)

    # Get the arguments from the command line
    script_argument1 = sys.argv[1]  # First argument (after the script name)
    script_argument2 = sys.argv[2]  # Second argument

    # Print the arguments
    print(f"Script Argument 1: {script_argument1}")
    print(f"Script Argument 2: {script_argument2}")

if __name__ == "__main__":
    main()
