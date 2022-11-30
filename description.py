from selenium import webdriver as wd
import time

def main(target):

    #song_path = '/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[9]/div[2]/ytd-video-secondary-info-renderer/div/ytd-expander/ytd-metadata-row-container-renderer/div[2]/ytd-metadata-row-renderer[1]/div/yt-formatted-string'
    #showmore_path = '/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[9]/div[2]/ytd-video-secondary-info-renderer/div/ytd-expander/tp-yt-paper-button[2]'
    #showmore_path = '/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[1]/ytd-topbar-logo-renderer/a/div/ytd-logo/yt-icon'
    #/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[9]/div[2]/ytd-video-secondary-info-renderer/div/ytd-expander/tp-yt-paper-button[2]/yt-formatted-string
    #/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[9]/div[2]/ytd-video-secondary-info-renderer/div/ytd-expander/tp-yt-paper-button[2]
    driver = wd.Chrome("C:\\Users\\mathe\\Documents\\drivers_computerfiles\\chromedriver.exe")
    driver.get(target)
    time.sleep(20)
    print("start")
    showmore = driver.find_element_by_css_selector(".more-button style-scope ytd-video-secondary-info-renderer")
    print("done")
    
    showmore.click()
    song_in_video = driver.find_element_by_xpath(song_path)
    extract_song_video = song_in_video.text

    if extract_song_video == 'Never Gonna Give You Up (7" Mix)':
        return True
    else:
        return False


main("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
