<h1 align="center">Chinese Poetry Understanding and Reasoning Evaluation Task (CCL 2026)</h1>

<h1 align="center">第二届古诗词理解和推理评测任务（CCL 2026）</h1>

<p align="center">
  <img src="https://img.shields.io/badge/CCL-2026-blue" />
  <img src="https://img.shields.io/badge/Task-Poetry%20Understanding%20%26%20Reasoning-green" />
  <img src="https://img.shields.io/badge/Language-Chinese-red" />
  <img src="https://img.shields.io/badge/Evaluation-BLEU%20%7C%20BERTScore%20%7C%20LLM-yellow" />
  <img src="https://img.shields.io/badge/Status-Active-brightgreen" />
</p>

---

## 🧩 任务简介

中文古诗词具有高度凝练性和语言的音乐美，讲究对仗、平仄和押韵。为了准确理解古诗的语义，不仅需要掌握古诗的语言特色，还需要调动对历史、文化背景的知识，结合对古诗中所描绘的自然景象和人物情感的认知，从而进行综合性的推理与理解。

为了进一步衡量模型在中文古诗词赏析场景中的语言理解深度与文化推理能力，我们推出第二届中文古诗词赏析评测。在第一届的基础上，本届评测进一步聚焦模型的**深度理解与复杂推理能力**，引入更具挑战性的高级任务，以全面考察模型对古诗词文化内涵与高层语义结构的掌握程度。
具体任务设置如下：

### 🔍 Task：古诗词理解

#### 1️⃣ 字词理解（Word-level Understanding）
解释古诗词中**词语或短语的含义**  
- 题型：问答题

#### 2️⃣ 诗句理解（Sentence-level Understanding）
解释整句诗的语义及表达内容  
- 题型：问答题

#### 3️⃣ 情感理解（Emotion Recognition）
判断诗人通过诗句表达的情感倾向  
- 题型：选择题

Task 1️⃣、2️⃣、3️⃣ 提交为 task1。评测提供了164条数据用于训练，327条数据用来验证、测试。所有数据均以 JSON 格式提供。每条数据包括以下字段：
- `title`：古诗词题目
- `author`：古诗词作者
- `content`：古诗词内容
- `keywords`：古诗词的关键词及其释义
- `trans`：古诗词的白话文译文
- `emotion`：古诗词的情感表达
- `qa_words`：需要回答的关键词
- `qa_sents`：需要回答的句子
- `choose`：情感选项
- `ans_qa_words`：回答关键词的结果
- `ans_qa_sents`：回答句子的结果
- `choose_id`：选择的情感选项的下标

📌 **训练数据示例：**

```json
{
    "title": "泊秦淮",
    "author": "杜牧",
    "content": "烟笼寒水月笼沙，夜泊秦淮近酒家。商女不知亡国恨，隔江犹唱后庭花。",
    "keywords": {
        "泊": "停泊",
        "商女": "歌女",
        "后庭花": "歌曲《玉树后庭花》的简称"
    },
    "trans": "迷离的月色下，轻烟笼罩寒水、白沙，夜晚船只停泊在秦淮边靠近岸上的酒家。卖唱的歌女好似不懂什么叫亡国之恨，隔着江水仍然高唱着《玉树后庭花》。",
    "emotion": "爱国"
}
```
📌 **测试数据示例：**

```json
{
    "title": "泊秦淮",
    "author": "杜牧",
    "content": "烟笼寒水月笼沙，夜泊秦淮近酒家。商女不知亡国恨，隔江犹唱后庭花。",
    "qa_words": ["泊", "商女", "后庭花"],
    "qa_sents": ["烟笼寒水月笼沙", "夜泊秦淮近酒家"],
    "choose": ["A":"爱国", "B":"庆祝", "C":"闲适", "D":"赞美"],
}
```
📌 **提交格式**（task1）：
```json
{
    "ans_qa_words": {"泊": "", "商女": "", "后庭花": ""},
    "ans_qa_sents": {"烟笼寒水月笼沙": "", "夜泊秦淮近酒家": ""},
    "choose_id": "A"
}
```

