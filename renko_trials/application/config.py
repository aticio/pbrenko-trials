import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Base configuration"""


class ProductionConfig(object):
    """Production configuration"""


class DevelopmentConfig(object):
    """Development configuration"""


class TestingConfig(object):
    """Testing configuration"""

    TESTING = True
