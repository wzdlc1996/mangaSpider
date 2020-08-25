# README.md

简易漫画爬虫, 学习使用. 

感谢 [amol-/dukpy](https://github.com/amol-/dukpy) 项目!

关于这个项目的网页: [My gitpage](https://wzdlc1996.github.io/artic/other/mangaspider/)

## Manhuaren

站点 [Manhuaren](www.manhuaren.com) 的策略是使用html文件最下方的<script>标签来动态呈现章节列表和图片. 请求图片时需要在请求头加入referer, 查看网页调试器的Network标签页可以找到.

## 90mh

站点 [90mh](www.90mh.com) 的策略类似manhuaren, 在各个章节的页面<body>中有着放着各个图片所在链接的<script>标签, 一部分为列表变量 "chapterImages" , 另一部分来自 "chapterPath", 形式为: "https://js1.zzszs.com.cn/" + chapterPath + chapterImages, 如: "https://js1.zzszs.com.cn/images/comic/55/108068/1567566288yE5aPS8mZEu0XO41.jpg". 注意这个站点由于证书原因在中国大陆无法访问, 经测试改为http协议可以下载, 但速度较慢.
