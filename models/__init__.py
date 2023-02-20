#!/usr/bin/python3
"""Creates a unique storage instance for your application"""
import os


type_storage = os.getenv('HBNB_TYPE_STORAGE')


if type_storage == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
