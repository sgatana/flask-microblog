import os


class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    SQLALCHMEY_DATABASE_URI = os.getenv('DATABASE_URL')
    DEBUG = True


class TestingConfig(Config):
    SQLALCHMEY_DATABASE_URI = os.getenv('TEST_DB_URL')
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    SQLALCHMEY_DATABASE_URI = os.getenv('DATABASE_URL')
    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}