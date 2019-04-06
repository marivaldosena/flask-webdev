import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Config:
    SECRET_KEY = (
        os.environ.get("SECRET_KEY")
        or "f2d6b10519fce5dd69f04c02db99e4eb7d434968a0a48512a767690551c0c55d"
    )
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DEV_DATABASE_URL"
    ) or "sqlite:///{}".format(os.path.join(BASE_DIR, "db.sqlite"))
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "TEST_DATABASE_URL"
    ) or "sqlite:///{}".format(os.path.join(BASE_DIR, "testing.db"))


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("DATABASE_URL") or "postgresql://usuario:senha@hostname/database"
    )

    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    # 'mysql://usuario:senha@hostname/database'


def get_config(config):
    if config.lower() == "dev" or config.lower() == "development":
        return DevConfig
    elif config.lower() == "test" or config.lower() == "testing":
        return TestingConfig
    elif config.lower() == "prod" or config.lower() == "production":
        return ProdConfig
    else:
        return DevConfig
