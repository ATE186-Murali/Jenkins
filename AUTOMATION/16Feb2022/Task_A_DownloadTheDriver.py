from zipfile import ZipFile

import wget

downloadpath="D:\\driver"
wget.download("https://chromedriver.storage.googleapis.com/97.0.4692.71/chromedriver_win32.zip",downloadpath)
zipfilepath="D:\\driver\\chromedriver_win32.zip"
zip=ZipFile(zipfilepath)
ZipFile.extractall(zip,downloadpath)