from RecommendedData import RecommendedData
from AppStart import AppStart


def main():

    # This function will create database if not created and create tables if not created
    AppStart.start_application()

    recommended_system = RecommendedData()
    # use the following functions to enter keyword it will give dataframe containting recommended results
    # Use any keyword in replace of Machine Learning

    recommended_system.get_recommendation("deep learning")
    # Following function save the search result in database

    recommended_system.save_search_result_in_db()


if __name__ == "__main__":
    main()