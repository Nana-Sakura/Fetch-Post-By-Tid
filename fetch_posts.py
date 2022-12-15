import datetime
import time
import requests
import bs4
import sqlite3
def wget(UA,url,tid):
    try:
        cache=requests.get(url,headers=UA,timeout=6.05)
        cache.raise_for_status()
        cache.encoding=cache.apparent_encoding
        return cache.text
    except:
        print("[DEBUG]:Failed to fetch tid %d."%tid)
        return ""
def modify(cache,tid):
    try:
        soup=bs4.BeautifulSoup(cache,"html.parser")
        result=soup.prettify()
        return result
    except:
        print("[DEBUG]:Failed to modify tid %d."%tid)
        return ""
def export(page,tid):
    database=sqlite3.connect("post-cache.sqlite3")
    c=database.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS posts(tid INT NOT NULL PRIMARY KEY, content MEDIUMTEXT NOT NULL)")
    try:
        c.execute("INSERT INTO posts VALUES (?,?)",(tid,page))
        database.commit()
        database.close()
    except:
        print("[DEBUG]:Failed in executing database for tid %d."%tid)
        database.close()
def fetch(tid):
    UA={"****"} #Fill in the dictionary by yourself.
    url="https://****/forum.php?mod=viewthread&tid=%d"%tid #Fill in the blank by yourself.
    print(url)
    origin=wget(UA,url,tid)
    mod=modify(origin,tid)
    export(mod,tid)
def main():
    interval=datetime.timedelta(microseconds=250)
    for i in range(****,****): #Fill in the blank by yourself.
        start=datetime.datetime.now()
        end=start+interval
        print(start)
        fetch(i)
        while datetime.datetime.now()<=end:
            time.sleep(0.000001)
        i+=1
main()
