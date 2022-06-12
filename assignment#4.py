
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://lms.umt.edu.pk/login/index.php")
driver.find_element_by_id("username").send_keys('F2019105127')
driver.find_element_by_id("password").send_keys('GNp9E5@A')
driver.find_element_by_id('loginbtn').click
time.sleep(3)
button=driver.find_element_by_tag_name("button").click()
time.sleep(3)
list1=driver.find_elements_by_tag_name("a")
for x in list1:
    j=x.text
    if len(j)>=25:
        if j[-5::]=='S2022':
            print(j)