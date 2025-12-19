import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-change-in-prod")
    # MySQL connection using pymysql
    DB_USER = os.environ.get("DB_USER", "root")
    DB_PASS = os.environ.get("DB_PASS", "")   # default XAMPP = empty
    DB_HOST = os.environ.get("DB_HOST", "localhost")
    DB_NAME = os.environ.get("DB_NAME", "supportdesk")

    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False




#  EXISTING CONFIG upar hoga (DB, SECRET_KEY, etc)

# ================= EMAIL (ADD ONLY) =================
MAIL_SERVER = 'smtp.office365.com'
MAIL_PORT = 587
MAIL_USE_TLS = True

ADMIN_EMAIL = 'itva@vihanggroup.com'
ADMIN_EMAIL_PASSWORD = 'P@ss0rd@2024'

