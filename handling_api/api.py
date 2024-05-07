import requests

def fetch_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers?page=1&limit=10"
    response = requests.get(url)
    data = response.json()

    if data.get("success") and "data" in data:
        user_data = data["data"][0]  # Assuming you want the first user's data
        username = user_data.get("login", {}).get("username")
        country = user_data.get("location", {}).get("country")
        return username, country
    else:
        raise Exception("Failed to fetch user data")

def main():
    try:
        username, country = fetch_random_user()
        if username and country:
            print(f"Username: {username}\nCountry: {country}")
        else:
            print("User data is incomplete")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
