import os
config_path = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL","sqlite:///" + os.path.join(config_path, "twittor,db"))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TWEET_PER_PAGE = 4
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER', 'ljing1027@gmail.com')
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = os.environ.get('MAIL_PORT', 587)
    MAIL_USE_TLS = True
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 1)
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', 'ljing1027@gmail.com')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', 'lijing951027.')
    MAIL_SUBJECT_RESET_PASSWORD = '[Twittor] Please Reset Your Password'