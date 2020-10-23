# README.md

简易漫画爬虫, 学习使用. 

感谢 [amol-/dukpy](https://github.com/amol-/dukpy) 项目!

关于这个项目的网页: [My gitpage](https://wzdlc1996.github.io/artic/other/mangaspider/)

## Manhuaren

站点 [Manhuaren](www.manhuaren.com) 的策略是使用html文件最下方的<script>标签来动态呈现章节列表和图片. 请求图片时需要在请求头加入referer, 查看网页调试器的Network标签页可以找到.

## 90mh

站点 [90mh](www.90mh.com) 的策略类似manhuaren, 在各个章节的页面<body>中有着放着各个图片所在链接的<script>标签, 一部分为列表变量 "chapterImages" , 另一部分来自 "chapterPath", 形式为: "https://js1.zzszs.com.cn/" + chapterPath + chapterImages, 如: "https://js1.zzszs.com.cn/images/comic/55/108068/1567566288yE5aPS8mZEu0XO41.jpg". 注意这个站点由于证书原因在中国大陆无法访问, 经测试改为http协议可以下载, 但速度较慢.

## Manhuabei

站点 [Manhuabei](www.manhuabei.com) 的策略是使用html文件中的<script>标签中的变量chapterImages加密章节图片信息. 其加密方法存放在服务器的/js/decrypt<date>.js中, 使用Crypto来进行加密. 其加密信息可以通过[PyExecJs](https://github.com/doloopwhile/PyExecJS)包来完成提取. 可以参考文章[知乎@Dmaple](https://zhuanlan.zhihu.com/p/88988849). 但在2020年更新后其js文件进行混淆, 可以使用在线工具 [beautifier](https://beautifier.io/) 来美化代码. 以20200824版的代码为例, 其解密核心在于函数(已进行部分修改):
```javascript
function decrypt20180904(_0x5676c2){//, _0x49a5d2, _0x1e530c, _0xdfae70) {
    var _0x40c64e = {
        'VZoxi': _0x1632('0', 'vMr8')
    };
    var _0x572aa3 = CryptoJS[_0x1632('1', '2Yir')][_0x1632('2', '7czB')][_0x1632('3', '0X[u')](_0x1632('4', 's^a['));
    var _0x28ee89 = CryptoJS[_0x1632('5', 'y[Ua')][_0x1632('6', 'j6Z[')]['parse'](_0x40c64e['VZoxi']);
    var _0x1fd834 = CryptoJS[_0x1632('7', 'fo3d')]['decrypt'](chapterImages, _0x572aa3, {
        'iv': _0x28ee89,
        'mode': CryptoJS[_0x1632('8', 'Il[0')][_0x1632('9', '6VXi')],
        'padding': CryptoJS[_0x1632('a', '5Zf^')][_0x1632('b', 'gbFa')]
    });
    console[_0x1632('c', 'lZsY')](_0x1fd834);
    var _0x14b724 = _0x1fd834[_0x1632('d', 'fVW(')](CryptoJS[_0x1632('e', '7czB')]['Utf8']);
    chapterImages = JSON['parse'](_0x14b724[_0x1632('f', 's^a[')]());;
    return chapterImages
    //SinMH[_0x1632('10', 'qSbe')](_0x5676c2, _0x49a5d2, _0x1e530c, _0xdfae70);
    //SinTheme[_0x1632('11', 'q68E')](_0x5676c2, _0x49a5d2, _0x1e530c, _0xdfae70);
};
```
其后三个参数均只用于初始化SinMH和SinTheme类, 同我们所要的列表无关. 另外第8行的chapterImages事实上是全局变量, 它在解码前与输入参数相等, 因此我们应当改为 _0x5676c2. 因而只需要将js文件全部复制后以execjs编译运行即可. 其中我们额外需要Crypto.js的内容, 需要调整更改以定义Crypto变量如下:
```javascript
var Crypto = function(){
...
return Crypto;
}()
```
在获得章节图片信息后即可. 值得注意的是部分章节并不从dmzj中获取, 而是通过 "manga.mipcdn.com/*" 的模式加载, 需要注意调节. 
