import pandas as pd
import sqlite3 as sql


class DataBase:
    def __init__(self):
        self.__db = 0

    def connect_to_database(self):
        self.__db = sql.connect('recommedation_db.db')

    def close_database(self):
        self.__db.close()

    def create_table(self):
        self.__db.execute('''CREATE TABLE IF NOT EXISTS author
                        (    ID INTEGER not null
                             primary key autoincrement,
                             name_of_author TEXT not null,
                             views_of_author INTEGER not null
                        )''')

        self.__db.execute('''CREATE TABLE IF NOT EXISTS publisher
                          (ID INTEGER not null
                             primary key autoincrement, 
                          name_of_publisher TEXT NOT NULL,
                          views_of_publisher INTEGER NOT NULL
                          )''')

        self.__db.execute('''CREATE TABLE IF NOT EXISTS affilname
                                (ID INTEGER not null
                                  primary key autoincrement,
                                 name_of_affilname TEXT NOT NULL,
                                 views_of_affilname INTEGER NOT NULL
                             )''')

        self.__db.execute('''CREATE TABLE IF NOT EXISTS affiliation_city
                                (ID INTEGER not null
                                  primary key autoincrement, 
                                 name_of_affiliation_city TEXT NOT NULL,
                                 views_of_affiliation_city INTEGER NOT NULL
                             )''')

        self.__db.execute('''CREATE TABLE IF NOT EXISTS affiliation_country
                                (ID INTEGER not null
                                  primary key autoincrement, 
                                 name_of_affiliation_country TEXT NOT NULL,
                                 views_of_affiliation_country INTEGER NOT NULL
                             )''')

    def insert_metadata_in_database(self, meta_data):
        self.connect_to_database()

        self.insert_data_by_column_name("author", meta_data.name_of_author)
        self.insert_data_by_column_name("publisher", meta_data.name_of_publisher)
        self.insert_data_by_column_name("affilname", meta_data.name_of_affilname)
        self.insert_data_by_column_name("affiliation_country", meta_data.name_of_affiliation_city)
        self.insert_data_by_column_name("affiliation_country", meta_data.name_of_affiliation_country)

        self.close_database()

    def get_dataframe_by_colums(self, cloumn_name):
        strin = "select views_of_" + cloumn_name + ",name_of_" + cloumn_name + " from " + cloumn_name

        df = pd.read_sql_query(strin, self.__db)
        return df

    def insert_data_by_column_name(self, column_name, data):

        try:
            read_query = "SELECT views_of_" + column_name + " from " + column_name + " where " \
                                                                                     "name_of_" + column_name + " LIKE '" + data + "';"

            results = self.__db.execute(read_query)

            number_of_rows = 0
            temp1 = 0

            for temp in results:
                temp1 = temp[0]
                number_of_rows += 1

            if number_of_rows == 0:
                insert_querty = "INSERT INTO " + column_name + "(name_of_" + column_name + ",views_of_" + column_name + "" \
                                                                                                                        ") VALUES (?,?)"
                self.__db.execute(insert_querty, (data, 1))
                self.__db.commit()

            else:
                update_query = "UPDATE " + column_name + " SET views_of_" + column_name + "" \
                                                                                          "=? where name_of_" + column_name + " LIKE ?"
                self.__db.execute(update_query,
                                  (temp1 + 1, data))

                self.__db.commit()
        except:
            print("something wrong in " + column_name)
