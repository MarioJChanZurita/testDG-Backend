class Config():
    MONGO_URI = 'mongodb+srv://dealergeek:dealergeek@cluster0.6gg8a.mongodb.net/test'


class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'development': DevelopmentConfig,
    'default': Config
}
