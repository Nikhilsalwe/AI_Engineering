import requests

def get_github_info(username):
    try:
        url = f"https://api.github.com/users/{username}"
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        
        data = response.json()
        print(f"Name: {data.get('name', 'N/A')}")
        print(f"Company: {data.get('company', 'N/A')}")
        print(f"Public repos: {data.get('public_repos', 0)}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except KeyError as e:
        print(f"Error accessing data: {e}")

if __name__ == "__main__":
    username = "NikhilSalwe"
    get_github_info(username)