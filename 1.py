import requests
import threading
w=input("请输入爬取页数（10的倍数）:")
g=int(eval(w)/10)
keyword=input("你想爬取图片为:")
url='https://image.baidu.com/search/acjson?'
header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
def pachong(n):
    param={
        'tn': 'resultjson_com',
    'logid': '12232808846347360870',
    'ipn': 'rj',
    'ct': '201326592',
    'is':'', 
    'fp': 'result',
    'fr':'', 
    'word': keyword,
    'queryWord':keyword,
    'cl': '2',
    'lm': '-1',
    'ie': 'utf-8',
    'oe': 'utf-8',
    'adpicid': '',
    'st': '-1',
    'z':'', 
    'ic': '',
    'hd': '',
    'latest':'', 
    'copyright': '',
    's':'', 
    'se':'', 
    'tab':'', 
    'width': '',
    'height': '',
    'face': '0',
    'istype': '2',
    'qc': '',
    'nc': '1',
    'expermode': '',
    'nojc':'', 
    'isAsync': '',
    'pn': str(n),
    'rn': str(g),
    'gsm': '1e',
    '1667898142750':''
        }
    res=requests.get(url=url,headers=header,params=param)
    data=res.json()['data']
    #得到图片地址
    del data[-1]
    upages=[]
    udatas=[]
    for i in data:
        if i.get('thumbURL') !=None:
          upages.append(i['thumbURL'])
    for urr in upages:
        udatas.append(requests.get(url=urr,headers=header).content)    
    for c_data in udatas:
        with open(str(n)+'.jpg','wb')as f:
            f.write(c_data) 
        n+=1
thread_list = []
n = 0
for i in range(10): # 使用10个线程
    thread = threading.Thread(target=pachong,args=(n,))#args为数组变量参数，逗号不能省（传递参数）
    thread.start()
    thread_list.append(thread)
    n += g
for j in thread_list:
    j.join()

#https://www.cnblogs.com/shentt/p/16620869.html
