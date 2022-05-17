class Config(object):
    DEBUG = False
    TESTING = False
    INIT_FIRST = False
    SECRET_KEY = "xblocks2022"
    SECRET_KEY_REFRESH = "xblocks2022_reload"
    
class Development(Config):
    DEBUG = True
    ENV_VALUE = "Development"
    INIT_FIRST = True
    SECRET_KEY = "xblocks2022"
    SECRET_KEY_REFRESH = "xblocks2022_reload"

class Testing(Config):
    TESTING = True
    DEBUG = True
    INIT_FIRST = False
    SECRET_KEY = "xblocks2022"
    SECRET_KEY_REFRESH = "xblocks2022_reload"
class Production(Config):
    DEBUG = False
    INIT_FIRST = False
    T_REFRESH = "refresh"
    SECRET_KEY = "xblocks2022"
    SECRET_KEY_REFRESH = "xblocks2022_reload"