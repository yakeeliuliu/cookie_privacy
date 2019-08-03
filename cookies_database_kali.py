# coding: utf-8

# In[1]:


import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pickle
import MySQLdb
import pymysql
import json


#open a chrome and locate the search bar and put search keywords
def test_search_in_python_org():
    driver = webdriver.Chrome()
    driver.get("http://python.org")
    #assert("Python", driver.title)
    elem = driver.find_element_by_name("q")
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
#get cookies and use pickle to dump and save the cookies in a pkl file
def cookies():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("http://python.org")
    cookies = driver.get_cookies()
    print(cookies)
    pickle.dump( cookies , open("cookies.pkl","wb"))
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        print(cookie)
        driver.add_cookie(cookie)
    print(cookie)

def connect_db():
    coon = pymysql.connect(
    host = '127.0.0.1',user = 'root',passwd = '',
    port = 3306,db = 'test',charset = 'utf8')
    #port必须写int类型
    #charset必须写utf8，不能写utf-8
    cur = coon.cursor()
    #cur.execute('insert into cookies(domain,is_http_only,name,path,is_secure,value) VALUE ("baidu.com","yes","cookie","yes","c:\","sdfdlklf,df3434");')
    #coon.commit()
    #cur.execute("select * from cookies")  #查询数据
    #res = cur.fetchall()    #获取结果
    #print(res)
    #cur.close()     #关闭游标
    #coon.close()    #关闭连接
    #如果是插入数据，则要commit一下，把第9行换成以下两行
    #cur.execute('insert into stu(name,is_http_only,name,path,is_secure,value) VALUE ("baidu.com","yes","cookie");')
    #coon.commit()
    #insert_pkl_to_database():
    cookies_pkl = pickle.load(open("cookies.pkl", "rb"))
   
    for cookie in cookies_pkl:
        val = []
        for key,value in cookie.items():
            print("key is : " + key)
            print("value is :" + str(value) + "\n")
            val.append(str(value))
        print(val)
        if len(val) == 7:
	    sql = "INSERT INTO cookies(domain,expiry,is_http_only,name,path,is_secure,value) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            cur.execute(sql,val)
            coon.commit()
        else:
            print("There is some atribute missing ：" + str(val) + "\n")
    #for cookie in cookies_pkl:
    #    print(cookie)
    #    cur.execute("""INSERT INTO cookies VALUES ()""", (cookie, ))
    print("$$$$$$$$$$$$$ The SELECT QUERY RESULT $$$$$$$$$$$$$$$$$$\n")
    cur.execute("select * from cookies")  #查询数据
    res = cur.fetchall()    #获取结果
    print(res)
    cur.close()     #关闭游标
    coon.close()    #关闭连接


#test_search_in_python_org()
cookies()
connect_db()


