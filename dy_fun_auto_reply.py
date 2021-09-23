#%%
import requests
import urllib
import json
from selenium import webdriver
import selenium

def qingyunke(msg):
    url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg={}'.format(urllib.parse.quote(msg))
    html = requests.get(url)
    return html.json()["content"]
    
# use attrs = driver.execute_script(script, element) to get all attributes of an element
script = 'var items = {}; \
    for (index = 0; index < arguments[0].attributes.length; ++index) \
    { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; \
        return items;'

options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "localhost:9222")
driver = webdriver.Chrome(chrome_options=options)

# chat box attributes
t1 = driver.find_elements_by_class_name('js-noblefloating-barragecont Barrage-notice--noble')
t2 = driver.find_elements_by_class_name('Barrage-notice--normalBarrage')
t3 = driver.find_elements_by_class_name('js-fansfloating-barragecont Barrage--paddedBarrage')

if len(t2) > 0:
    txt = t2[-1].text

msg = txt.split("：")[-1].split("@")[0]
usr = txt.split("：")[-2].split(" |\n")[-1]
res = qingyunke(msg)
ind_end = min(10,len(msg))
response = res + "@" + usr + ":" + msg[0:ind_end] + "..."
# check
print(txt)
print(response)

# past msg to chat box
element = driver.find_elements_by_class_name('ChatSend-txt')
element[0].send_keys(response)

# click send button
element = driver.find_elements_by_class_name('ChatSend-button')
# element[0].click()


#%%

file_name = "C:/Users/ZheChen/Desktop/cookie_mmm.txt"
with open(file_name) as f:
    t = f.read()

items = t.split(";")

