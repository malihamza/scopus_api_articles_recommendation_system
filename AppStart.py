from DAL.DataBase import DataBase


class AppStart:
    @staticmethod
    def start_application():
        db = DataBase()
        db.connect_to_database()
        db.create_table()