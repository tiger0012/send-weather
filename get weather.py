import requests
from bs4 import BeautifulSoup
headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
url='http://www.weather.com.cn/weather1d/101270101.shtml'
res=requests.get(url,headers=headers)
res.encoding='utf-8'
html=BeautifulSoup(res.text,'html.parser')


Weather=html.find(class_='wea')
temperature=html.find(class_='tem')



print( Weather.text,temperature.text,)

