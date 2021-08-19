import os
import sqlite3
import json
from win32crypt import CryptUnprotectData


def get_cookie_from_chrome(host: '.oschina.net'):

    cookie_path = os.environ['LOCALAPPDATA']+r"\Google\Chrome\User Data\Default\Cookies"
    sql = "select host_key,name,encrypted_value from cookies where host_key='%s'" % host
    with sqlite3.connect(cookie_path) as conn:
        cu = conn.cursor()

        # The following original code does not work. So I directly read a cookie for a user
        # cookies = {name: CryptUnprotectData(encrypted_value)[1].decode() for host_key, name, encrypted_value in cu.execute(sql).fetchall()}
        with open("C:/Users/ZheChen/Desktop/usr_cookie_1.json", "r") as f:
            cookies = json.load(f)

        for key in cookies.keys():
            cookie_jar = cookies[key]  # for each user

        cookies = cookie_jar
        # end of modification

        # print(cookies)
        return cookies
