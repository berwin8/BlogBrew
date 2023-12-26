# run.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import create_app, db  # 确保从你的 app 包中导入 db

app = create_app()
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run()
