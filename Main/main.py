from Main.RecommendedData import RecommendedData
from Main.AppStart import AppStart


def main():

    AppStart.start_application()

    recommended_system = RecommendedData()
    recommended_system.get_recommendation("deep learning")

    recommended_system.save_search_result_in_db()


if __name__ == "__main__":
    main()