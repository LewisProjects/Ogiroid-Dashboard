import os
from dotenv import load_dotenv
from zenora import APIClient

load_dotenv()
client = APIClient(os.environ.get("TOKEN"), client_secret=os.environ.get("CLIENT_SECRET"))


def get_access_token(code, redirect_uri):
    access_token = client.oauth.get_access_token(code, redirect_uri).access_token

    return access_token


def get_user_client(access_token):
    user = APIClient(access_token, bearer=True).users.get_current_user()

    return str(user)