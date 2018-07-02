# 雪球网爬虫 
雪球网的爬虫比起微信公众号爬虫有个易处理的点在于它的url是很有规律的，而且没有key啊userid之类的反爬虫手段  
比如https://xueqiu.com/P/ZH019696 这样，因此我们可以很容易地遍历url来爬取，但也会遇到一些问题，如有些组合已经被删除之类的
## 需求
python3 urllib urllib3 Beautifulsoup
## 代码
代码分为三部分，分别爬取了最近调仓数据、收益率走势数据和其他信息  
change.py: 先到"https://xueqiu.com/P/ZH%06d" 里去获得一个last_user_rb_gid的信息（需要用到正则表达式），之后再利用这个last_user_rb_gid直接到https://xueqiu.com/cubes/rebalancing/show_origin.json?rb_id=*** 爬取调仓数据信息
data.py: 根据规律"https://xueqiu.com/cubes/nav_daily/all.json?cube_symbol=ZH%06d" 直接进行遍历，利用http.request直接将json形式的网页内容获取。  
performance.py：利用beautifulsoup在"https://xueqiu.com/P/ZH%06d" 里find所需要的各种数据
## 数据
### change 最近调仓数据   
"stock_symbol" "stock_name" "price" "weight" "prev_weight_adjusted"  
分别是股票的id(SHXXXXXX) 名字 成交价 现权重 之前权重   
这几个数据是显示在https://xueqiu.com/P/ZH%06d 中曲线图上的 还有一些数据没显示  
  
### data 收益率走势数据  
一个文件里有两组数据 一组是该组合收益率 一组是沪深300收益率  
（我偶然发现竟然ZH打头的也有一些美股的，如果要区分只需看第二组数据的symbol是不是“SH000300”）  
然后里面关键信息就是 date 和 percent 这个是图里的两个坐标。其他信息value不太清楚是啥 time应该没用  
这个爬的时候没考虑有一些组合已经没了。。所以有大概1000多条废数据，建议以performance_weight里为准再来这个文件夹找对应组合的走势数据  

### performance_weight 其他数据  
举个例子：    
传统金融  	  组合名  
ZH000104 	  组合号  
110.92% 	  总收益  
98.61% 		   总收益打败了多少组合  
组合    	  （这行没用）  
-2.66% 		    日  
1.51%	    	    月  
2.1092  	    净值        （下面这些就是当前配置）  
纺织服装 3.28%           大类 及占比  
雅戈尔 SH600177 3.28%    大类下的具体股票 及占比  
ETF 3.47%   
300ETF SH510300 0.80%   
50ETF SH510050 2.67%   
银行 22.81%   
招商银行 SH600036 11.74%   
民生银行 SH600016 5.05%   
兴业银行 SH601166 6.02%   
非银金融 23.98%   
中国平安 SH601318 10.18%  
中信证券 SH600030 3.31%  
海通证券 SH600837 2.98%  
中国太保 SH601601 7.51%  
房地产 13.98%  
万科A SZ000002 13.98%  
现金 32.48%  
## 现状
2018.7.2 url规律依旧没变  
change.py能爬取到数据 但输出到文件时存在编码问题报错。   
data.py出现{"error_description":"遇到错误，请刷新页面或者重新登录帐号后再试","error_uri":"/cubes/nav_daily/all.json","error_code":"400016"}考虑更改headers试试。
performance.py依旧可用。

