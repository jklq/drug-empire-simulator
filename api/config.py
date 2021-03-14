from datetime import timedelta

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///../database.db'
JWT_SECRET_KEY="1akljsdfjklsdfjhasdkljfhjasdkfjlsdahfkjlsad"
JWT_ACCESS_TOKEN_EXPIRES=timedelta(days=3)
CORS_SUPPORTS_CREDENTIALS=True
