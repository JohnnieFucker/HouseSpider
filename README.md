# HouseSpider
基于python的scrapy爬虫，爬取链家网成都地区别墅房价，并用高德api在地图上可视化显示

1.工程里面已经有爬取后的rent.csv文件，可以删除，然后执行命令scrapy crawl HouseSpider -o rent.csv -t csv生成csv文件

2.爬取完成后，执行命令python -m SimpleHTTPServer 3000,然后打开http://localhost:3000，导入上面生成的rent.csv文件即可。

参考[buyhouse](https://github.com/happyte/buyhouse)
