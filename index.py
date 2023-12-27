import os
from urllib import parse

from dotenv import load_dotenv
from flask import Flask, Response, redirect, render_template, request
from flask_migrate import Migrate
from sqlalchemy.ext.automap import automap_base

from models import *

from login import get_access_token, get_user_client
from zenora import APIClient
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user

from models import db

app = Flask(__name__)

load_dotenv()
TOKEN = os.environ.get("TOKEN")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
CLIENT_ID = os.environ.get("CLIENT_ID")
REDIRECT_URI = os.environ.get("REDIRECT_URI")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("POSTGRES_DASHBOARD_CONNECTION_STRING")
app.config["SQLALCHEMY_BINDS"] = {
    "ogiroid": os.environ.get("POSTGRES_OGIROID_CONNECTION_STRING"),
    "dashboard": os.environ.get("POSTGRES_DASHBOARD_CONNECTION_STRING"),
}

OAUTH_URL = (
    f"https://discord.com/api/oauth2/authorize?client_id=1011297534334996502&redirect_uri={parse.quote(REDIRECT_URI)}&response_type=code&scope=identify%20email%20guilds")

login_manager = LoginManager(app)
login_manager.login_view = "signin"

client = APIClient(TOKEN, client_secret=CLIENT_SECRET)

migrate = Migrate(app, db)
db.init_app(app)
with app.app_context():
    Base = automap_base()
    Base.prepare(autoload_with=db.engines["ogiroid"])

Tag = Base.classes.tags
Warnings = Base.classes.warnings
TagRelation = Base.classes.tag_relations
Blacklist = Base.classes.blacklist
FlagQuiz = Base.classes.flag_quiz
Trivia = Base.classes.trivia
ReactionRole = Base.classes.reaction_roles
Level = Base.classes.levels
RoleReward = Base.classes.role_rewards
Birthday = Base.classes.birthday
Timezone = Base.classes.timezone
Config = Base.classes.config
Command = Base.classes.commands
TotalCommand = Base.classes.total_commands


@app.route("/")
def home() -> str:
    return render_template("index.html")


@app.route("/sign-in")
def signin() -> Response:
    """
    It will send user to oath site to set in config
    """
    return redirect(OAUTH_URL)


@app.route("/sign-out")
def signout() -> Response:
    logout_user()
    return redirect("/")


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/oauth/callback")
def login_callback():
    code = request.args['code']
    access_token = client.oauth.get_access_token(code, REDIRECT_URI).access_token
    bearer_client = APIClient(access_token, bearer=True)
    discord_user = bearer_client.users.get_current_user()
    guilds = bearer_client.users.get_my_guilds()

    joined = False
    for guild in guilds:
        if guild.id == 897666935708352582:
            joined = True
            break

    if not joined:
        return "You are not in the Coding with Lewis Server"

    user_db = User.query.get(int(discord_user.id))
    if not user_db:
        new_user = User(id=int(discord_user.id), username=discord_user.username, email=discord_user.email,
                        avatar_url=discord_user.avatar_url)
        db.session.add(new_user)
        db.session.commit()
        user_db = User.query.get(int(discord_user.id))

    login_user(user_db, remember=True)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=os.getenv("DEBUG"))
