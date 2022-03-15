import requests
from bs4 import BeautifulSoup
YOUTUBE_TRENDING_URL='https://www.youtube.com/feed/trending'

response=requests.get(YOUTUBE_TRENDING_URL)  #does not execute javascript

if response.status_code == 200:
  print("We are good to go")
else:
  print("Error")


# print(f"Output:{response.text[:100]}" )
# with open('trending.html','w') as f:
#   f.write(response.text)

soup=BeautifulSoup(response.text,'html.parser')

# print('Page title:',soup.title.text)

# find video divs
selective_class='style-scope ytd-rich-grid-media'
video_divs=soup.find_all('div',{'class':selective_class})

print("videos found:",len(video_divs))
# print("video tag:",video_divs[0])

