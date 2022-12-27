from ConfigVariables import ConfigVariables
from ConsoleColor import ConsoleColor
from google.cloud import automl
from StorageAPI import StorageAPI


class NaturalLanguageAPI:

    def __init__(self):
        self.project_id = ConfigVariables.googleCloudProjectId
        self.project_location = ConfigVariables.googleCloudProjectLocation
        self.credentials = ConfigVariables.googleCloudCredentials
        self.cloud_region = ConfigVariables.googleCloudRegion
        self.blob_extension = ConfigVariables.blobExtension

        self.client = automl.AutoMlClient()
        self.bucket = StorageAPI().bucket

    def create_dataset(self, dataset_display_name: str, blob_name: str):
        metadata = automl.TextClassificationDatasetMetadata(
            classification_type=automl.ClassificationType.MULTICLASS
        )

        new_dataset = automl.Dataset(
            display_name=dataset_display_name,
            text_classification_dataset_metadata=metadata,
        )

        response = self.client.create_dataset(parent=self.project_location, dataset=new_dataset)

        print(f"\n{ConsoleColor.GREEN}Dataset created successfully{ConsoleColor.END} {response.result()}")

        self.__import_data_to_dataset(response.result().name.split('/')[-1], blob_name)

    def display_datasets(self):
        request = automl.ListDatasetsRequest(parent=self.project_location, filter="")
        response = self.client.list_datasets(request=request)

        number_of_datasets: int = 0

        for dataset in response:
            print()
            print(f"Dataset id: {dataset.name.split('/')[-1]}")
            print(f"Dataset name: {dataset.display_name}")
            print(f"Dataset full name: {dataset.name}")
            print(f"Dataset create time: {dataset.create_time}")

            number_of_datasets += 1

        print(f"\n{ConsoleColor.GREEN}Number of displayed datasets: {number_of_datasets}{ConsoleColor.END}\n")

    def remove_dataset(self, dataset_id: str):
        dataset_full_id = self.client.dataset_path(self.project_id, self.cloud_region, dataset_id)
        response = self.client.delete_dataset(name=dataset_full_id)

        print(f"\n{ConsoleColor.GREEN}Dataset deleted successfully{ConsoleColor.END} {response.result()}\n")

    def create_model(self, model_display_name: str, dataset_id: str):
        metadata = automl.TextClassificationModelMetadata()

        model = automl.Model(
            display_name=model_display_name,
            dataset_id=dataset_id,
            text_classification_model_metadata=metadata,
        )

        response = self.client.create_model(parent=self.project_location, model=model)

        print(f"\n{ConsoleColor.GREEN}Model created successfully{ConsoleColor.END} {response.result()}\n")

    def deploy_model(self, model_id: str):
        model_full_id = self.client.model_path(self.project_id, "us-central1", model_id)

        response = self.client.deploy_model(name=model_full_id)

        print(f"\n{ConsoleColor.GREEN}Model deployed successfully{ConsoleColor.END} {response.result()}\n")

    def evaluate_model(self, model_id: str):
        model_full_id = self.client.model_path(self.project_id, "us-central1", model_id)

        evaluations = self.client.list_model_evaluations(parent=model_full_id, filter="")

        print("List of model evaluations:")

        for evaluation in evaluations:
            print("Model evaluation name: {}".format(evaluation.name))
            print("Model annotation spec id: {}".format(evaluation.annotation_spec_id))
            print("Create Time: {}".format(evaluation.create_time))
            print("Evaluation example count: {}".format(evaluation.evaluated_example_count))
            print(
                "Classification model evaluation metrics: {}".format(
                    evaluation.classification_evaluation_metrics
                )
            )

    def apply_model_prediction(self, model_id: str):
        prediction_client = automl.PredictionServiceClient()

        model_full_id = automl.AutoMlClient.model_path(self.project_id, "us-central1", model_id)
        text_snippet = automl.TextSnippet(content=self.content, mime_type="text/plain")
        payload = automl.ExamplePayload(text_snippet=text_snippet)
        response = prediction_client.predict(name=model_full_id, payload=payload)

        for annotation_payload in response.payload:
            print(u"Predicted class name: {}".format(annotation_payload.display_name))
            print(u"Predicted class score: {}".format(annotation_payload.classification.score))

    def display_models(self):
        request = automl.ListModelsRequest(parent=self.project_location)
        response = self.client.list_models(request=request)

        number_of_models: int = 0

        for model in response:
            print()
            print(f"Model name: {model.display_name}")
            print(f"Model id: {model.name.split('/')[-1]}")
            print(f"Model full name: {model.name}")
            print(f"Model create time: {model.create_time}")

            number_of_models += 1

        print(f"\n{ConsoleColor.GREEN}Number of displayed models: {number_of_models}{ConsoleColor.END}\n")

    def remove_model(self, model_id: str):
        model_full_id = self.client.model_path(self.project_id, "us-central1", model_id)
        response = self.client.delete_model(name=model_full_id)

        print(f"\n{ConsoleColor.GREEN}Model removed successfully{ConsoleColor.END}\n {response.result()}")

    def display_current_operations(self):
        client = automl.AutoMlClient()
        response = client._transport.operations_client.list_operations(
            name=self.project_location, filter_="", timeout=5
        )

        print("List of operations:")
        for operation in response:
            if not operation.done:
                print("Name: {}".format(operation.name))
                print(operation.metadata)

    def __import_data_to_dataset(self, dataset_id: str, blob_name: str):
        dataset_full_id = self.client.dataset_path(self.project_id, self.cloud_region, dataset_id)
        blob_path = f"gs://{self.bucket.name}/{blob_name}{self.blob_extension}"

        print("Importing data to the dataset...")

        input_config = automl.InputConfig(
            gcs_source=automl.GcsSource(input_uris=[blob_path]),
        )

        response = self.client.import_data(
            name=dataset_full_id,
            input_config=input_config
        )

        print(f"\n{ConsoleColor.GREEN}Data imported successfully to the dataset{ConsoleColor.END} {response.result()}")
