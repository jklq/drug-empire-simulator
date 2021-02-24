from setuptools import find_packages, setup

setup(
    name='Drug Empire Simulator',
    version='0.1.0',
    install_requires=[
        'flask',
        'cerberus',
        'bcrypt',
        'python-dotenv',
        'Flask-SQLAlchemy',
        'Flask-Migrate',
        'psycopg2',
        'Flask-JWT-Extended',
        'Flask-Marshmallow',
        'flask-classful'
        'flask-cors'
    ],
    extras_require={
        'dev': [
            'flask-debugtoolbar',
            'neovim',
            'pytest',
            'pytest-cov'
        ],
    },
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            ''
        ]
    }
)
