from datetime import timedelta

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///../test.db'
JWT_SECRET_KEY="1akljsdfjklsdfjhasdkljfhjasdkfjlsdahfkjlsad"
JWT_ACCESS_TOKEN_EXPIRES=timedelta(days=3)
