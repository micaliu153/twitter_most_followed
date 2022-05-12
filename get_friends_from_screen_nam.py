import json
import requests

def get_user_friends_v1_by_screen_name(screen_name,bearer_token):
        
        trend_headers = {
            'Authorization': 'Bearer {}'.format(bearer_token)
        }
        url = "https://api.twitter.com/1.1/friends/list.json?cursor=-1&screen_name={}&skip_status=false&include_user_entities=true&count=100".format(
            screen_name)
        # print(url)

        i = 0
        while i < 5:
            i += 1
            try:
                response = requests.get(url, headers=trend_headers)
                return response.json()
            except requests.exceptions.RequestException as e:
                print(e)
        return None



if __name__ == "__main__":
    screen_name = 'elonmusk' 
    bearer_token = '' # your token
    user_tweets_json = get_user_friends_v1_by_screen_name(screen_name,bearer_token)
    print(json.dumps(user_tweets_json, indent=4, sort_keys=True))