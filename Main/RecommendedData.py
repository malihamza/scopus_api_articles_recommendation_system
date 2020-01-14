import pandas as pd
import numpy as np
from Main.DAL.DataBase import DataBase
from Main.API.ScopusAPI import ScopusAPI


class RecommendedData:
    def __init__(self):
        self.__preprocessed_data_for_recommendation = 0
        self.__links_of_articles                    = 0
        self.__titles_of_articles                   = 0
        self.__db                                   = DataBase()
        self.__api                                  = ScopusAPI()
        self.__api.config_api()

    def get_preprocessed_data_for_recommendation(self):
        return self.__preprocessed_data_for_recommendation

    def get_links_of_articles(self):
        return self.__links_of_articles

    def get_titles_of_article(self):
        return self.__titles_of_article

    @staticmethod
    def __make_affiliation_data_frame(affiliation_data):

        temp_array               = []

        for i in affiliation_data:
            if i is not None and i == i:
                temp_array.append(i[0])

        data_frame_of_affiliation = pd.DataFrame(temp_array)[['affilname', 'affiliation-city', 'affiliation-country']]

        return data_frame_of_affiliation

    def preprocess_data_for_recommendation(self, data_from_api):

        self.__preprocessed_data_for_recommendation = data_from_api[
            ['prism:url', 'dc:title', 'dc:creator', 'prism:publicationName', 'affiliation' ]]

        affiliation = self.__make_affiliation_data_frame(self.__preprocessed_data_for_recommendation['affiliation'])

        self.__preprocessed_data_for_recommendation = pd.concat([self.__preprocessed_data_for_recommendation, affiliation], axis=1)
        affiliation                                 = self.__preprocessed_data_for_recommendation ['affiliation']

        self.__links_of_articles                    = self.__preprocessed_data_for_recommendation['prism:url']
        self.__titles_of_articles                   = self.__preprocessed_data_for_recommendation['dc:title']

        del self.__preprocessed_data_for_recommendation['affiliation']
        del self.__preprocessed_data_for_recommendation['prism:url']
        del self.__preprocessed_data_for_recommendation['dc:title']

        self.__preprocessed_data_for_recommendation.columns = ['name_of_author', 'name_of_publisher',
                                                               'name_of_affilname', 'name_of_affiliation_city',
                                                               'name_of_affiliation_country']

    def make_dummy_data(self):
        self.__preprocessed_data_for_recommendation = pd.get_dummies(self.__preprocessed_data_for_recommendation,
                                                                     columns=['name_of_author', 'name_of_publisher',
                                                                              'name_of_affilname',
                                                                              'name_of_affiliation_city',
                                                                              'name_of_affiliation_country'])

    def make_dummy_data_by_columns(self,column_name):
        return pd.get_dummies(self.__preprocessed_data_for_recommendation['name_of_'+column_name], columns=['name_of_'+column_name])

    def get_column_share_in_decision(self,column_name):
        self.__db.connect_to_database()

        pre_processed_data = self.make_dummy_data_by_columns(column_name)
        data_from_database = self.__db.get_dataframe_by_colums(column_name).values

        for row_data in data_from_database:
           if row_data[1] in pre_processed_data:
               pre_processed_data[row_data[1]] = pre_processed_data[row_data[1]]*row_data[0]

        self.__db.close_database()
        return pre_processed_data.sum(axis=1)

    def get_recommendation(self,search_keywords):
        result_from_api              = self.__api.get_search_data_frame(search_keywords)
        self.preprocess_data_for_recommendation(result_from_api)

        author_data                  = self.get_column_share_in_decision("author")
        publisher_data               = self.get_column_share_in_decision("publisher")
        affilname_data               = self.get_column_share_in_decision("affilname")
        affiliation_city_data        = self.get_column_share_in_decision("affiliation_city")
        affiliation_country_data     = self.get_column_share_in_decision("affiliation_country")

        recommended_results          = author_data + publisher_data + affilname_data + affiliation_city_data + affiliation_country_data

        self.__titles_of_articles    = pd.DataFrame(self.__titles_of_articles.values, columns=['title'])
        recommended_results          = pd.concat([self.__titles_of_articles, recommended_results], axis=1)

        recommended_results          = pd.concat([self.__links_of_articles, recommended_results], axis=1)
        recommended_results.columns  = ['Url', 'Title', 'Score']
        recommended_results['Score'] = recommended_results['Score'] / recommended_results['Score'].sum()
        recommended_results          = recommended_results.sort_values(by='Score', ascending=False)

        return recommended_results

