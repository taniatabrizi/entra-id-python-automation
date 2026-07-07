import requests

def get_users(access_token):
    url = "https://graph.microsoft.com/v1.0/users"

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)

    response.raise_for_status()

    return response.json()


if __name__ == "__main__":
    print("Microsoft Graph IAM automation module")
