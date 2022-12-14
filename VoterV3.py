

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome() 


driver.get('https://campaign.aptivada.com/contest/1379016?js=true&parent=https%3A%2F%2Fwww.audacy.com%2Fb101philly%2Fcontests%2Fchristmas-choir-voting-2022&apt_widget_type=preview&apt_widget_action=default')


while "true" == "true":
    
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"enterWithEmail\"]/div[1]/input")))
    email_box = driver.find_element(By.XPATH, "//*[@id=\"enterWithEmail\"]/div[1]/input")
    email_box.send_keys("matthew@ifloyd.com")

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"enterWithEmail\"]/div[2]")))
    submit_email = driver.find_element(By.XPATH, "//*[@id=\"enterWithEmail\"]/div[2]")
    submit_email.click()

    longmode = "yes"

    try:

        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"mandatory_fields_container\"]/div[4]/div[1]/div[1]/div[2]/div[1]/select")))
        ddmenu = driver.find_element(By.XPATH, "//*[@id=\"mandatory_fields_container\"]/div[4]/div[1]/div[1]/div[2]/div[1]/select")
        ddmenu.click()

        
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"mandatory_fields_container\"]/div[4]/div[1]/div[1]/div[2]/div[1]/select/option[2]")))
        ddoption = driver.find_element(By.XPATH, "//*[@id=\"mandatory_fields_container\"]/div[4]/div[1]/div[1]/div[2]/div[1]/select/option[3]")
        ddoption.click()

    except:

        longmode = "no"

    if longmode == "yes":
        print("longmode")
        time.sleep(1)
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"mandatory_fields_container\"]/div[5]")))
        submitbuttonlong = driver.find_element(By.XPATH, "//*[@id=\"mandatory_fields_container\"]/div[5]")
        submitbuttonlong.click()
        time.sleep(1)
        
        print("longbuttonclicked")
    if longmode == "no":
        print("shortmode")
        
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"mandatory_fields_container\"]/div[5]")))
        submitbuttonshort = driver.find_element(By.XPATH, "//*[@id=\"mandatory_fields_container\"]/div[5]")
        submitbuttonshort.click()
        time.sleep(1)

    
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"formWrapper\"]/div[1]/div/div[4]/a[2]")))
    startover =  driver.find_element(By.XPATH, "//*[@id=\"formWrapper\"]/div[1]/div/div[4]/a[2]")
    startover.click()




time.sleep(5)