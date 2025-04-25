# GenAI for Software Development (Prompt Engineering for In Context Learning)

* [1 Introduction](#1-introduction)  
* [2 Getting Started](#2-getting-started)  
  * [2.1 Preparations](#21-preparations)  
  * [2.2 Install Packages](#22-install-packages)  
  * [2.3 Run the prompt engineering model](#23-run-the-fine-tuning-model)  
* [3 Report](#3-report)  

---

# **1. Introduction**  
**Prompt Engineering for In-Context Learning** investigates the impact of different prompt designs on the performance of **Large Language Models** (LLMs) across a variety of software engineering tasks. 

In this assignment, five prompting strategies—*zero-shot*, *few-shot*, *chain-of-thought*, *prompt-chaining*, and *self-consistency*—were applied to 22 tasks, including code summarization, bug fixing, API generation, and code translation. 

Experiments compared four models—[gpt-4.1](https://github.com/marketplace/models/azure-openai/gpt-4-1/), [Codestral-2501](https://github.com/marketplace/models/azureml-mistral/Codestral-2501), [gpt-4.1-mini](https://github.com/marketplace/models/azure-openai/gpt-4-1-mini), and [gpt-4.1-nano](https://github.com/marketplace/models/azure-openai/gpt-4-1-nano)—to demonstrate how the strategic use of prompt examples and structured reasoning influences the quality and clarity of generated code. 

Self-consistency prompting employed `3` repetitions, with a temperature setting of `0.7` and a maximum token limit of `1024` tokens across all evaluations.

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

## **2.3 Enter your API key**

You will need to enter your GitHub **Personal Access Token** (PAT) key into the script to use the models. Create a `token.txt` file, and paste your API key inside that file.

## **2.4 Run the prompt engineering model**

(1) Run Prompt Engineering Demo

This script takes a list of problems that are already prompted by certain strategies and then runs each prompt based upon the models chosen. After the model is ran, multiple `.csv` files containing the prompts, code snippets, and outputs are created.

Navigate to the ```src``` directory, then run:
```shell
(venv) ~/Prompt-Engineering-for-In-Context-Learning/src $ python prompt-engineering.py
```

You can find the `.csv` files in the `data/interim/user_files` folder.

## 3. Report & Analysis

The assignment report is available inside the ``reports`` folder named ``Assignment_Report.pdf``.

You can also find the model comparisons and analyses inside ``reports`` folder named ``Assignment_Analysis.pdf``.


