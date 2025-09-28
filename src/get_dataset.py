import os
import kagglehub

PATH = "./"

if not os.path.isdir(PATH + "datasets/"):
    # Creates and downloads to a folder `datasets` inside `PATH`
    os.environ["KAGGLEHUB_CACHE"] = PATH
    kagglehub.dataset_download("asaniczka/mammals-image-classification-dataset-45-animals")