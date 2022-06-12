import time
from selenium import webdriver
import urllib.request
############################# Nature
#driver = webdriver.Chrome()
#driver.get("https://unsplash.com/s/photos/nature")
#d=driver.find_element_by_css_selector("#app > div > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div > div")
#im=d.find_elements_by_tag_name("img")
#print(im)
#i=0

#for x in im:
 #   link=x.get_attribute("src")
  #  if x.get_attribute("class")=="YVj9w":
   #     path="nature/a"+str(i)+".jpg"
    #    urllib.request.urlretrieve(link,path)
     #   print(i,"= ",link,path)
      #  i = i + 1
       # if i==10:
        #    break

###################################Beach
#driver = webdriver.Chrome()
#driver.get("https://unsplash.com/s/photos/beach")
#d=driver.find_element_by_css_selector("#app > div > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div > div")
#im=d.find_elements_by_tag_name("img")
#i=0

#for x in im:
    #link=x.get_attribute("src")
    #if x.get_attribute("class")=="YVj9w":
        #path="Beach/a"+str(i)+".jpg"
        #urllib.request.urlretrieve(link,path)
        #print(i,"= ",link,path)
        #i = i + 1
       # if i==10:
           # break
#################################################Animals

driver = webdriver.Chrome()
driver.get("https://unsplash.com/s/photos/animals")
d=driver.find_element_by_css_selector("#app > div > div:nth-child(3) > div:nth-child(5) > div:nth-child(1) > div")
im=d.find_elements_by_tag_name("img")
i=0

for x in im:
    link=x.get_attribute("src")
    if x.get_attribute("class")=="YVj9w":
        path="Animal/a"+str(i)+".jpg"
        urllib.request.urlretrieve(link,path)
        print(i,"= ",link,path)
        i = i + 1
        if i==10:
            break