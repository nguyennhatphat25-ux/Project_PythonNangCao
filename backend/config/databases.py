import os

class Config:
    # mysql+pymysql://<user>:<password>@<host>:<port>/<database>
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "SQLALCHEMY_DATABASE_URI",
        # nếu mật khẩu chứa '@', encode nó: '@' -> '%40'
        "mysql+pymysql://root:Phatxike2004%40@localhost:3306/db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False