# bloom-taxonomy-lm-analysis [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

This repository contains code and data for evaluating small and large language models (SLMs & LLMs) on the task of generating educational questions aligned with Bloom's Taxonomy. The evaluation considers semantic similarity, prompt complexity, and readability etc across multiple Bloom levels and topics.

## Project Overview
- **Goal:** Evaluate Bloom's Taxonomy-aligned questions using LLMs and SLMs, assessing their capabilities and performance across key quality metrics.
- **Models:** 
  - **LLMs:** GPT-3.5, GPT-4, Mistral, LLaMA and PaLM 2.
  - **SLMs:** Deepseek R1, Gemma 3, Granite 4, Phi 4, Phi 4 mini, GPT-OSS, Mistral Small 3.2 and LLaMA 3.2 (smaller variants).

  Additional parameter and configuration available [here](Supplementary_Tables_and_Figures/Model_config.md)

- **Prompts:** 5 [Prompt Structures (PS)](Prompts/) per topic
- **Topics**: 17 Machine Learning and Data Science topic, available [here](Supplementary_Tables_and_Figures/Topics.png)
- **Metrics:**
  - Prompt-Question Similarity
  - Grade Level
  - Readability
  - Semantic evaluation (e.g., BERTScore)
  - Pedagogical Alignment (w/ Verb Check)
  - Model-as-a-Judge

## Directory and File Overview
* **Code/** — Helper python scripts and jupyter notebooks utilized for preprocessing, experimentation and analysis
* **Evaluation/** — Results for Model-as-a-Judge analysis along with its evaluation metrics.
* **Generation/** — Results for assessing question generative capabilites of SLMs and LLMs along with its evaluation metrics.
* **Licenses/** — Licenses for the repository
* **Prompts/** — Prompt templates used to generate responses from language models in experimentaion.
* **Supplementary_Tables_and_Figures/** — Supplementary materials for additional information on study and analysis performed.
* `README.md` — Readme file for the repository

## License
 - This repository is licensed under the [MIT License](Licenses/LICENSE).  
 - Portions of the data are reused under compatible MIT licensing from third-party sources.

## Attributions
This project includes data adapted from work by [Nicy Scaria](https://github.com/nicyscaria/AEQG_Blooms_Evaluation_LLMs), licensed under the [MIT License](Licenses/LICENSE.nicy_scaria).
