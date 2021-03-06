HOST = '127.0.0.1'
PORT = 5000
DEBUG = True
TESTING = True

DB_CONFIG_DICT = {
    'user': 'pgsqluser',
    'password': 'pgsqlpwd',
    'host': 'localhost',
    'port': 5432
}
DATABASE_NAME = 'MOSP'
SQLALCHEMY_DATABASE_URI = 'postgres://{user}:{password}@{host}:{port}/{name}'.format(name=DATABASE_NAME, **DB_CONFIG_DICT)
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = 'dev'
SECURITY_PASSWORD_SALT = 'dev'

UPLOAD_FOLDER = './mosp/web/public/pictures/'
ALLOWED_EXTENSIONS = set(['png'])

ADMIN_EMAIL = 'info@cases.lu'

LOG_PATH = './var/log/mosp.log'
LOG_LEVEL = 'info'

CSRF_ENABLED = True
# slow database query threshold (in seconds)
DATABASE_QUERY_TIMEOUT = 0.5

MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USE_TLS = False
MAIL_USE_SSL = False
MAIL_DEBUG = DEBUG
MAIL_USERNAME = None
MAIL_PASSWORD = None
MAIL_DEFAULT_SENDER = ADMIN_EMAIL
