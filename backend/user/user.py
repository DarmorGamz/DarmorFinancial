import os
import pymysql
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from dotenv import load_dotenv
load_dotenv()

class User():
    def __init__(self):
        pass

    def UserGsad(self, cmd):
        oUserDb = UserDb()

        match cmd:
            case 'Get':
                db = oUserDb.get_session()
                try:
                    # Attempt to add a user (this may raise a duplicate entry error if username/email exists)
                    new_user = UserTable(username="Darren", email="d@test.ca")
                    db.add(new_user)
                    db.commit()
                    db.refresh(new_user)
                    return {"message": "User added successfully", "user_id": new_user.id}
                
                # Catch duplicate entry error
                except IntegrityError as e:
                    db.rollback()  # Roll back the session to prevent issues
                    return {"error": "Duplicate entry: The username or email already exists"}

                # Catch other SQLAlchemy-related errors
                except SQLAlchemyError as e:
                    db.rollback()
                    return {"error": "A database error occurred", "details": str(e)}

                # Ensure the session is closed
                finally:
                    db.close()

            case 'Set':
                pass
            case 'Add':
                pass
            case 'Del':
                pass
            case _:
                # Set Response
                return False
            
        # Set Response
        return False

Base = declarative_base()
class UserDb():
    DB_HOST = os.getenv("DB_HOST")
    DB_USER = os.getenv("DB_USER")
    DB_PWD = os.getenv("DB_PWD")
    DB_NAME = os.getenv("DB_NAME")
    DB_PORT = os.getenv("DB_PORT", "3306")

    def __init__(self):
        connection = pymysql.connect(host=self.DB_HOST, user=self.DB_USER, password=self.DB_PWD)

        with connection.cursor() as cursor:
            # Create the database if it does not exist
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.DB_NAME}")
        connection.close()

        self.DATABASE_URL = f"mysql+pymysql://{self.DB_USER}:{self.DB_PWD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        print(f"Connecting to DB at {self.DATABASE_URL}")
        self.engine = create_engine(self.DATABASE_URL)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        Base.metadata.create_all(bind=self.engine, checkfirst=True)  # Creates tables if they don't exist
        
    def get_session(self):
        return self.SessionLocal()

    def __del__(self):
        self.engine.dispose()

class UserTable(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=False, nullable=False)