### xuanwu(玄武)
> 玄武是一个简单的网页爬虫，主要爬取的是下厨房的网页端的分类以及APP端的列表及详情界面。下厨房前后端没有分离，所以最简单的网页爬取再过滤即可。

#### download模块
```
http 主要是爬了5K个UA,然后我本地开了个代理IP池提供爬虫代理
speed.py 多进程相关
ss_download.py 网络下载模块，接入了 延时请求，ua更换，代理更换，错误重试等
```

#### parser
```
xcf_parser.py 三个方法分别爬了：获取分类列表，获取单个分类的菜品列表，菜品内容
```


#### pipeline
```
export_to_reids.py 输出到本地redis
export_to_output.py 输出到本地py文件
```

#### tool
```
config.py  配置请求延时时间，重试次数以及redis数据前缀
```

#### go  and  mul_go
```
go 程序入口，三个方法分别对应爬三处内容（1.种类2.对应种类下列表3.列表中单个的内容）
mul_go.py 该程序入口 我这边仅在get_content方法时候使用，十个默认进程去爬菜品内容