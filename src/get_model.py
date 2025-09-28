import os
from huggingface_hub import snapshot_download

PATH = "./model/"

if not os.path.isdir(PATH):
    os.mkdir(PATH)
    snapshot_download(
        repo_id="openai/clip-vit-large-patch14",
        local_dir=PATH,  # where to save
        ignore_patterns=["*.msgpack", "*.h5"], # optional: skip unused formats
    )
