from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sys

def print_same_line(text):
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write(text)
    sys.stdout.flush()

class Gleambot:
    def __init__(self,fname,email):
        self.driver = webdriver.Chrome()

    def closeBrowser(self):
        self.driver.close()

    def openweb(self):
        driver= self.driver
        driver.get("https:wn.nr/U8Zfqm")
        time.sleep(2)
        login_button= driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[1]/div[6]/div[2]/div[2]/div/form/fieldset[1]/div/ul/li[1]/a")
        login_button.click()
        time.sleep(2)
        full_name = driver.find_element_by_id("//input['contestant[email]']")
        full_name.clear()
        driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS); 
        full_name.send_keys(self.fname)
        #user_email = driver.find_element_by_xpath("//input[@name='email']")
        #user_email.send_keys(self.email)
      

    def tpmail(self):
        driver= self.driver
        driver.get("https://temp-mail.org/en/")
        time.sleep(2)


if __name__=="__main__":
    fname=""
    email =""
    gb=Gleambot(fname,email)
    #gb.tpmail()
    gb.openweb()
    
  

