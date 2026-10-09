# 预防骨质疏松的关键营养素数据网站，本项目为本人原创，2022 年独立完成，2026 年 10 月上传存档。
> Original work developed independently by the author in 2022; uploaded in October 2026.

毕业设计项目：使用 Python 爬虫定向爬取食物营养成分数据（钙、磷、脂肪、蛋白质），
存入 SQLite 数据库，再通过 Flask + Apache ECharts 制作成本地可视化展示网站。

网站共 5 个主要页面：首页（主页）、钙+脂肪/磷、蛋白质、饮食推荐&禁忌、科普，
各页面间支持相互跳转；钙/脂肪/磷图表支持下载图片，蛋白质图表支持缩放。


## 目录结构

```
.
├── app.py                  # Flask 主程序（路由 + 数据库读取）
├── spiders/
│   ├── GZL/                # 钙/脂肪/磷爬虫，共 16 个（对应 16 类食材）
│   │   ├── spider_41_gu.py     # 谷类
│   │   ├── spider_42_shu.py    # 薯类淀粉
│   │   └── ...                 # 编号 41~416，与 app.py 中 Cal42()~Cal417() 对应
│   └── protein/            # 蛋白质爬虫，共 5 个（优质蛋白质来源）
│       ├── spider_03_gandou.py # 干豆类
│       └── ...                 # 编号 03/08/09/010/011，与 app.py 中 ProXX() 对应
└── templates/              # Flask 模板（网页）
    ├── index.html          # 主页
    ├── Cal.html            # 钙+脂肪/磷 页面（18 类食材卡片 + 16 组折线图）
    ├── Pro.html            # 蛋白质 页面（5 组柱状图，支持缩放）
    ├── Phos.html           # 饮食推荐 & 禁忌 页面
    ├── Synth.html          # 【科普】页面
    └── Fat.html            # 占位页（见文末说明）
```

## 运行方法

1. 准备依赖（Python 3）：

   ```bash
   pip install flask beautifulsoup4
   ```

   （爬虫另需 `urllib`、`re`、`sqlite3`，均为标准库。）

2. 爬取数据：进入 `spiders/GZL/` 或 `spiders/protein/`，先将目标文件中的
   `目标网页链接` 与 `页数` 替换为实际值，再运行，例如：

   ```bash
   python spiders/GZL/spider_41_gu.py
   ```

   每个爬虫会在**当前运行目录**生成对应的 `.db` 数据库文件，请把它们放到
   `app.py` 同级目录（或修改 `app.py` 中的路径）。

3. 启动网站：

   ```bash
   python app.py
   ```

   浏览器访问 http://127.0.0.1:5000/

## 静态资源（论文PDF 中，需自行补齐）

网页主体使用的是开源 web 模板（FREEHTML5.CO），以下文件不在本仓库中：

- `static/css/*`、`static/js/*`、`static/images/*`（模板自带资源）
- `static/js/echarts.min.js`（Apache ECharts，<https://echarts.apache.org/>）
- `index.html` 头部引用的是 `echarts.min.js`（相对模板目录的根路径），
  其余页面引用 `static/js/echarts.min.js`，按实际存放位置保持引用一致即可

## 爬虫编号对照表

### 钙/脂肪/磷（spiders/GZL/，表 Gdbz：name, scoreG, scoreZ, scoreL）

| 编号 | 类别 | 数据库文件 | app.py 函数 |
|---|---|---|---|
| 41 | 谷类 | Gu_GZL.db | `Cal()` 内直接读取 |
| 42 | 薯类淀粉 | Shu_GZL.db | `Cal42()` |
| 43 | 干豆类 | GanDou_GZL.db | `Cal43()` |
| 44 | 蔬菜类 | ShuCai_GZL.db | `Cal44()` |
| 45 | 菌藻类 | JunZao_GZL.db | `Cal45()` |
| 46 | 水果类 | ShuiGuo_GZL.db | `Cal46()` |
| 47 | 坚果种子 | JianGuo_GZL.db | `Cal47()` |
| 48 | 畜肉类 | Chu_GZL.db | `Cal48()` |
| 49 | 禽肉类 | Qin_GZL.db | `Cal49()` |
| 410 | 乳类 | Ru_GZL.db | `Cal410()` |
| 411 | 蛋类 | Dan_GZL.db | `Cal411()` |
| 412 | 速食食品 | SuShi_GZL.db | `Cal412()` |
| 413 | 软饮料 | Ruan_GZL.db | `Cal413()` |
| 414 | 酒精饮料 | Jiu_GZL.db | `Cal414()`（页面不做展示） |
| 415 | 糖蜜饯类 | Tang_GZL.db | `Cal415()` |
| 416 | 油脂类 | You_GZL.db | `Cal416()` |
| — | 调味品类 | Tiao_GZL.db | `Cal417()`（待核对：论文附录 1 未列出该类爬取） |

### 蛋白质（spiders/protein/，表 Gdbz：name, score）

| 编号 | 类别 | 数据库文件 | app.py 函数 |
|---|---|---|---|
| 03 | 干豆类 | GanDou_Dn.db | `Pro03()` |
| 010 | 乳类 | Ru_Dn.db | `Pro010()` |
| 08 | 禽肉类 | Qin_Dn.db | `Pro08()` |
| 09 | 畜肉类 | Chu_Dn.db | `Pro09()` |
| 011 | 蛋类 | Dan_Dn.db | `Pro011()` |
| — | 汇总 | YingYang.db | `Pro()` 内直接读取 |

## 待核对清单（论文PDF 中“···”省略）

1. **每个爬虫文件**中的 `目标网页链接`、`页数` 为占位符，需按目标网站实际填写；
   数据库文件名（ `Gu_GZL.db`、`YingYang.db` 为论文原文）。
2. **Cal.html**：第 2~17 张分类卡片的描述文字为补写；PDF 未给出第 17 类食材的
   名称（原文仅有第 1 与第 18 张卡片），卡片 17 留了占位。第 2~16 组图表按第 1 组
   「谷类」的模板补写，DOM id / 变量名按编号递进。
3. **Pro.html**：`YingYang.db` 总览图一组为补写（`Pro()` 传递的 `name/score`
   在省略部分使用）；第 2~5 组图表按「干豆类」模板补写。
4. **Phos.html**：黄豆猪骨汤、猪皮汤、当归羊肉汤、猪血瘦肉豆腐汤、黄豆核桃鸡、
   鲤鱼汤、乌豆猪骨汤共 7 个菜谱的做法为补写（「桑葚牛骨汤」为原文）。
5. **Synth.html**：「二、高发人群」「三、危害」「四、为何推荐食疗预防」
   「五、维生素D」四节正文为补写（「一、产生原因」为原文）。
6. **Fat.html**：整页为占位。
