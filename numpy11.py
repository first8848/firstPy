import requests
import os
from PIL import Image
from IPython.display import IFrame
url='https://www.ibm.com/'
r=requests.get(url)
r.status_code
print(r.status_code)
header = r.headers
print(r.headers)
