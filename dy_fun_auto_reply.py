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
t4 = driver.execute_script(script='return document.getElementsByClassName(\'js-noblefloating-barragecont Barrage-notice--noble\')')
t5 = driver.execute_script(script='return document.getElementsByClassName(\'Barrage-notice--normalBarrage\')')
t6 = driver.execute_script(script='return document.getElementsByClassName(\'js-fansfloating-barragecont Barrage--paddedBarrage\')')

if len(t2) > 0:
    txt = t2[-1].text
elif len(t3) > 0:
    txt = t3[-1].text
elif len(t1) > 0:
    txt = t1[-1].text
elif len(t5) > 0:
    txt = t5[-1].text
elif len(t6) > 0:
    txt = t6[-1].text
elif len(t4) > 0:
    txt = t4[-1].text

msg = txt.split("：")[-1].split("@")[0]
usr = txt.split("：")[-2].split(" ")[-1].split("\n")[-1]
res = qingyunke(msg)
ind_end = min(10,len(msg))
response = res + "@" + usr + ":" + msg[0:ind_end] + "..."
# check
print(txt)
print(response)

# past msg to chat box
element = driver.find_elements_by_class_name('ChatSend-txt')
# element[0].send_keys(response)

# click send button
element = driver.find_elements_by_class_name('ChatSend-button')
element[0].click()

# get cookies and convert to dictionary
d = {}
cookies = driver.get_cookies()
for item in cookies:
    key = item['name']
    value = item['value']
    d.update({key:value})

# write as json file
file_name = "C:/Users/chenz/Desktop/cookie.json"
with open(file_name, 'w') as f:
    json.dump(d,f)
    
#%%
import json

# read cookie from txt
file_name = "C:/Users/chenz/Desktop/cookie.txt"
with open(file_name) as f:
    t = f.read()

d = {}
for item in t.split(";"):
    key, value = item.split("=")
    d.update({key:value})

