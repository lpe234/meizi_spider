#基于Scrapy(0.22)爬虫示例
获取([http://www.meizitu.com/](http://www.meizitu.com/))网站图片，并保存到本地文件夹(meizi_images)下。

##运行

```
python run_spider.py  # 即可
```


##网站对请求做了一些限制

1.必须使用Cookie,否则无法访问

2.访问频率限制(请求间隔2秒,可正常访问)


---

#获取慕课网视频信息

返回数据结构如下：

```python
{'title': u'Java\u5fae\u4fe1\u516c\u4f17\u53f7\u5f00\u53d1\u8fdb\u9636',
 'videos': [{u'1-1 \u8bfe\u7a0b\u7b80\u4ecb (01:37)': u'http://v1.mukewang.com/abd539cc-0bb4-4406-a74f-44f4142b88f6/H.mp4'},
            {u'1-2 \u5fae\u4fe1\u516c\u4f17\u5e73\u53f0\u6d4b\u8bd5\u53f7 (03:17)': u'http://v1.mukewang.com/06f38c77-855d-4ee0-98d6-d9e90e84f57e/H.mp4'},
            {u'2-1 \u56fe\u6587\u6d88\u606f (15:58)': u'http://v1.mukewang.com/93391f90-d78f-4b9b-b6f5-694d328fe198/H.mp4'},
            {u'2-2 access_token\u7684\u83b7\u53d6(\u4e0a) (12:27)': u'http://v1.mukewang.com/c25173a3-39b7-4c2b-a3df-de636c5ccbeb/H.mp4'},
            {u'2-3 access_token\u7684\u83b7\u53d6\uff08\u4e0b\uff09 (08:01)': u'http://v1.mukewang.com/b3c697a4-d22c-4315-a7ac-8bac6c1e1832/H.mp4'},
            {u'2-4 \u56fe\u7247\u6d88\u606f\u56de\u590d (13:00)': u'http://v1.mukewang.com/72515165-14ff-48ac-8463-a0d4c57d6617/H.mp4'},
            {u'2-5 \u97f3\u4e50\u6d88\u606f\u7684\u56de\u590d (11:17)': u'http://v1.mukewang.com/e6b12d81-6738-4e09-87d7-ed61a22c0667/H.mp4'},
            {u'3-1 \u81ea\u5b9a\u4e49\u83dc\u5355\uff08\u4e0a\uff09 (08:11)': u'http://v1.mukewang.com/74300719-b984-42e2-8bc0-97aa7497880c/H.mp4'},
            {u'3-2 \u81ea\u5b9a\u4e49\u83dc\u5355\uff08\u4e0b\uff09 (13:48)': u'http://v1.mukewang.com/b8c06855-f410-4b51-8a21-b2da1fe3d3a5/H.mp4'},
            {u'3-3 \u83dc\u5355\u7684\u4e8b\u4ef6\u63a8\u9001 (11:09)': u'http://v1.mukewang.com/0f4724af-ecc2-43f7-a0c9-81b975b2c091/H.mp4'},
            {u'3-4 \u83dc\u5355\u67e5\u8be2\u4e0e\u5220\u9664 (07:39)': u'http://v1.mukewang.com/9101ef6b-dce6-4a34-894d-636f3fe788ec/H.mp4'},
            {u'4-1 \u767e\u5ea6\u7ffb\u8bd1\u4e00 (22:32)': u'http://v1.mukewang.com/68970e37-0b9d-49e0-944a-5458d5e0f937/H.mp4'},
            {u'4-2 \u767e\u5ea6\u7ffb\u8bd1\u4e8c (12:25)': u'http://v1.mukewang.com/820416f8-d896-4112-9e0d-68c6719993fb/H.mp4'},
            {u'5-1 \u603b\u7ed3 (04:59)': u'http://v1.mukewang.com/aeeb3a4c-df01-4e49-bff5-c16aee781118/H.mp4'}
            ]
}
```

_目前只是获取信息，并没有将视频保存在本地_

```text
本爬虫旨在帮助不方便联网观看视频教程的同学。
其实“慕课网”还是蛮不错，希望各位不要乱跑本脚本!!!****
```