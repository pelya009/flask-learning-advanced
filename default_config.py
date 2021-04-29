import os

DEBUG = True
SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///data.db")
SQLALCHEMY_TRACK_MODIFICATIONS = False
PROPAGATE_EXCEPTIONS = True
JWT_SECRET_KEY = os.environ.get("APP_SECRET_KEY")
UPLOADED_IMAGES_DEST = os.path.join("static", "images")
JWT_BLACKLIST_ENABLED = True
JWT_BLACKLIST_TOKEN_CHECKS = ["access", "refresh"]
