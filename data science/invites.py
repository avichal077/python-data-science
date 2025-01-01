import requests
import time

url = "https://www.clubhouseapi.com/api/grant_social_club_invites"

token = "6b4eff3ce9b84794b37277720b2e7e6f0e4e0ce4"  # Placeholder for your token, replace it with the actual token
headers = {
    'CH-Languages': 'en-US',
    'CH-Locale': 'en_US',
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate',
    'CH-AppBuild': '588',
    'CH-AppVersion': '1.0.10',
    'CH-UserID': '667493545',
    'User-Agent': 'clubhouse/588 (iPhone; iOS 15; Scale/2.00)',
    'Connection': 'close',
    'Content-Type': 'application/json; charset=utf-8',
    "Authorization": f"Token {token}"
}
user_id = 1112441201# User ID to grant invites to
invites_to_grant = 100  # Number of invites to grant in each batch
payload = {
    "social_club_id": 996805112,
    "user_id": user_id,
    "num_invites": invites_to_grant  # Include the number of invites to grant
}

while True:
    for _ in range(invites_to_grant):
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            response_json = response.json()
            if response_json.get("success"):
                print(f"Invitation granted successfully to user {user_id}.")
                time.sleep(4)  # Wait for 5 seconds after a successful invite
            else:
                print(f"Invitation granting to user {user_id} was successful, but 'success' is not True in the response.")
                print("Response JSON:", response_json)
        elif response.status_code == 429:# high usuage 
            print(f"Rate limit exceeded. Waiting for a while before making the next request.")
            time.sleep(1)  # Wait for a minute before retrying
        else:
            print(f"Invitation granting to user {user_id} failed with status code:", response.status_code)
            print("Response content:", response.text)
    print(f"Batch of {invites_to_grant} invitations processed. Waiting for a while before starting a new batch.")
    time.sleep(4)  # Wait for a minute before starting a new batch
