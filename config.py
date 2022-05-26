class Config(object):
    DEBUG = False
    TESTING = False
    INIT_FIRST = False
    SECRET_KEY = "xblocks2022"
    SECRET_KEY_REFRESH = "xblocks2022_reload"
    USER_URL = "http://localhost:5002"
    TOKEN_URL = "http://localhost:5003"
    
class Development(Config):
    DEBUG = True
    ENV_VALUE = "Development"
    INIT_FIRST = True
    SECRET_KEY = "xblocks2022"
    SECRET_KEY_REFRESH = "xblocks2022_reload"
    USER_URL = "http://localhost:5002"
    TOKEN_URL = "http://localhost:5003"
class Testing(Config):
    TESTING = True
    DEBUG = True
    INIT_FIRST = False
    SECRET_KEY = "xblocks2022"
    SECRET_KEY_REFRESH = "xblocks2022_reload"
    USER_URL = "http://user:5002"
    TOKEN_URL = "http://token:5003"
class Production(Config):
    DEBUG = False
    INIT_FIRST = False
    T_REFRESH = "refresh"
    SECRET_KEY = "xblocks2022"
    SECRET_KEY_REFRESH = "xblocks2022_reload"
    USER_URL = "http://user:5002"
    TOKEN_URL = "http://token:5003"