#### 4️⃣ 典故识别（Allusion Identification）
识别诗句中的典故，并进行解释。评测提供了20条数据用于训练，125条数据用来验证、测试。所有数据均以 JSON 格式提供。

📌 **训练数据示例：**（训练数据均包含典故）：
```json
{
    "que": "欲得周郎顾，时时误拂弦。",
    "answer": "周郎：指三国时吴将周瑜。他二十四岁为大将，时人称其为“周郎”。他精通音乐，听人奏错曲时，即使喝得半醉，也会转过头看一下奏者。当时人称：“曲有误，周郎顾。”"
},
```

📌 **测试数据示例：**
```json
{
    "idx": 1,
    "que": "北斗七星高，哥舒夜带刀。"
}
```
📌 **提交格式**（task2）：
flag为 0 代表不含典故，1代表包含典故，不包含典故默认不会进行answer对比
```json
{
    "idx": 1,
    "flag": 1,
    "answer": "哥舒：指哥舒翰，是唐玄宗时期的名将，突厥族哥舒部后裔。此处借其威名表现边塞紧张局势。"
}
```

### 🔍 Task：古诗词推理

该任务侧重考察模型的高阶推理能力与语义关联能力，包含两个子任务：

#### 1️⃣ 古诗词类比（Analogy Reasoning）

从诗句中抽取隐含关系或语义对应，完成类比推理或填空。

📌 **训练数据示例：**
```json
{
    "que": "《烛之武退秦师》中，烛之武面对秦伯，开门见山，表明自己对国家命运的认识：“秦、晋围郑，__________。__________，敢以烦执事。”有效消除了秦伯的戒备。",
    "answer": [
        "郑既知亡矣",
        "若亡郑而有益于君"
    ]
}
```

📌 **测试数据示例：**
```json
{
    "idx": 1,
    "que": "杜甫的《客至》中，从“____________，____________”两句中能够感受到主人竭诚尽意的盛情和力不从心的歉疚。"
}
```
📌 **提交格式**（task3）：
```json
{
    "idx": 1,
    "answer": [
        "盘飧市远无兼味",
        "樽酒家贫只旧醅"
    ]
}
```

#### 2️⃣ 古诗词辨析（Critical Analysis）

根据诗词内容与语境，对多个选项进行分析，选择最合理或不正确的一项。

📌 **训练数据示例：**
```json
{
    "title": "路芳行·送子权桂藤",
    "author": "朱敦儒",
    "content": "花溪藤江，草衍鸳鸯。\n锦帆兰舟分去。二阕元是一溪云，暂为山北山南雨。\n绿酒多对，白须休颓。飞丹约定烟霞路。与君先占赤城春，回棹早惭桃源路。\n\n【注】①鸳鸯: 鸳鸯草。②观: 览，看。",
    "zhushi": [
        "① 鸳鸯: 鸳鸯草。",
        "② 观: 览，看。"
    ],
    "questions": [
        {
            "que": "下列对这首词的理解和赏析，不正确的一项是（  ）",
            "type": "选择题",
            "options": {
                "A": "开篇两句描绘春暖花开、水涨藤江、芳草鲜美的景象，富有审美意趣。",
                "B": "友人乘舟远行，也将走眼前的春光，以春之分写人之别，造语十分奇妙。",
                "C": "词人将自己与友人合称“二翁”，并以溪云为喻，写出二人漂泊无依的悲哀。",
                "D": "“赤城”桃源运用典故，含蓄写出了词人对神仙府邸、世外桃源的向往。"
            },
            "answer": "C"
        }
    ]
}
```

