# 图书馆占座分析

## 自行抓Cookies或登录网址!

## 自行抓Cookies或登录网址!!

## 自行抓Cookies或登录网址!!!

## 必须使用Nodejs环境,不然Execjs模块会崩溃

### 主页地址:
http://wechat.v2.traceint.com/index.php/reserve/index.html

```
  <a href="javascript:;" data-url="/index.php/reserve/layout/libid=10557.html&amp;1599880808" class="list-group-item ">
    <h4 class="list-group-item-heading">南301中文图书借阅七厅 (3楼) 	<span class="badge" style="background: none; color:#5c84bd; font-size: 16px;">18/72</span> </h4>
    <p class="list-group-item-text">		8:00 ~  22:15	开馆前可提前 30分钟 预定		</p>
  </a>
```
从中可以找到区域id
### 座位列表
http://wechat.v2.traceint.com/index.php/reserve/layout/libid=10550.html&1599880808
(最后面Unix时间戳)

带Cookies提交下面网址选座
http://wechat.v2.traceint.com/index.php/reserve/get/libid=10550&RAe2fw=21,15&yzm=

libid -> 区域id

RAe2fw -> 随机字符串

21,15 -> 座位坐标,关键字'data-key'

```html
  <div class="grid_cell  grid_active grid_status3" data-key="15,15" style="left:560px;top:560px;">
  <em>8</em>
  </div>
```

#### RAe2fw生成
http://wechat.v2.traceint.com/index.php/reserve/layout/libid=10550.html&1599880808

在座位列表的HTML中分析查找(大概倒数第三行?)

`<script src="http://static.wechat.v2.traceint.com/template/theme2/cache/layout/bMtmT7rnm8WYTXtN.js"></script>`

下面是一个例子
```javascript
  var G = function(t) {
  var r = ""
    , a = []
    , h = []
    , c = t.length;
  for (i = 0; i < c; i++)
      a[i] = t.charCodeAt(i),
      h[i] = t.charCodeAt(i + 1);
  for (i = 0; i < c; i += 2)
      r += String.fromCharCode(a[i] - h[i]);
  return r
  };
  reserve_seat = function(a, h, t) {
  void 0 === t && (t = "");
  var r = "EkdtsN".charAt(4)
    , c = (r = "dMESXY".charAt(4),
  "jFHcsDpKWi".charAt(8))
    , A = (c = "WxiHztyT°z".charAt(8),
  "nNGSBGtZKsKi".charAt(6))
    , i = (A = "kfDaanětfSrF".charAt(6),
  "zRJrHaKz".charAt(4))
    , e = (i = "JJDpĘyAG".charAt(4),
  "FxdBGzh".charAt(2))
    , s = "eJaAWjGHmÊycYDYsZA".charAt(9)
    , n = "iJJye¾tAwNYhyQ".charAt(5)
    , D = "DHpkTxMcMh".charAt(2)
    , f = (D = "ae¥BrnJaek".charAt(2),
  "QYiXnNzsyJE".charAt(8))
    , C = (f = "NptBGBWSGYS".charAt(8),
  f = "ZDeYyGwN±Rp".charAt(8),
  "AhDDWCRQDSHmxNmDZ".charAt(8))
    , m = (C = "yTmHisrJëNzaDabWX".charAt(8),
  "ĊCZsZZMGbh".charAt(0))
    , o = "DfEhTSpaKmw".charAt(8)
    , H = ("XYiDfkMjHwC".charAt(8),
  "WXahGWRhbPC".charAt(8),
  o = "isSTmFmxûYw".charAt(8),
  "XwxAHThHCR".charAt(2))
    , d = "dQxkt".charAt(0)
    , p = "wJbxsEexsZdrPADk".charAt(8)
    , x = "nFxb³Z".charAt(4);
  jpkNDjeFHs = n + e + o + x + s + p + C + H + m + c + i + D + A + f + d + r;
  x = "idycsx".charAt(4),
  x = "fYJhfC".charAt(4),
  x = "pJhekw".charAt(4),
  d = "bTJrRk".charAt(0),
  d = "nhpRHG".charAt(0),
  H = "pEEMSNmTiz".charAt(2),
  f = "jcCDpxfPFae".charAt(8),
  f = "nsyGCCJWpbH".charAt(8),
  n = "NiACBcfshtkaZb".charAt(5),
  n = "xSQCsesCMjDSeD".charAt(5),
  e = "HfzdeSH".charAt(2),
  e = "HKkNiHT".charAt(2),
  A = "pfznxKrDNCDm".charAt(6),
  A = "YGYmdHMFCTic".charAt(6),
  A = "yQdzmmRnbhQc".charAt(6),
  c = "DhencrjCFm".charAt(8),
  r = "XtcaMK".charAt(4),
  r = "CsXwch".charAt(4),
  r = "NhTAMS".charAt(4);
  T.ajax_get(AJAX_URL + "libid=" + a + "&" + G(jpkNDjeFHs) + "=" + h + "&yzm=" + t, function(t) {
      var r = "undefined" == typeof _ORG || _ORG;
      "0" == t.code ? (T.tips(t.msg),
      setTimeout(function() {
          location.href = t.url
      }, 1e3)) : r && 1e3 == t.code ? show_yzm(function(t) {
          reserve_seat(a, h, t)
      }) : T.tips(t.msg)
  })
  }
  ;
```

