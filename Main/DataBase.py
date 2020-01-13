import pandas as pd
import sqlite3 as sql
from Main.MetaData import MetaData


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

    def insert_author(self, author_name):
       try:
            strin = "SELECT views_of_author from author where " \
                    "name_of_author LIKE '" + author_name + "';"
            results  = self.__db.execute(strin)


            number_of_rows = 0
            temp1 = 0


            for temp in results:
                temp1 = temp[0]
                number_of_rows += 1

            if number_of_rows == 0:

                self.__db.execute('''INSERT INTO author(name_of_author,
                                     views_of_author) VALUES (?,?)''',
                                  (author_name, 1))
                self.__db.commit()

            else:
                 self.__db.execute('''UPDATE author SET views_of_author
                                      =? where name_of_author LIKE ?''', (temp1 + 1, author_name))
                 self.__db.commit()
       except:
            temp =1
            #print("someting went wrong")

    def insert_publication_name(self, publisher_name):

        try:
            strin = "SELECT views_of_publisher from publisher where " \
                    "name_of_publisher LIKE '" + publisher_name + "';"

            results = self.__db.execute(strin)

            number_of_rows = 0
            temp1 = 0

            for temp in results:
                temp1 = temp[0]
                number_of_rows += 1

            if number_of_rows == 0:

                self.__db.execute('''INSERT INTO publisher(name_of_publisher,
                                     views_of_publisher) VALUES (?,?)''',
                                  (publisher_name, 1))
                self.__db.commit()

            else:
                self.__db.execute('''UPDATE publisher SET views_of_publisher
                                      =?where name_of_publisher LIKE ?''', (temp1 + 1, publisher_name))
                self.__db.commit()
        except:
            print("someting went wrong")

    def insert_affilname(self, affilname_name):
        try:
            strin = "SELECT views_of_affilname from affilname where " \
                    "name_of_affilname LIKE '" + affilname_name + "';"

            results = self.__db.execute(strin)

            number_of_rows = 0
            temp1 = 0

            for temp in results:
                temp1 = temp[0]
                number_of_rows += 1

            if number_of_rows == 0:

                self.__db.execute('''INSERT INTO affilname(name_of_affilname,
                                     views_of_affilname) VALUES (?,?)''',
                                  (affilname_name, 1))
                self.__db.commit()

            else:
                self.__db.execute('''UPDATE affilname SET views_of_affilname
                                      =? where name_of_affilname LIKE ?''', (temp1 + 1,affilname_name))
                self.__db.commit()
        except:
            print("something went wrong")

    def insert_affiliation_city(self, affiliation_city_name):
        try:
            strin = "SELECT views_of_affiliation_city from affiliation_city where " \
                    "name_of_affiliation_city LIKE '" + affiliation_city_name + "';"
            results = self.__db.execute(strin)

            number_of_rows = 0
            temp1 = 0

            for temp in results:
                temp1 = temp[0]
                number_of_rows += 1

            if number_of_rows == 0:

                self.__db.execute('''INSERT INTO affiliation_city(name_of_affiliation_city,
                                     views_of_affiliation_city) VALUES (?,?)''',
                                  (affiliation_city_name, 1))
                self.__db.commit()

            else:
                self.__db.execute('''UPDATE affiliation_city SET views_of_affiliation_city
                                      =? where name_of_affiliation_city LIKE ?''', (temp1 + 1,affiliation_city_name))
                self.__db.commit()
        except:
            print("something went wrong")

    def insert_affiliation_country(self, affiliation_country_name):
        try:
            strin   = "SELECT views_of_affiliation_country from affiliation_country where " \
                      "name_of_affiliation_country LIKE '" + affiliation_country_name + "';"

            results = self.__db.execute(strin)

            number_of_rows = 0
            temp1 = 0

            for temp in results:
                temp1 = temp[0]
                number_of_rows += 1

            if number_of_rows == 0:

                self.__db.execute('''INSERT INTO affiliation_country(name_of_affiliation_country,
                                     views_of_affiliation_country) VALUES (?,?)''',
                                  (affiliation_country_name, 1))
                self.__db.commit()

            else:
                print('''UPDATE affiliation_country SET views_of_affiliation_country
                                      =? where name_of_affiliation_country LIKE ?''')
                self.__db.execute('''UPDATE affiliation_country SET views_of_affiliation_country
                                      =? where name_of_affiliation_country LIKE ?''', (temp1 + 1,affiliation_country_name))
                self.__db.commit()
        except:
            print("something went wrong")

    def insert_data_by_column_name(self, column_name,data):

        try:
            read_query   = "SELECT views_of_"+column_name+" from "+column_name+" where " \
                      "name_of_"+column_name+" LIKE '" + data + "';"

            results = self.__db.execute(read_query)

            number_of_rows = 0
            temp1 = 0

            for temp in results:
                temp1 = temp[0]
                number_of_rows += 1

            if number_of_rows == 0:
                insert_querty = "INSERT INTO "+column_name+"(name_of_"+column_name+",views_of_"+column_name+"" \
                                ") VALUES (?,?)"
                self.__db.execute(insert_querty,(data,1))
                self.__db.commit()

            else:
                update_query = "UPDATE "+column_name+" SET views_of_"+column_name+"" \
                                "=? where name_of_"+column_name+" LIKE ?"
                self.__db.execute(update_query,
                                  (temp1 + 1,data))

                self.__db.commit()
        except:
            print("something wrong in "+column_name)

    def insert_metadata_in_database(self, meta_data):

        self.insert_data_by_column_name("author",meta_data.name_of_author)
        self.insert_data_by_column_name("publisher",meta_data.name_of_publisher)
        self.insert_data_by_column_name("affilname",meta_data.name_of_affilname)
        self.insert_data_by_column_name("affiliation_country",meta_data.name_of_affiliation_city)
        self.insert_data_by_column_name("affiliation_country",meta_data.name_of_affiliation_country)
    def get_authors_dataframe(self):

        df = pd.read_sql_query('select views_of_author,name_of_author from author', self.__db)
        # df =pd.get_dummies(df, columns=['name_of_author'])
        # df.iloc[:, 1:] = df.iloc[:, 1:] * df.iloc[:, 0].values

        return df

    def get_dataframe_by_colums(self,cloumn_name):
        strin = "select views_of_"+cloumn_name+",name_of_"+cloumn_name +" from "+ cloumn_name

        df = pd.read_sql_query(strin, self.__db)
        # df =pd.get_dummies(df, columns=['name_of_author'])
        # df.iloc[:, 1:] = df.iloc[:, 1:] * df.iloc[:, 0].values

        return df
    def get_pulbishers_dataframe(self):

        df = pd.read_sql_query('select views_of_publisher,name_of_publisher from publisher', self.__db)
        # df = pd.get_dummies(df, columns=['name_of_publisher'])
        # df.iloc[:, 1:] = df.iloc[:, 1:] * df.iloc[:, 0].values

        return df

    def get_affilname_dataframe(self):

        df = pd.read_sql_query('select views_of_affilname,name_of_affilname from affilname', self.__db)
        # df = pd.get_dummies(df, columns=['name_of_affilname'])
        # df.iloc[:, 1:] = df.iloc[:, 1:] * df.iloc[:, 0].values

        return df

    def get_affiliation_city_dataframe(self):

        df = pd.read_sql_query('select views_of_affiliation_city,name_of_affiliation_city from affiliation_city',
                               self.__db)
        # df = pd.get_dummies(df, columns=['name_of_affiliation_city'])
        # df.iloc[:, 1:] = df.iloc[:, 1:] * df.iloc[:, 0].values

        return df

    def get_affiliation_country_dataframe(self):

        df = pd.read_sql_query(
            'select views_of_affiliation_country, views_of_affiliation_country from affiliation_country', self.__db)
        # df = pd.get_dummies(df, columns=['name_of_affiliation_country'])
        # df.iloc[:, 1:] = df.iloc[:, 1:] * df.iloc[:, 0].values

        return df