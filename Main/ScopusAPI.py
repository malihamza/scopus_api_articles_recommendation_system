from elsapy.elsclient import ElsClient
from elsapy.elsprofile import ElsAuthor, ElsAffil
from elsapy.elsdoc import FullDoc, AbsDoc
from elsapy.elssearch import ElsSearch
import json


class ScopusAPI:

    def __init__(self):
        self.__client = 0
        self.__config = 0

    def __config_file(self):
        con_file = open("config.json")
        self.__config = json.load(con_file)
        con_file.close()

    def __make_client(self):
        self.__client = ElsClient(self.__config['apikey'])
        self.__client.inst_token = self.__config['insttoken']

    def config_api(self):
        self.__config_file()
        self.__make_client()

    def get_search_data_frame(self, search_keywords):
        search_results_from_api = ElsSearch(search_keywords, 'scopus')
        search_results_from_api.execute(self.__client)

        return search_results_from_api.results_df
