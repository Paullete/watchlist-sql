import os

class Config:
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key=aabb0c7ca8b510be8e9e03a4e8ffd9aa'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://dell:Dell@localhost/watchlist'


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}