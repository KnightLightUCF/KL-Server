from urllib.request import urlretrieve
from zipfile import ZipFile 
import os


'''
Will make a http request to the dropbox link.
Here it will download the files as a zip.
Then ZipFile will unzip it.
'''
def download_skybrush_DROP_BOX():
    url = (
        "https://www.dropbox.com/scl/fi/1euh62vgk5f40ohynekp2/skybrush-server.zip?rlkey=prkfe1gh6wrv9ym3wetwvbjk4&dl=1"
    )
    filename = "skybrush_download.zip"

    urlretrieve(url,filename)

    with ZipFile("skybrush_download.zip", 'r') as zObject: 
  
        #Extracting specific file in the zip 
        # into a specific location. 
        zObject.extractall(path="skybrush-server")

        zObject.close() 

    os.remove("skybrush_download.zip")

'''
Checks if skybrush is downloaded on their machine
'''
def is_skybrush_downloaded() -> bool:
    for file_name in os.listdir():
        if file_name == "skybrush-server":
            return True
    return False

'''
logic for checking download and installing skybrush
'''
def download_check() -> bool:
    result = is_skybrush_downloaded()
    if not result:
        print("[WARNING] SKYBRUSH NOT INSTALLED. NOW INSTALLING.")
        download_skybrush_DROP_BOX()
    return result