import numpy as np
import pandas as pd


import pandas as pd
import numpy as np
from Main.ScopusAPI import ScopusAPI
from Main.RecommendedData import RecommendedData
from elsapy.elsclient import ElsClient
from elsapy.elsprofile import ElsAuthor, ElsAffil
from elsapy.elsdoc import FullDoc, AbsDoc
from elsapy.elssearch import ElsSearch
import json
from Main.DataBase import DataBase
from Main.MetaData import MetaData


def main():


    db = DataBase()
    db.connect_to_database()
    db.insert_data_by_column_name("affilname","ali")
    # api = ScopusAPI()
    # api.config_api()
    # data = RecommendedData()
    # results = api.get_search_data_frame('machine learning')
    # data.preprocess_data_for_recommendation(results)
    # print(data.get_column_share_in_decision("affiliation_country"))

    # for i in data1:
    #
    #     if range_of_data==3:
    #         break
    #     if (i[0] is not None and i[0] == i[0]):
    #         db.insert_author(i[0])
    #
    #     if (i[1] is not None and i[1] == i[1]):
    #         db.insert_publication_name(i[1])
    #
    #     if (i[2] is not None and i[2] == i[2]):
    #         db.insert_affilname(i[2])
    #
    #     if (i[3] is not None and i[3] == i[3]):
    #         db.insert_affiliation_city(i[3])
    #
    #     if (i[4] is not None and i[4] == i[4]):
    #         db.insert_affiliation_country(i[4])
    #     range_of_data += 1


if __name__ == "__main__":
    main()