import os


class ConfigVariables:
    pythonProjectRootDirectory = os.path.dirname(os.path.abspath(__file__))
    googleCloudProjectId = "automl-370415"
    googleCloudRegion = f"us-central1"
    googleCloudProjectLocation = f"projects/{googleCloudProjectId}/locations/{googleCloudRegion}"
    googleCloudCredentials = os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = \
        os.path.join(pythonProjectRootDirectory, "google-cloud-credentials.json")
    googleCloudBucketName = "datasets_ccs"
    blobExtension = ".csv"
    localCsvFilesFolder = "ReviewFiles"
    localCsvFilesLocation = os.path.join(pythonProjectRootDirectory, localCsvFilesFolder)