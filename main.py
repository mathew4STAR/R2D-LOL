from selenium import webdriver as wd
import time

#paths
song_path = '/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[9]/div[2]/ytd-video-secondary-info-renderer/div/ytd-expander/ytd-metadata-row-container-renderer/div[2]/ytd-metadata-row-renderer[1]/div/yt-formatted-string'
showmore_path = '/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[9]/div[2]/ytd-video-secondary-info-renderer/div/ytd-expander/tp-yt-paper-button[2]'

target = input()

driver = wd.Chrome("C:\\Program Files (x86)\\chromedriver.exe")
driver.get(target)
time.sleep(20)
print("started")
showmore = driver.find_element_by_xpath(showmore_path)
print =("got one")
showmore.click()
song_in_video = driver.find_element_by_xpath(song_path)
print("got two")
extract_song_video = song_in_video.text

print("this")
print(extract_song_video)
print("this is it")

if extract_song_video == 'Never Gonna Give You Up (7" Mix)':
    print("Its a RickRoll lol, Runnn")
else:
    print("Its safe lol probably")