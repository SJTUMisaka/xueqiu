import urllib.request

import urllib3

headers = {#'Connection':'keep-alive',
'Cookie':'s=ez11dvoxxg; device_id=290ceb040979f2d53958772048a4285b; aliyungf_tc=AQAAAJmjhDzTqAkA24YXfFRjeCWSbhyb; xq_a_token=9fe68a74102e36c95d83680e70152894648189b5; xq_a_token.sig=Wp2RDfA0m2SS1--eP6TyzeJrNqE; xq_r_token=31f446a0ba3f00cf0ec805ef008a3ad7d7ef5f6e; xq_r_token.sig=-MGYDh3MlR7dkoz1vYeWUVTTyoQ; u=181517828430719; Hm_lvt_1db88642e346389874251b5a1eded6e3=1517486158,1517828431; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1517828448',
#'Cookie':'s=e815x09tza; device_id=829a889d70417a92843da1d2b4e30912; __utmz=1.1517489222.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); aliyungf_tc=AQAAACm12XXeMggAUoYXfCgZn99nnGZe; Hm_lvt_1db88642e346389874251b5a1eded6e3=1517568957,1517586418,1517726552,1517733942; bid=c8c536ef6e8b2e28cef8f37cebc7f6a5_jd8si587; xq_a_token=bd227a1ab5ff9e3703cad21d13a58339e1fb7ce5; xqat=bd227a1ab5ff9e3703cad21d13a58339e1fb7ce5; xq_r_token=e77c423dbaac8c63db068eea2c243bf8047e31e8; xq_is_login=1; u=8337197601; __utmc=1; __utma=1.1419189262.1517489222.1517756336.1517758519.4; snbim_minify=true; _sid=YxWSRCNxAH7b1QxLect8bXoMHv4pfw; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1517802873',
#'Cookie':'s=e815x09tza; device_id=829a889d70417a92843da1d2b4e30912; __utmz=1.1517489222.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=1.1419189262.1517489222.1517489222.1517568976.2; aliyungf_tc=AQAAACm12XXeMggAUoYXfCgZn99nnGZe; Hm_lvt_1db88642e346389874251b5a1eded6e3=1517568957,1517586418,1517726552,1517733942; bid=c8c536ef6e8b2e28cef8f37cebc7f6a5_jd8si587; _sid=6xG42MM4bjS6eO2NLYnaSLwmOhAW0g; xq_a_token=bd227a1ab5ff9e3703cad21d13a58339e1fb7ce5; xqat=bd227a1ab5ff9e3703cad21d13a58339e1fb7ce5; xq_r_token=e77c423dbaac8c63db068eea2c243bf8047e31e8; xq_is_login=1; u=8337197601; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1517749054',
#'Host':'xueqiu.com',
#'Referer':'https://xueqiu.com/P/ZH139823',
'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.90 Safari/537.36 2345Explorer/9.2.1.17116'
#'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
#'X-Requested-With':'XMLHttpRequest'
}

#url = "https://xueqiu.com/cubes/nav_daily/all.json?cube_symbol=ZH000000"

#req = urllib.request.Request(url,headers=headers)
#html = urllib.request.urlopen(req).read().decode('utf-8')
#print(html)

http = urllib3.PoolManager()

for i in range(200,300):
    url = ("https://xueqiu.com/cubes/nav_daily/all.json?cube_symbol=ZH%06d"%(i))
    f = open("data\\ZH%06d.txt"%(i), "w")
    r = http.request('GET',url,headers = headers)
    print (r.data.decode("utf-8"),file = f)
    f.close()
