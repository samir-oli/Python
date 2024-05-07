import requests
def fetch_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers?page=1&limit=10"
    response = requests.get(url)
    data = response.json()


    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        # picture = user_data["picture"]["medium"]
        return username, country
    else:
        raise Exception("Faile to fetch user data")
    

def main():
        try:
            username, country = fetch_random_user()
            print(f"Username: {username} \n Country: {country} " )
        except Exception as e:
            print(str(e))





if __name__ == "__main__":
    main()    

