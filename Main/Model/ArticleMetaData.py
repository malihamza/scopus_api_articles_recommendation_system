class ArticleMetaData:
    def __init__(self):
        self.__preprocessed_data_for_recommendation = 0
        self.__links_of_articles = 0
        self.__titles_of_articles = 0

    def get_preprocessed_data_for_recommendation(self):
        return self.__preprocessed_data_for_recommendation

    def get_links_of_articles(self):
        return self.__links_of_articles

    def get_titles_of_article(self):
        return self.__titles_of_article

    def set_titles_of_article(self, src):
        self.__titles_of_article = src

    def set_links_of_articles(self, src):
        self.__links_of_articles = src

    def set_preprocessed_data_for_recommendation(self, src):
        self.__preprocessed_data_for_recommendation = src
