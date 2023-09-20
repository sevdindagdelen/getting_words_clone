from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://app.memrise.com/course/1022039/the-oxford-3000-ingilizce-turkce/1/")
time.sleep(1)


global sozlukIngilizce,sozlukTurkce
sozlukIngilizce=[]
sozlukTurkce=[]
def getWords():
    element=driver.find_elements(By.CLASS_NAME,"thing.text-text")
    
    for e in element:
        bilgi=e.find_elements(By.CLASS_NAME,"col_a.col.text")
        for b in bilgi:
            metin=b.text
            print(metin)
            sozlukIngilizce.append(metin)
    
    for e in element:
        bilgi=e.find_elements(By.CLASS_NAME,"col_b.col.text")
        for b in bilgi:
            metin=b.text
            print(metin)
            sozlukTurkce.append(metin)    
            
  
sayac=0
while(True):
    sayac=sayac+1
    getWords()
    if (sayac==35):
        break
    driver.find_element(By.CLASS_NAME,"level-nav.level-nav-next").click()
    
    

with open("sozlukIngilizce","w",encoding="utf-8") as file:       
        for soz in sozlukIngilizce:
            file.write(soz + "\n")    
            
with open("sozlukTurkce","w",encoding="utf-8") as file:       
        for soz in sozlukTurkce:
            file.write(soz + "\n")                

print(len(sozlukIngilizce)," ",len(sozlukTurkce))
driver.quit()    






        
            
            
            
            
                