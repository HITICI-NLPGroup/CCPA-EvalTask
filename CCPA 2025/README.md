# CCL-2025-Chinese-Poetry-Understanding-and-Reasoning-Evaluation-Task
第一届古诗词理解和推理评测任务
**见阿里云天池 CCL25-Eval 任务5：第一届中文古诗词赏析评测**
<br>
**阿里云天池有永久钉钉群**
## 任务奖项
本届评测将设置一、二、三等奖，提供总额为6000元的奖金。所有奖金将在公布奖项后10个工作日内发布。

## 任务简介

古诗词理解和推理评测任务旨在测试自然语言模型对古诗词的内容、情感理解与推理能力。古诗词具有高度的凝练性和语言的音乐美，不仅需要掌握古诗的语言特色，还需要结合历史、文化背景的知识，从而进行综合性的推理与理解。

本次评测任务分为两个主要部分：
1. **古诗词理解**  
   包括古诗词短语内容理解与古诗词句子理解。
   
2. **古诗词推理**  
   针对古诗词表达的情感进行推理，判断诗人所表达的情感。

## 评测任务描述

### 1. 古诗词理解

- **任务a：古诗词短语内容理解**  
  给定古诗词的内容，回答其中每个词语的释义。

- **任务b：古诗词句子理解**  
  给定古诗词的内容，提供对应诗句的白话文译文。

### 2. 古诗词推理

- **情感推理**  
  根据古诗词内容，推理出诗人在诗中所表达的情感。给定多个选项，选择最符合古诗情感的选项。

## 数据集说明
古诗词理解和推理评测任务是一个few-shot的任务，包含了古诗、唐诗和宋词，拥有五言绝句、七言绝句、五言律诗和七言律诗等形式的古诗词。评测提供了200条数据用于训练，400条数据用来验证、测试。所有数据均以 JSON 格式提供。每条数据包括以下字段：

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

### 示例数据格式

#### 训练数据集：

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
#### 测试数据集：

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
## 提交结果格式

**提交的结果应为 `result.json` 文件，格式如下：**
请将结果提交到23S151077@stu.hit.edu.cn，命名格式为ccl-队名-test.json
建议英文队名
```json
{
    "ans_qa_words": {"泊": "", "商女": "", "后庭花": ""},
    "ans_qa_sents": {"烟笼寒水月笼沙": "", "夜泊秦淮近酒家": ""},
    "choose_id": "A"
}
```
##  评价指标

对于古诗词理解任务，评测任务采用BLEU值、 中文BertScore分数和大语言模型作为评估指标。对于古诗词推理任务，根据选择题准确率计算得分。

## 评测赛程

| 时间               | 事项                              |
|--------------------|-----------------------------------|
| 2 月 1 日 - 3 月 15 日 | 开放报名                          |
| 3 月 1 日           | 发布训练集          |
| 4 月 1 日           | 发布无答案验证集                   |
| 5 月 10 日          | 发布无答案的测试集，开始提交测试集结果 |
| 5 月 28 日          | 结果提交截止                       |
| 5 月 31 日          | 公布成绩和排名                     |
| 6 月 15 日          | 提交最终版本的模型及评测论文        |
| 7 月 1 日           | 评测论文审稿及录用通知              |
| 7 月 25 日 - 28 日  | 评测研讨会  
## BibTeX
```
@article{devlin2018bert,
  title={Bert: Pre-training of deep bidirectional transformers for language understanding},
  author={Devlin, Jacob},
  journal={arXiv preprint arXiv:1810.04805},
  year={2018}
}
```
如果你对我们的工作感兴趣，欢迎查看我们的工作
```
@article{chen2024benchmarking,
  title={Benchmarking llms for translating classical chinese poetry: Evaluating adequacy, fluency, and elegance},
  author={Chen, Andong and Lou, Lianzhang and Chen, Kehai and Bai, Xuefeng and Xiang, Yang and Yang, Muyun and Zhao, Tiejun and Zhang, Min},
  journal={arXiv preprint arXiv:2408.09945},
  year={2024}
}
```
## 任务联系人
裴振武 
联系方式：（哈尔滨工业大学（深圳），23S151077@stu.hit.edu.cn）

