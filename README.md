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

#### 1️⃣ 字词理解（Word-level Understanding）
解释古诗词中**词语或短语的含义**  
- 题型：问答题

#### 2️⃣ 诗句理解（Sentence-level Understanding）
解释整句诗的语义及表达内容  
- 题型：问答题

#### 3️⃣ 情感理解（Emotion Recognition）
判断诗人通过诗句表达的情感倾向  
- 题型：选择题

Task 1、2、3（理解）
提交为 task1.json，格式见上届

#### 4️⃣ 典故识别（Allusion Identification）
识别诗句中的典故，并进行解释  

📌 **数据示例：**
```json
{
    "que": "北斗七星高，哥舒夜带刀。"
}
```
📌 提交格式（task2.json）：
0 代表不含典故，1代表包含典故，不包含典故默认不会进行answer对比
```json
{
    "flag": 1
    "answer": "哥舒：指哥舒翰，是唐玄宗时期的名将，突厥族哥舒部后裔。此处借其威名表现边塞紧张局势。"
}
```

🔍 Task 2：古诗词推理

该任务侧重考察模型的高阶推理能力与语义关联能力，包含两个子任务：

1️⃣ 古诗词类比（Analogy Reasoning）

从诗句中抽取隐含关系或语义对应，完成类比推理或填空。
📌 示例：
```json
{
    "que": "杜甫的《客至》中，从“____________，____________”两句中能够感受到主人竭诚尽意的盛情和力不从心的歉疚。"
}
```
📌 提交格式（task3.json）：
```json
{
    "answer": [
        "盘飧市远无兼味",
        "樽酒家贫只旧醅"
    ]
}
```
👉 注：答案不严格匹配标点符号
2️⃣ 古诗词辨析（Critical Analysis）

根据诗词内容与语境，对多个选项进行分析，选择最合理或不正确的一项。

📌 示例输入：
```json
{
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
📌 提交格式（task4.json）：
```json
{
    "answer": "A"
}
```








## 📈 评价指标
| 指标 / 任务 | 字词理解 | 诗句理解 | 情感理解 | 典故识别 | 古诗词类比 | 古诗词辨析 |
|------------|------------------|------------------|------------------|----------|------------|------------|
| BLEU       | ✅               | ✅               | ❌               | ❌       | ❌         | ❌         |
| BERTScore  | ✅               | ✅               | ❌               | ✅       | ❌         | ❌         |
| LLM语义评估 | ✅               | ✅               | ❌               | ❌       | ❌         | ❌         |
| Accuracy   | ❌               | ❌               | ✅ (选择题)               | ✅ (flag)       | ✅ (填空题)         | ✅ (选择题)        |

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

<img src="https://github.com/HITICI-NLPGroup/CCPA-EvalTask/blob/main/%E5%BE%AE%E4%BF%A1%E4%BA%A4%E6%B5%81%E7%BE%A4.jpg" width="30%"  alt="微信交流群" align="center"/>


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

