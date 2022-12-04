import requests

from bs4 import BeautifulSoup

import sys

import re



if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    sys.exit("Error: Please enter the TED talk URL")

#url = "https://www.ted.com/talks/dan_harris_the_benefits_of_not_being_a_jerk_to_yourself"

response = requests.get(url)
#print(response.content)
#print("download about to start")

soup = BeautifulSoup(response.content, "html.parser")

result=soup.find(id="__NEXT_DATA__")

print(re.search("(?P<url>https?://[^\s]+)(mp4)",str(result)))

"""
for val in soup.find(id="__NEXT_DATA__"):
    if (re.search("talkPage.init",str(val))) is not None:
        result = str(val)

try:
    result_mp4 = re.search("(?P<url>https?://[^\s]+)(mp4)", result).group("url")
except AttributeError:
     result_mp4 = re.search("(?P<url>https?://[^\s]+)(mp4)", result)


mp4_url = result_mp4.split('"')[0]

print("downloading video from..."+mp4_url)

file_name = mp4_url.split("/")[len(mp4_url.split("/"))-1].split('?')[0]

r = requests.get(mp4_url)
with open(file_name,'wb') as f:
    f.write(r.content)

print("download finished")
"""