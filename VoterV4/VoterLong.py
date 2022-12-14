

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import random
import json

emails = json.loads(open('emails.json').read())
fnames = json.loads(open('fnames.json').read())
lnames = json.loads(open('lnames.json').read())
localnumbers = json.loads(open('localnumbers.json').read())
localzips = json.loads(open('localzips.json').read())

driver = webdriver.Chrome() 



driver.get('https://campaign.aptivada.com/contest/1379016?js=true&parent=https%3A%2F%2Fwww.audacy.com%2Fb101philly%2Fcontests%2Fchristmas-choir-voting-2022&apt_widget_type=preview&apt_widget_action=default')




while "true" == "true":
    
    tempemails = random.choice(emails)
    tempfnames = random.choice(fnames)
    templnames = random.choice(lnames)
    templocalnumbers = random.choice(localnumbers)
    templocalzips = random.choice(localzips)

    additionalemailint = random.randint(0,999)

    tempemailswithnum = str(additionalemailint)+str(tempemails)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"enterWithEmail\"]/div[1]/input")))
    email_box = driver.find_element(By.XPATH, "//*[@id=\"enterWithEmail\"]/div[1]/input")
    email_box.send_keys(tempemailswithnum)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"enterWithEmail\"]/div[2]")))
    submit_email = driver.find_element(By.XPATH, "//*[@id=\"enterWithEmail\"]/div[2]")
    submit_email.click()

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"mandatory_fields_container\"]/div[4]/div[1]/div[1]/div[2]/div[1]/select")))
    ddclick = driver.find_element(By.XPATH, "//*[@id=\"mandatory_fields_container\"]/div[4]/div[1]/div[1]/div[2]/div[1]/select")
    ddclick.click()

    
    ddclickop = driver.find_element(By.XPATH, "//*[@id=\"mandatory_fields_container\"]/div[4]/div[1]/div[1]/div[2]/div[1]/select/option[3]")
    ddclickop.click()

    time.sleep(3)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"mandatory_fields_container\"]/div[4]/div[1]/div[2]/div/div[1]/input")))
    first = driver.find_element(By.XPATH, "//*[@id=\"mandatory_fields_container\"]/div[4]/div[1]/div[2]/div/div[1]/input")
    first.send_keys(tempfnames)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"mandatory_fields_container\"]/div[4]/div[1]/div[3]/div/div[1]/input")))
    last = driver.find_element(By.XPATH, "//*[@id=\"mandatory_fields_container\"]/div[4]/div[1]/div[3]/div/div[1]/input")
    last.send_keys(templnames)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"mandatory_fields_container\"]/div[4]/div[1]/div[4]/div/div[1]/input")))
    phone = driver.find_element(By.XPATH, "//*[@id=\"mandatory_fields_container\"]/div[4]/div[1]/div[4]/div/div[1]/input")
    phone.send_keys(templocalnumbers)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"mandatory_fields_container\"]/div[4]/div[1]/div[5]/div/div[1]/input")))
    zip = driver.find_element(By.XPATH, "//*[@id=\"mandatory_fields_container\"]/div[4]/div[1]/div[5]/div/div[1]/input")
    zip.send_keys(templocalzips)

    time.sleep(2)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"mandatory_fields_container\"]/div[5]")))
    submit = driver.find_element(By.XPATH, "//*[@id=\"mandatory_fields_container\"]/div[5]")
    submit.click()

    time.sleep(1)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"formWrapper\"]/div[1]/div/div[4]/a[2]")))
    startover = driver.find_element(By.XPATH, "//*[@id=\"formWrapper\"]/div[1]/div/div[4]/a[2]")
    startover.click()



time.sleep(5)