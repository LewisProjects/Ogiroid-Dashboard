from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.BigInteger, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    avatar_url = db.Column(db.String(200))
    developer = db.Column(db.Boolean, default=False)

#
#
# class Tag(db.Model):
#     __tablename__ = "tags"
#     tag_id = db.Column(db.String(80), primary_key=True)
#     content = db.Column(db.String(2000))
#     owner = db.Column(db.BigInteger)
#     created_at = db.Column(db.BigInteger)
#     views = db.Column(db.Integer)
#
#
# class TagRelation(db.Model):
#     __tablename__ = "tag_relations"
#     tag_id = db.Column(db.String(80), primary_key=True)
#     alias = db.Column(db.String(80), primary_key=True)
#
#
# class Blacklist(db.Model):
#     __tablename__ = "blacklist"
#     user_id = db.Column(db.BigInteger, primary_key=True)
#     reason = db.Column(db.String(2000))
#     bot = db.Column(db.Boolean)
#     tickets = db.Column(db.Boolean)
#     tags = db.Column(db.Boolean)
#     expires = db.Column(db.BigInteger)
#
#
# class FlagQuiz(db.Model):
#     __tablename__ = "flag_quiz"
#     user_id = db.Column(db.BigInteger, primary_key=True)
#     tries = db.Column(db.Integer)
#     correct = db.Column(db.Integer)
#     completed = db.Column(db.Integer)
#     guild_id = db.Column(db.BigInteger)
#
#
# class Trivia(db.Model):
#     __tablename__ = "trivia"
#     id = db.Column(db.BigInteger, primary_key=True)
#     correct = db.Column(db.Integer)
#     incorrect = db.Column(db.Integer)
#     streak = db.Column(db.Integer)
#     longest_streak = db.Column(db.Integer)
#
#
# class ReactionRole(db.Model):
#     __tablename__ = "reaction_roles"
#     message_id = db.Column(db.BigInteger, primary_key=True)
#     role_id = db.Column(db.BigInteger, primary_key=True)
#     emoji = db.Column(db.String(80))
#     roles_given = db.Column(db.Integer)
#
#
# class Warnings(db.Model):
#     __tablename__ = "warnings"
#     warning_id = db.Column(db.BigInteger, primary_key=True)
#     user_id = db.Column(db.BigInteger)
#     moderator_id = db.Column(db.BigInteger)
#     reason = db.Column(db.String(2000))
#     guild_id = db.Column(db.BigInteger)
#
#
# class Level(db.Model):
#     __tablename__ = "levels"
#     guild_id = db.Column(db.BigInteger, primary_key=True)
#     user_id = db.Column(db.BigInteger, primary_key=True)
#     level = db.Column(db.Integer)
#     xp = db.Column(db.Integer)
#
#
# class RoleReward(db.Model):
#     __tablename__ = "role_rewards"
#     guild_id = db.Column(db.BigInteger, primary_key=True)
#     role_id = db.Column(db.BigInteger, primary_key=True)
#     required_lvl = db.Column(db.Integer)
#
#
# class Birthday(db.Model):
#     __tablename__ = "birthday"
#     user_id = db.Column(db.BigInteger, primary_key=True)
#     birthday = db.Column(db.String(80))
#     birthday_last_changed = db.Column(db.BigInteger)
#
#
# class Timezone(db.Model):
#     __tablename__ = "timezone"
#     user_id = db.Column(db.BigInteger, primary_key=True)
#     timezone = db.Column(db.String(80))
#     timezone_last_changed = db.Column(db.BigInteger)
#
#
# class Config(db.Model):
#     __tablename__ = "config"
#     guild_id = db.Column(db.BigInteger, primary_key=True)
#     xp_boost = db.Column(db.Integer)
#     xp_boost_expiry = db.Column(db.BigInteger)
#     xp_boost_enabled = db.Column(db.Boolean)
#
#
# class Command(db.Model):
#     __tablename__ = "commands"
#     guild_id = db.Column(db.BigInteger, primary_key=True)
#     command = db.Column(db.String(80), primary_key=True)
#     command_used = db.Column(db.Integer)
#
#
# class TotalCommand(db.Model):
#     __tablename__ = "total_commands"
#     guild_id = db.Column(db.BigInteger, primary_key=True)
#     total_commands_used = db.Column(db.Integer)
