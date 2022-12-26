CustomKaraokeURL = "https://www.karaoke-version.com/custombackingtrack/fantasy/wenn-du-mir-in-die-augen-schaust.html"
username = "username 
password = "password"

################################################
# AST.PL
# Automatic Single Track Playback Loader
# (c) 2022 Christian Gehring
# mailto:christian@gehring.com
# https://sites.google.com/it-secrets.de/browser-fernsteuerung
################################################

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

############################
#Init
############################

############################
#Download Track
############################
def dl_track(tracknumber):
    driver.get(CustomKaraokeURL)
    time.sleep(1)
    # Solo Click track to unmask all channels
    solo = driver.find_element_by_xpath('//*[@id="html-mixer"]/div[1]/div[2]/div[1]/button[2]')
    solo.click()
    time.sleep(1)
    # Solo Click track for download
    solo = driver.find_element_by_xpath('//*[@id="html-mixer"]/div[1]/div[2]/div['+tracknumber+']/button[2]')
    solo.click()
    time.sleep(1)
    # Start download
    download = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div[6]/div[2]/div[2]/a/span[2]')
    time.sleep(1)                             
    download.click()
    time.sleep(30)

 

############################
#Main
############################

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.karaoke-version.com/my/login.html")
time.sleep(3)

############################
#Login
############################
id_box = driver.find_element_by_name('frm_login')
id_box.send_keys(username)
id_box = driver.find_element_by_name('frm_password')
id_box.send_keys(password)
login_button = driver.find_element_by_name('sbm')
login_button.click()
time.sleep(1)

################################################
#Jump to Song URL & Reset alle Tracks to Default
################################################
driver.get(CustomKaraokeURL)
time.sleep(1)
reset = driver.find_element_by_xpath('//*[@id="html-mixer"]/div[1]/div[1]/div[2]/button[2]')
reset.click()
time.sleep(1)

############################
#Get Tracks
############################
tracks = driver.find_elements_by_class_name('track__caption')
CountTracks = len(tracks)
tracknames = []
for track in tracks:
    print(track.text)
    tracknames.append(track.text)

CountTracks = len(tracks)
for i in range(2,CountTracks+1):
    dl_track(str(i))
    print(str(i))

driver.quit()
exit()
