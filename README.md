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

- **任务一：古诗词理解：**
  - **古诗词字词理解**：解释古诗词中短语级别的语义。本子任务通过问答题的形式对待测系统进行评估。
  - **古诗词诗句理解**：解释古诗词中诗句级别的语义。本子任务通过问答题的形式对待测系统进行评估。
  - **古诗词情感理解**：推断诗人透过作品所传达的情感。本子任务通过选择题的形式对待测系统进行评估。
  - **典故识别**：判断诗句中是否包含典故并进行解释。本子任务通过问答题的形式对待测系统进行评估。

- **任务二：古诗词推理：**
  - **古诗词类比**：发现古诗词中不同事物之间的相同关系，意象的关联。本子任务通过问答题的形式对待测系统进行评估。
  - **古诗词辨析**：依据诗词内容与语境，对给定选项进行辨析，判断其中表述最为合理的一项。本子任务通过选择题的形式对待测系统进行评估。

---

## 📊 数据格式说明
即将发布

---

## 📦 提交格式
即将发布

---

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

