from selenium import webdriver
import pandas as pd
driver = webdriver.Chrome('/home/veerendra/whatsapp/chromedriver')
driver.get('https://web.whatsapp.com/')
src=pd.read_excel("input.xlsx","Sheet1")
whatsapp_usrnames=src['Whatsapp_usernames'].values.tolist()
messeges=src['Message'].values.tolist()
input("Press any Key to send ")
for i in range(len(whatsapp_usrnames)):
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(whatsapp_usrnames[i]))
    user.click()
    msg_box = driver.find_element_by_class_name('_2S1VP')
    msg_box.send_keys(messeges[i])
    button = driver.find_element_by_class_name('_35EW6')
    button.click()
