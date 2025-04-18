import pyodbc
from util.DBPropertyUtil import DBPropertyUtil

class DBConnUtil:
    @staticmethod
    def get_db_connection():

        db_props = DBPropertyUtil.get_db_properties()
        conn = pyodbc.connect(
            f'DRIVER={{SQL Server}};SERVER={db_props["server"]};'
            f'DATABASE={db_props["database"]};'
            f'Trusted_Connection=yes;'
        )
        return conn