📌 **测试数据示例：**
```json
{
    "idx": 1,
    "title": "元珍",
    "author": "欧阳修",
    "content": "燕条鸡头乱山中，时节煎熬已乍穷。\n游女羞鬟风俗古，野狐歌舞岁年丰。\n平时都巴为难，故国江山最雄。\n莉瑶先贺多胜，酒问酒问何须穷。",
    "questions": [
        {
            "que": "下列对这首诗的理解和赏析，不正确的一项是？",
            "type": "选择题",
            "options": {
                "A": "首联提题，上句描写山景况",
                "B": "颈联承接上联，描绘当地习俗",
                "C": "颈联运用对比，体现情感转变",
                "D": "尾联叙事，情感与《客至》不同"
            }
        }
    ]
}
```
📌 **提交格式**（task4）：
```json
{
    "idx": 1,
    "answer": "A"
}
```

## 🎯最终提交格式：
最终提交一个JSON文件，格式如下：
```json
{
    "task1": [
        {
            "idx": 0,
            "ans_qa_words": {
                "衰草": "xxx",
                "故关": "xxx",
                "风尘": "xxx"
            },
            "ans_qa_sents": {
                "xxx",
                "xxx"
            },
            "choose_id": "xxx"
        },
        ...
    ]
    "task2": [
        {
            "idx": 0,
            "flag": 1/0,
            "answer": "xxx"
        },
        ...
    ]
    "task3": [
        {
            "idx": 0,
            "answer": [
                "xxx",
                "xxx"
            ]
        },
        ...
    ]
    "task4": [
        {
            "idx": 0,
            "answer": "xxx"
        },
        ...
    ]
}
```


## 📈 评价指标
| 指标 / 任务 | 字词理解 | 诗句理解 | 情感理解 | 典故识别 | 古诗词类比 | 古诗词辨析 |
|------------|------------------|------------------|------------------|----------|------------|------------|
| BLEU       | ✅               | ✅               | ❌               | ❌       | ❌         | ❌         |
| BERTScore  | ✅               | ✅               | ❌               | ✅       | ❌         | ❌         |
| Accuracy   | ❌               | ❌               | ✅ (选择题)               | ✅ (flag)       | ✅ (填空题)         | ✅ (选择题)        |

**字词理解分数** = (BLEU + BERTScore) / 2，**诗句理解分数** = (BLEU + BERTScore) / 2，**情感理解分数** = Accuracy，**典故识别分数** = (flag_Accuracy + BERTScore) / 2，**古诗词类比分数** = Accuracy，**古诗词辨析分数** = Accuracy。

最终得分为各项任务得分的加权和。即：
```
Score = (Task1_score + Task2_score + Task3_score + Task4_score) / 4
```
其中，Task1_score =（ 字词理解分数 + 诗句理解分数 + 情感理解分数 ）/ 3，Task2_score  = 典故识别分数，Task3_score = 古诗词类比分数，Task4_score = 古诗词辨析分数。

---

## 📅 日程安排
即将发布

---

## 🏆 奖项设置

- 🥇 一等奖（1名）：3000元
- 🥈 二等奖（1名）：2000元
- 🥉 三等奖（1名）：1000元
  
所有奖金将在公布奖项后10个工作日内发布。

---

## 📬 组织者和联系人

- **评测组织者**：白雪峰、陈科海（哈尔滨工业大学（深圳））
- **任务联系人**：朱颖杰、裴振武 （哈尔滨工业大学（深圳），zhuyj@stu.hit.edu.cn）

---

## 💬 微信交流群

欢迎各位参赛同学加入微信交流群

<img src="https://github.com/HITICI-NLPGroup/CCPA-EvalTask/blob/main/%E5%BE%AE%E4%BF%A1%E4%BA%A4%E6%B5%81%E7%BE%A4.png" width="30%"  alt="微信交流群" align="center"/>


---

## 📖 参考文献

如果您对我们的工作感兴趣，欢迎查看我们的工作
```
@inproceedings{pei2025tianwen,
  title={TianWen: A Comprehensive Benchmark for Evaluating LLMs in Chinese Classical Poetry Understanding and Reasoning},
  author={Pei, Zhenwu and Chen, Rongbo and Bai, Xuefeng and Chen, Kehai and Zhu, Yingjie and Chen, Andong and Zhang, Min},
  booktitle={CCF International Conference on Natural Language Processing and Chinese Computing},
  pages={516--528},
  year={2025}
}
```

