from ConsoleColor import ConsoleColor


class Menu:

    def __init__(self):
        self.buttons = (
            f"{ConsoleColor.VIOLET}* Web scraping{ConsoleColor.END}",
            f"{ConsoleColor.YELLOW}1. Get reviews from website{ConsoleColor.END} input: link",
            f"{ConsoleColor.VIOLET}* Google Cloud Storage operations (blobs){ConsoleColor.END}",
            f"{ConsoleColor.YELLOW}2. Add a blob{ConsoleColor.END} input: file_name, blob_name",
            f"{ConsoleColor.YELLOW}3. Display all blobs{ConsoleColor.END} displays: blob_name",
            f"{ConsoleColor.YELLOW}4. Remove a blob{ConsoleColor.END} input: blob_name",
            f"{ConsoleColor.VIOLET}* Vertex AI operations (datasets){ConsoleColor.END}",
            f"{ConsoleColor.YELLOW}5. Create and fill the dataset{ConsoleColor.END} input: dataset_name, blob_name",
            f"{ConsoleColor.YELLOW}6. Display all datasets{ConsoleColor.END} displays: dataset_name, dataset_id etc.",
            f"{ConsoleColor.YELLOW}7. Remove a dataset{ConsoleColor.END} input: dataset_id",
            f"{ConsoleColor.VIOLET}* Vertex AI operations (models){ConsoleColor.END}",
            f"{ConsoleColor.YELLOW}8. Create and train a model{ConsoleColor.END} input: model_name, dataset_id",
            f"{ConsoleColor.YELLOW}9. Evaluate a model{ConsoleColor.END} input: model_id",
            f"{ConsoleColor.YELLOW}10. Deploy a model{ConsoleColor.END} input: model_id",
            f"{ConsoleColor.YELLOW}11. Apply model prediction{ConsoleColor.END} input: model_id, file_name",
            f"{ConsoleColor.YELLOW}12. Display all models{ConsoleColor.END} displays: model_name, model_id etc.",
            f"{ConsoleColor.YELLOW}13. Remove a model{ConsoleColor.END} input: model_id",
            f"{ConsoleColor.VIOLET}* Other {ConsoleColor.END}",
            f"{ConsoleColor.YELLOW}14. Display all current operations {ConsoleColor.END}",
            f"{ConsoleColor.BLUE}15. Exit{ConsoleColor.END}"
        )

    def display(self):
        print(f"Choose your action by typing a digit\n")
        for button in self.buttons:
            print(button)
