import requests

def check_username_availability(username):
    """Check if a GitHub username is available."""
    url = f"https://github.com/{username}"
    response = requests.get(url)
    
    # If the response status code is 404, the username is available
    if response.status_code == 404:
        return True
    elif response.status_code == 200:
        return False
    else:
        raise Exception(f"Unexpected response code: {response.status_code}")

def read_usernames_from_file(filename):
    """Read usernames from a file and return a list."""
    try:
        with open(filename, 'r') as file:
            usernames = [line.strip() for line in file if line.strip()]
        return usernames
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return []

def save_available_usernames_to_file(usernames, filename):
    """Save available usernames to a file."""
    try:
        with open(filename, 'w') as file:
            for username in usernames:
                file.write(f"{username}\n")
        print(f"Available usernames saved to '{filename}'.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

def main():
    input_file = 'usernames.txt'
    output_file = 'available_usernames.txt'
    
    usernames = read_usernames_from_file(input_file)
    available_usernames = []

    for username in usernames:
        try:
            if check_username_availability(username):
                available_usernames.append(username)
                print(f"Username '{username}' is available.")
            else:
                print(f"Username '{username}' is taken.")
        except Exception as e:
            print(f"Error checking username '{username}': {e}")

    save_available_usernames_to_file(available_usernames, output_file)

if __name__ == "__main__":
    main()
