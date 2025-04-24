# GenAI for Software Development (Prompt Engineering for In Context Learning)

* [1 Introduction](#1-introduction)  
* [2 Getting Started](#2-getting-started)  
  * [2.1 Preparations](#21-preparations)  
  * [2.2 Install Packages](#22-install-packages)  
  * [2.3 Run the prompt engineering model](#23-run-the-fine-tuning-model)  
* [3 Report](#3-report)  

---

# **1. Introduction**  
**Prompt Engineering for In-Context Learning** explores how different prompt designs influence **Large Language Models** (LLMs) in solving diverse software engineering tasks. In this assignment, we applied five strategies—**zero-shot**, **few-shot**, **chain-of-thought**, **prompt-chaining**, and **BLEU-based self-consistency**—to 22 problems ranging from code summarization and bug fixing to API generation and code translation. Our experiments compare four models—[gpt-4.1](https://github.com/marketplace/models/azure-openai/gpt-4-1/), [Codestral-2501](https://github.com/marketplace/models/azureml-mistral/Codestral-2501), [gpt-4.1-mini](https://github.com/marketplace/models/azure-openai/gpt-4-1-mini), and [gpt-4.1-nano](https://github.com/marketplace/models/azure-openai/gpt-4-1-nano), demonstrating how strategic prompt examples and structured reasoning affect code quality and clarity. The repetitions is set to `3` for self-consistency prompting, the temperature is set to `0.7`, and the token limit is `1024` for all tables.

---

# **2. Getting Started**  

This project is implemented in **Python 3.9+** and is compatible with **macOS, Linux, and Windows**.  

## **2.1 Preparations**  

(1) Clone the repository to your workspace:  
```shell
~ $ git clone https://github.com/theantigone/Prompt-Engineering-for-In-Context-Learning.git
```
(2) Navigate into the repository:
```shell
~ $ cd Prompt-Engineering-for-In-Context-Learning
~/Prompt-Engineering-for-In-Context-Learning $
```
(3) Set up a virtual environment and activate it:

For macOS/Linux:
```shell
~/Prompt-Engineering-for-In-Context-Learning $ python -m venv ./venv/
~/Prompt-Engineering-for-In-Context-Learning $ source venv/bin/activate
(venv) ~/Prompt-Engineering-for-In-Context-Learning $ 
```

For Windows:
```shell
~/Prompt-Engineering-for-In-Context-Learning $ python -m venv .\venv\
~/Prompt-Engineering-for-In-Context-Learning $ .\venv\bin\Activate.ps1
(venv) ~/Prompt-Engineering-for-In-Context-Learning $
```

To deactivate the virtual environment, use the command:
```shell
(venv) $ deactivate
```

## **2.2 Install Packages**

Install the required dependencies:
```shell
(venv) ~/Prompt-Engineering-for-In-Context-Learning $ pip install -r requirements.txt
```
## **2.3 Run the prompt engineering model**

(1) Run Prompt Engineering Demo

This script takes a list of problems that are already prompted by certain strategies and then runs each prompt based upon the models chosen. After the model is ran, then the script with the prompt, strategy uses, and output is all then logged in a csv that is created.

Navigate to the ```src``` directory, then run:
```shell
(venv) ~/Prompt-Engineering-for-In-Context-Learning/src $ python prompt-engineering.py
```

## 3. Report

The assignment report is available inside the ``reports`` folder named ``Assignment_Report.pdf``.



