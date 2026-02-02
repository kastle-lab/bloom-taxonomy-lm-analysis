## Model Configuration
We group models into **Large Language Models (LLMs)** and **Small Language Models (SLMs)**, and distinguish between
their roles as **generators** (question generation) and **evaluators** (model-as-a-judge).

Unless otherwise noted:
- **Generation temperature:** `0.8`  
- **Evaluation temperature:** `0.0`  
- **Max tokens per completion:** `no limit` (sufficient to cover a full question + brief rationale when applicable)  
- **Frequency / presence penalties:** `0.0`  

These defaults are consistent across models to support comparability with the study reported in the paper.

---

### 1. Large Language Models (LLMs)

#### 1.1 GPT-4 (`G4`)
- **Provider:** OpenAI
- **Primary usage:** Question generation across all Bloom levels and prompt structures (PS1–PS5)

#### 1.2 GPT-3.5 (`G3.5`)
- **Provider:** OpenAI
- **Primary usage:** Question generation across all Bloom levels and prompt structures (PS1–PS5)

#### 1.3 PaLM-2 (`P2`)
- **Provider:** Google
- **Primary usage:** Question generation across all Bloom levels and prompt structures (PS1–PS5)

#### 1.4 LLaMA-2 (`L2`)
- **Provider:** Meta
- **Size:** 70B
- **Primary usage:** Question generation across all Bloom levels and prompt structures (PS1–PS5)

#### 1.5 Mistral 7B (`M`)
- **Provider:** Mistral
- **Size:** 7B
- **Primary usage:** Question generation across all Bloom levels and prompt structures (PS1–PS5)

#### 1.6 Gemini Pro (`GP`)
- **Provider:** Google
- **Primary usage:** Model-as-a-judge / rubric-based evaluator for question quality and skill-match

---

### 2. Small Language Models (SLMs)

SLMs were selected for being **lightweight, open-weight, or locally deployable**, while still offering strong instruction.

#### 2.1 Granite 4 (`Gr4`)
- **Provider:** IBM
- **Size:** 3.4B
- **Primary usage:** Question generation + model-as-a-judge evaluator

#### 2.3 Phi-4 mini (`P4m`)
- **Provider:** Microsoft
- **Size:** 3.84B
- **Primary usage:** Question generation + model-as-a-judge evaluator

#### 2.4 LLaMA 3.2 (`L3.2`)
- **Provider:** Meta
- **Size:** 3.21B
- **Primary usage:** Question generation + model-as-a-judge evaluator

#### 2.4 Mistral Small 3.2 (`MS`)
- **Provider:** Mistral
- **Size:** 24B
- **Primary usage:** Question generation + model-as-a-judge evaluator

#### 2.5 GPT-OSS (`GO`)
- **Provider:** OpenAI (open-weights / “OSS” configuration)
- **Size:** 20.9B
- **Primary usage:** Question generation + model-as-a-judge evaluator

#### 2.2 Phi-4 (`P4`)
- **Provider:** Microsoft
- **Size:** 14.7B
- **Primary usage:** Question generation + model-as-a-judge evaluator

#### 2.6 Deepseek R1 (`D1`)
- **Provider:** Deepseek
- **Size:** 14B
- **Primary usage:** Question generation + model-as-a-judge evaluator

#### 2.7 Gemma 3 (`Ge3`)
- **Provider:** Google
- **Size:** 4.3B
- **Primary usage:** Question generation + model-as-a-judge evaluator

---

##### Reproducibility Notes: 
Randomness is controlled only via the **model temperature** (no per-call sampling seed is enforced at the API level). All comparative analyses in the paper assume the default configuration listed above; any deviations (e.g. ablation runs) are explicitly called out in the corresponding notebooks or scripts.
