from ConsoleColor import ConsoleColor
from GraphCreator import GraphCreator
from Menu import Menu
from NaturalLanguageAPI import NaturalLanguageAPI
from StorageAPI import StorageAPI
from WebScraper import WebScraper

if __name__ == '__main__':
    while True:
        try:
            dataset_name: str
            input_value: int

            menu: Menu = Menu()
            naturalLanguageAPI = NaturalLanguageAPI()
            storageAPI = StorageAPI()
            webScraper = WebScraper()
            graphCreator = GraphCreator()

            menu.display()

            try:
                input_value = int(input(">"))
            except TypeError:
                input_value = -1

            if input_value == 1:
                webScraper.web_scrape(
                    input("Enter the film's URL on Metacritic: ")
                )

            elif input_value == 2:
                storageAPI.create_blob(
                    input("Enter the new blob's name: "),
                    input("Enter the existing file's name: ")
                )

            elif input_value == 3:
                storageAPI.list_blobs()

            elif input_value == 4:
                storageAPI.remove_blob(
                    input(f"Enter blob's name: ")
                )

            elif input_value == 5:
                naturalLanguageAPI.create_and_fill_dataset(
                    input(f"Enter the new dataset's display name: "),
                    input("Enter the existing blob's name: ")
                )

            elif input_value == 6:
                naturalLanguageAPI.display_datasets()

            elif input_value == 7:
                naturalLanguageAPI.remove_dataset(
                    input(f"Enter id: ")
                )

            elif input_value == 8:
                naturalLanguageAPI.create_and_train_model(
                    input(f"Enter model's name: "),
                    input(f"Enter dataset's id: ")
                )

            elif input_value == 9:
                naturalLanguageAPI.evaluate_model(
                    input(f"Enter model's id: ")
                )

            elif input_value == 10:
                naturalLanguageAPI.deploy_model(
                    input(f"Enter model's id: "),
                )

            elif input_value == 11:
                output_file_path = naturalLanguageAPI.apply_model_prediction(
                    input(f"Enter model's id: "),
                    input(f"Enter filename: ")
                )

                graphCreator.plot_review_categories(output_file_path)

            elif input_value == 12:
                naturalLanguageAPI.display_models()

            elif input_value == 13:
                naturalLanguageAPI.remove_model(
                    input(f"Enter model's id: ")
                )

            elif input_value == 14:
                naturalLanguageAPI.display_current_operations()

            elif input_value == 15:
                quit(0)

            else:
                print(f"\n{ConsoleColor.RED}Incorrect input value{ConsoleColor.END}\n")

        except Exception as ex:
            print(f"{ConsoleColor.RED}{ex}{ConsoleColor.END}\n")
            