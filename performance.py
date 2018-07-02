from bs4 import BeautifulSoup

import urllib.request

import urllib3

headers = {
'Coockie':'s=ez11dvoxxg; device_id=290ceb040979f2d53958772048a4285b; u=181517828430719; __utma=1.2007484895.1517828995.1517828995.1517941552.2; __utmz=1.1517828995.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); aliyungf_tc=AQAAALpeTjJNvggAuYYXfDNQ8WEt8i38; xq_a_token=9fe68a74102e36c95d83680e70152894648189b5; xq_r_token=31f446a0ba3f00cf0ec805ef008a3ad7d7ef5f6e; Hm_lvt_1db88642e346389874251b5a1eded6e3=1517486158,1517828431,1517974579,1518002405; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1518002407',
'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.90 Safari/537.36 2345Explorer/9.2.1.17116'
}

http = urllib3.PoolManager()

for i in range(1344,1345):
    #driver = webdriver.PhantomJS(desired_capabilities=dcap)
    url = ("https://xueqiu.com/P/ZH%06d"%(i))
    #driver.get(url)
    r = http.request('GET',url,headers = headers)
    #print (r.data)
    #resp = BeautifulSoup(driver.page_source, 'html5lib')
    resp = BeautifulSoup(r.data,"html5lib")
    
    name = resp.find("span", class_="name")
    if (name==None):
        #driver.quit()
        continue
    f = open("performance_weight\\ZH%06d.txt"%(i),"w")
    print(name.string, file = f)
    Id = resp.find("span", class_ = "symbol")
    print(Id.string, file = f)
    total = resp.find_all("span", class_="per")
    print(total[0].string + "%", file=f)
    print(total[1].string, file = f)
    sub_msg = resp.find_all("div", class_="per")
    for msg in sub_msg:
        print(msg.string, file = f)
    weight_list = resp.find("div", class_="weight-list")
    weights = weight_list.find_all(recursive=False)
    for weight in weights:
        string = ""
        tools = weight.find_all(True)
        for tool in tools:
            if (tool.string != None):string = string + tool.string + " "
        print(string, file = f)
    f.close()
    #driver.quit()
