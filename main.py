#@title __⬅️ спбмск__
!pip install selenium
from selenium import webdriver;from selenium.webdriver.common.by import By;from selenium.webdriver.support import expected_conditions as EC;from selenium.webdriver.common.keys import Keys;import time;from PIL import Image
chrome_options = webdriver.ChromeOptions();prefs = {'profile.default_content_setting_values': {'images': 2}};chrome_options.add_experimental_option("prefs", prefs);chrome_options.add_argument('--headless');chrome_options.add_argument('--no-sandbox');chrome_options.add_argument('--blink-settings=imagesEnabled=false');chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.170 Safari/537.36");chrome_options.headless = True;wd = webdriver.Chrome(options=chrome_options)
citiesout=["DEL","BOM","AQJ","AMM","CMN","RAK","DLM", "AYT","GZP","IST","ADB","BJV","DXB","SHJ","AUH","HKG","CGK","DPS","KUL","VTE","RGN","MNL","HAK","XIY","CAN","PEK","SGN","CXR","PVG","ICN","CMB","BKK","PBH","UTP","CGP","TNR","DAR","JNB","PMW","CCS","VRA","HAV","PUJ","TGD","SJJ","EVN", "TBS", "IKA","KGD","KZN"];start=0;flagx=0;flagi=0
prices=["15","15","15","15","15","15","6","6","6","6","6","6","10","10","10","16","16","16","16","16","16","16","16","16","16","16","16","16","16","16","16","16","16","16","16","20","20","20","40","40","40","40","40","16","16","6","6","6","2","2"]
wd.get("https://www.bgoperator.ru/price.shtml?flt=100410000047&flt2=100510001075");tour=wd.find_elements(By.XPATH, '//*[@class="price-tour"]');print("тур египет")
for x in tour:
  try:
    if int(x.text.replace("Цены от ","").replace(" Руб.",""))<=30000:print(x.text.replace("Цены от ","").replace(" Руб.",""))
  except:pass
wd.get("https://www.bgoperator.ru/price.shtml?flt=100411293179&flt2=100510001075");tour=wd.find_elements(By.XPATH, '//*[@class="price-tour"]');print("тур турция")
for x in tour:
  try:
    if int(x.text.replace("Цены от ","").replace(" Руб.",""))<=25000:print(x.text.replace("Цены от ","").replace(" Руб.",""))
  except:pass
def ts():time.sleep(1)
def find():
  global flagx
  try:wd.find_element(By.XPATH, '//*[@class="s__Z1CqtZzeLkO0c8DmNHV7 s__u5XZeMb_TRUN_16zDQhj s__syxx275e9ITZszaXJkqO s__hyD1O3C333EEuxQT2YBC"]').click();ts()
  except:pass
  #wd.save_screenshot(text+".png")
  wd.find_element(By.XPATH, '//*[@data-test-id="start-date-field"]').click();ts();ts()
  low=wd.find_elements(By.XPATH, '//*[@class="s__wRhMOEwg2Ub7G1CotYcY"]')
  for x in low:
    try:
      if int(x.text[:-4])<=int(prices[start-1]):print(x.text[:-4]);flagx=1
    except:pass
  ts()
def title():
  if text.endswith("DLM"):print("Даламан https://aviasales.ru?params="+text+"1")
  else:
    try:title1=wd.find_element(By.XPATH, '//*[@class="s__hvsT_hXxM_QgbBjp4_0e"]');print(title1.text.replace("Короче, ","").replace("Местные рекомендуют","")+" "+"https://aviasales.ru?params="+text+"1")
    except:pass;print("https://aviasales.ru?params="+text+"1")
def rev():
  if flagx==1:print("обратно");wd.find_element(By.XPATH, '//*[@class="s__Z1CqtZzeLkO0c8DmNHV7 s__u5XZeMb_TRUN_16zDQhj s__syxx275e9ITZszaXJkqO s__hyD1O3C333EEuxQT2YBC"]').click();ts();wd.find_element(By.XPATH, '//*[@class="s__BoGysceataOvz0hbDbMg s__BYMEwUW81JOvDNJPSK85"]').click();time.sleep(2);find();wd.find_element(By.XPATH, '//*[@class="s__Z1CqtZzeLkO0c8DmNHV7 s__u5XZeMb_TRUN_16zDQhj s__syxx275e9ITZszaXJkqO s__hyD1O3C333EEuxQT2YBC"]').click();ts();wd.find_element(By.XPATH, '//*[@class="s__BoGysceataOvz0hbDbMg s__BYMEwUW81JOvDNJPSK85"]').click()
while True:
  text="MOW"+citiesout[start];start=start+1
  if text.endswith("DLM") or text.endswith("AYT") or text.endswith("GZP") or text.endswith("IST") or text.endswith("ADB") or text.endswith("BJV") or text.endswith("DXB") or text.endswith("SHJ") or text.endswith("AUH") or text.endswith("BKK") or text.endswith("PBH") or text.endswith("UTP") or text.endswith("EVN") or text.endswith("TBS") or text.endswith("KGD") or text.endswith("KZN"):
    wd.get("https://www.aviasales.ru/?params="+text.replace("MOW","LED")+"1");title();find();rev();flagx=0;flagi=0
  else:
    if text.endswith("PMW") or text.endswith("CCS") or text.endswith("VRA") or text.endswith("HAV"):
      wd.get("https://www.aviasales.ru/?params="+text+"1");title();find();rev();flagx=0;flagi=0
    else:
      wd.get("https://www.aviasales.ru/?params="+text+"1");title();find();rev();flagx=0;flagi=0;print("https://aviasales.ru?params="+"LED"+text[3:]+"1");orig=wd.find_element(By.XPATH, '//*[@class="s__WHSr5kXNWCFqhAdQ4N48 s__QK7IEyjlBUan5ZeIZqy3 s__Zp6H0IkgbCliZJ23FmWT"]')
      try:orig.clear()
      except:pass
      orig.send_keys(Keys.CONTROL + 'a');ts();orig.send_keys(Keys.BACKSPACE);ts();orig.send_keys("Пулково");ts();orig.send_keys(Keys.ENTER);action = webdriver.common.action_chains.ActionChains(wd);action.move_to_element_with_offset(orig, 1, 1);action.click();action.perform();ts();find();rev();flagx=0;flagi=0
