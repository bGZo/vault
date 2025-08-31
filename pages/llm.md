---
title: Large Language Models
aliases:
  - Large Language Models
created: 2024-03-30T21:55:30
modified: 2025-02-03T11:21:21
description: LLMs are language models with many parameters, and are trained with self-supervised learning on a vast amount of text.
tags:
  - ai
  - nlp
wikipedia: https://en.wikipedia.org/wiki/Large_language_model
---

## Why

## How

### Train

- Data Collection
- Training
- Evaluation

## What

- an advanced Artificial Intelligence models
    - designed for understanding and generating human language.
- based on deep learning architectures
    - such as Transformers
- trained on massive amounts of text data from various sources
    - acquire a deep understanding of the nuances (细微差距) and complexities of language.
- have the ability to achieve state-of-the-art (最先进) performance in multiple Natural Language Processing (NLP) tasks
    - such as machine translation, sentiment (情绪) analysis, summarization, and more.
    - They can also generate coherent (连贯一致的) and contextually relevant text based on given input, making them highly useful for applications like chatbots, question-answering systems, and content generation.

### Types

#### Base LLMs

- designed to predict the next word based on the training data.
    - not designed to answer questions

#### Instruction tuned (指令调优) LLMs

```
Instruction Tuned LLMs = Base LLMs + Further Tuning + RLHF
```

- **Further Tuning**: trained using a large dataset covering sample “Instructions” and how the model should perform as a result of those instructions.
- Reinforcement Learning (强化学习) with Human Feedback (RLHF)

### History
- 2012：神经网络
- 2017：[[attention|注意力]] 机制 —> 改进 SEQ2SEQ
- 2018：GPT-1
- 2019：GPT-2
- 2020：GPT-3
- 2022：chatGPT
- 2023：GPT-4
- 2024：OpenAI O1

## Vocabulary

- [[machine-learning|ML]]
- [[natural-language-processing|NLP]]
- MLM：Masked language model.
- Label
- Label Space
- Label Distribution
- Sentiment Analysis
- Verbalizer
- Reinforcement Learning from Human Feedback (RLHF)

## References

- https://roadmap.sh/prompt-engineering?fl=1

![https://roadmap.sh/guides/introduction-to-llms](https://roadmap.sh/guides/llms.png)
