from  selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# from selenium import webdriver
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait




def get_driver():
  chrome_options=Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver=webdriver.Chrome(options=chrome_options)
  return driver


YOUTUBE_TRENDING_URL='https://www.youtube.com/feed/trending'

if __name__=='__main__':
  print("Creating the driver")
  driver=get_driver()
  print("Fetching the page ...")
  
  driver.get(YOUTUBE_TRENDING_URL)
  
  
  # CHECK TITLE
  print("Title:",driver.title)

  print("Get the video divs")
  video_div_tag='ytd-video-renderer'
  
  video_divs=driver.find_elements(By.TAG_NAME,video_div_tag)
  print("Number of video divs found:",len(video_divs))

  print('Parsing the first video')
  # print("First video,",video_divs[0])
  video=video_divs[0]
  title_element=video.find_element(By.ID,'video-title')
  print('title:',title_element.text)
  
  print("link:",title_element.get_attribute('href'))

  thumbnail_url=video.find_element(By.TAG_NAME,'img').get_attribute('src')

  print("thumbnail_url:",thumbnail_url)


  channel_name=video.find_element(By.CLASS_NAME,'ytd-channel-name').text
  print("Channel Name:",channel_name)


  meta_block=video.find_element(By.CLASS_NAME,'ytd-video-meta-block')

  spans=meta_block.find_elements(By.TAG_NAME,'span')

  views=spans[1].text
  print("Views:",views)

  uploaded=spans[2].text
  print('uploaded:',uploaded)

  desc=video.find_element(By.ID,'description-text').text
  print("Description:",desc)

  
