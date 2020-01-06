# README.md

简易漫画爬虫, 学习使用. 

感谢 [amol-/dukpy](https://github.com/amol-/dukpy) 项目!

关于这个项目的网页: [My gitpage](https://wzdlc1996.github.io/artic/other/mangaspider/)

## Manhuaren

站点 [Manhuaren](www.manhuaren.com) 的策略是使用html文件最下方的<script>标签来动态呈现章节列表和图片. 请求图片时需要在请求头加入referer, 查看网页调试器的Network标签页可以找到.
