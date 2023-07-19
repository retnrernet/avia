from selenium import webdriver
from selenium.webdriver.common.by import By
import time,ftplib,glob,os,threading
from PIL import Image
chrome_options = webdriver.ChromeOptions()
prefs = {'profile.default_content_setting_values': {'images': 2}}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--blink-settings=imagesEnabled=false')
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")
chrome_options.headless = True
wd = webdriver.Chrome(options=chrome_options)
citiesout=["EVN", "TBS", "IKA", "CAI","SSH","HRG","SKD","TAS","TNR","DYU","DAR","TGD","JNB","DEL","BOM","VTE","DXB","SHJ","AUH","CGP","PBH","EZE","CCS","VRA","HAV","GIG", "BKK", "CXR", "SGN", "SEZ", "MLE", "DLM", "AYT", "GZP", "IST", "ADB","HKG","AQJ","AMM","CMN","RAK","CGK","DPS","KUL","RGN","PMV", "LIM","CMB","MNL","HAK", "XIY", "PEK","PVG","CAN","ICN", "AER", "KGD", "KZN"]
start=0
while True:
  text="MOW"+citiesout[start];start=start+1
  if text.endswith("EVN") or text.endswith("TBS") or text.endswith("AER"):price=7
  if text.endswith("CCS") or text.endswith("VRA") or text.endswith("EZE") or text.endswith("HAV") or text.endswith("GIG") or text.endswith("SEZ") or text.endswith("MLE") or text.endswith("LIM") or text.endswith("MEX") or text.endswith("PMV"):price=50
  if text.endswith("DXB") or text.endswith("SHJ") or text.endswith("AUH") or text.endswith("HRG") or text.endswith("SSH") or text.endswith("CAI") or text.endswith("AQJ") or text.endswith("AMM") or text.endswith("AYT") or text.endswith("IST") or text.endswith("DLM") or text.endswith("GZP") or text.endswith("ADB") or text.endswith("IKA") or text.endswith("SKD") or text.endswith("TAS"):price=11
  if text.endswith("KGD") or text.endswith("KZN"):price=3
  else:price=20
  wd.get("https://www.aviasales.ru/?params="+text+"1")
  time.sleep(1)
  try:wd.find_element(By.XPATH, '//*[@class="trip-duration__input-wrapper --departure"]').click()
  except:continue
  try:title=wd.find_element(By.XPATH, '//*[@class="s__KVUgoBX9LWUlie9mLG9M"]')
  except:pass;print("https://aviasales.ru?params="+text+"1")#print("https://aviasales.ru?params="+text+"1")
  else:print("https://aviasales.ru?params="+text+"1 "+title.text.replace("Короче, ","").replace("Местные рекомендуют",""))
  time.sleep(1)
  low=wd.find_elements(By.XPATH, '//*[@class="h__wRhMOEwg2Ub7G1CotYcY trip_dates_price --low"]')
  for x in low:
    if int(x.text[:-6])<=price:print("M "+x.text[:-6])
  try:wd.find_element(By.XPATH, '//*[@class="calendar-navbar__button --next"]').click()
  except:continue
  time.sleep(1)
  wd.find_element(By.XPATH, '//*[@class="calendar-navbar__button --next"]').click()
  time.sleep(1)
  low2=wd.find_elements(By.XPATH, '//*[@class="h__wRhMOEwg2Ub7G1CotYcY trip_dates_price --low"]')
  for i in low2:
    if int(i.text[:-6])<=price:print("M "+i.text[:-6])
