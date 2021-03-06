__author__ = 'shaurya'

import os
from abc import abstractmethod


class DatabaseTable(object):
    """"Abstract DB Model specifying the required methods """
    @abstractmethod
    def create_schema_query(self):
        pass

    @abstractmethod
    def empty_database_content(self):
        pass

    @abstractmethod
    def get_insert_query(self):
        pass

    @abstractmethod
    def get_update_query(self):
        pass



#Should not be like this. Table & DB is one and the same table here.
#Should be a DB Table which should have a has-a relationship of multiple tables.
#Need to rewrite. Should work in this context as there is only one table.
class MessageTable(DatabaseTable):
    """DB Model to specify the message table in DB"""
    def __init__(self,dbname,path):
        if dbname[-3:]!=".db":
            dbname += ".db"
        self.dbname = dbname
        self.path = os.path.join(path,dbname)

        self._createquery = """
            CREATE TABLE MESSAGES (
                username    TEXT,
                message    TEXT,
                created    TEXT,
                tweet_id INTEGER
            )
        """

        self._insert_query = """
            INSERT INTO MESSAGES(username,message,created,tweet_id)
             VALUES (?,?,?,?)"""

        self._drop_all_rows = """
            DELETE FROM MESSAGES
        """
        
        self._count_rows = "SELECT count(*) from MESSAGES"
        
        self._get_limited_start = "SELECT * FROM MESSAGES LIMIT 100 OFFSET ?"
        
        
        self._get_all_rows = "SELECT * FROM MESSAGES"

        self._get_limited_rows = "SELECT * FROM MESSAGES LIMIT 1000"

    def create_schema_query(self):
        return self._createquery

    def empty_database_query(self):
        return self._drop_all_rows

    def get_insert_query(self):
        return self._insert_query

    def get_get_query(self):
        return self._get_all_rows

    def get_limited_get_query(self):
        return self._get_limited_rows
        
    def get_count(self):
        return self._count_rows
        
    def get_limited_start(self):
        return self._get_limited_start

    def get_db_path(self):
        return self.path
