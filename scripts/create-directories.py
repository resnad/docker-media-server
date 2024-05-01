import os
import sys

media_dict = {
    "media": {
        "movies": "",
        "tv": "",
        "anime": "",
        "music":"",
        "books":""
    },
    "torrents": {
        "movies": "",
        "tv": "",
        "anime": "",
        "music":"",
        "books":""
    },
    "usenet": {
        "complete": {
            "anime": "",
            "books": "",
            "movies": "",
            "music": "",
            "tv":""
        },
        "incomplete":""
    }
}

def create_folders(folder_dict, parent_path=''):
    for folder_name in folder_dict:
        folder_path = os.path.join(parent_path, folder_name)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        if isinstance(folder_dict[folder_name], dict):
            create_folders(folder_dict[folder_name], folder_path)

# Check if path argument is provided
if len(sys.argv) < 2:
    print('Please provide a parent folder path. Example: "python3 create_directories.py /data"')
    sys.exit()

parent_folder = sys.argv[1]
create_folders(media_dict, parent_folder)
print(
"""
Folder structure successfully created.

data
├── media
│   ├── anime
│   ├── books
│   ├── movies
│   ├── music
│   └── tv
├── torrents
│   ├── anime
│   ├── books
│   ├── movies
│   ├── music
│   └── tv
└── usenet
    ├── complete
    │   ├── anime
    │   ├── books
    │   ├── movies
    │   ├── music
    │   └── tv
    └── incomplete

Remember to run these commands to give your user permissions over these folders:
sudo chown -R $USER:$USER /data
sudo chmod -R a=,a+rX,u+w,g+w /data
"""
)