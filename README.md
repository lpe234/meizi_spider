#基于Scrapy(0.22)爬虫示例
获取([http://www.meizitu.com/](http://www.meizitu.com/))网站图片，并保存到本地文件夹(meizi_images)下。

##运行
```
python run_spider.py  # 即可
```


##网站做了一些防爬措施

1.必须使用Cookie,否则无法访问

2.访问频率限制(请求间隔2秒,可正常访问)
