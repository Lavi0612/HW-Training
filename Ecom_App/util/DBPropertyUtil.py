import configparser

class DBPropertyUtil:
    @staticmethod
    def get_db_properties():
        config = configparser.ConfigParser()
        config.read('resources/db.properties')
        return config['DATABASE']
