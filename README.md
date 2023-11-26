# AutoGenExperiments

Repo for my AutoGen Experiments. AutoGen is a framework that enables development of LLM applications using multiple agents that can converse with each other to solve tasks.

## setup

Create a conda environment.

```
conda create -n pyautogen python=3.10 
conda activate pyautogen
```

Install AutoGen

```
pip install pyautogen
pip install "pyautogen[blendsearch]<0.2"
pip install "pyautogen[retrievechat]<0.2"
pip install "pyautogen[lmm]"
pip install "pyautogen[mathchat]<0.2"
```

Add your OpenAI Key

```
# replace with your key and ensure you have funds
export OPENAI_API_KEY=XXXXXXXXXXYYYYYYYYZZZZZZ 
```

To test your install, navigate to the simple directory and execute:

```
python quick_start.py
```
