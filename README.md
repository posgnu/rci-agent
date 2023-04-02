# RCI Agent for MiniWoB++
Welcome to the codebase for our paper, "Language Models can Solve Computer Tasks". In this codebase, you will find the implementation of our RCI agent, which uses a pre-trained language model to execute computer tasks in [MiniWoB++ benchmark](http://miniwob.farama.org/) guided by natural language. The agent employs a simple RCI prompting scheme that allows it to improve its outputs.

![overview](./artifacts/overview.gif)

[[Website]](https://posgnu.github.io/rci-web/)
[[Arxiv Paper]](https://arxiv.org/abs/2303.17491v1)
[[PDF]](https://arxiv.org/pdf/2303.17491v1.pdf)


## Dependencies
The RCI agent is implemented in Python 3.9 and requires the following dependencies:

* gym
* openai
* selenium
* Pillow
* regex

```sh
pip install -r requirements.txt
```

## Usage

### Setup
To run the code, you must first install MiniWoB++ and configure your OpenAI API key. MiniWoB++ is integrated with the OpenAI Gym environment. Navigate to the `computergym` directory and execute the following command to install it:
```sh
cd computergym
pip install -e .
```
Once that's done, you need to write your OpenAI API key in the `example_config.json` file, then rename the file to `config.json`

### Run
To run the code, simply execute the following command:
```sh
python main.py --env [TASK NAME] --llm [LLM NAME] --num-episodes [NUM EPISODES] --erci [NUM Explicit RCI] --irci [NUM Implicit RCI] --sgrounding
```
Here are the arguments you need to specify:
* `--env`: MiniWoB++ task name
* `--llm`: the name of language model. model name and the corresponding API name is specified below.
    * `chatgpt`: "gpt-3.5-turbo"
    * `davinci`: "text-davinci-003"
    * `ada`: "ada"
    * `babbage`: "babbage" 
    * `curie`: "curie"
    * `davinci1`: "davinci"
    * `davinci2`: "text-davinci-002"

* `--env`: Name of the MiniWoB++ task you want to run. You can see the list of available tasks in `available_tasks.txt`
* `--llm`: Name of the language model you want to use. The model name and corresponding API name are specified below:
    * chatgpt: "gpt-3.5-turbo"
    * davinci: "text-davinci-003"
    * ada: "ada"
    * babbage: "babbage"
    * curie: "curie"
    * davinci1: "davinci"
    * davinci2: "text-davinci-002"
* `--num-episodes`: Number of episodes to run the task
* `--erci`: The number of explicit RCI loop for an action plan. `-1` will remove the action plan sampling.
* `--irci`: The number of implicit RCI loop for the agent grounding.
* `--sgrounding`: If this is True, then the state grounding update is enabled.
* `--headless`: If this is True, then the MiniWoB++ environment will run in headless mode.

Consider running the following command to verify if everything is functioning correctly:
```sh
python main.py --env choose-list --llm chatgpt --num-episodes 1 --irci 1 --sgrounding
```

## Evaluation
Our project's approach has yielded impressive results, with our agent achieving the second-highest score out of all tested models. We have observed that our agent outperforms the baselines, with the exception of CC-Net (SL + RL), which uses dictionary-based typing actions.

![](/artifacts/baseline-1.png)

What sets our RCI agent apart is that it accomplished this feat using 120 times fewer samples than WebN-T5-3B and 11,000 times fewer samples than CC-Net. Obtaining expert demonstrations and defining reward functions for computer tasks can be a daunting challenge, but our research highlights the potential of using LLMs to overcome these obstacles and achieve success in general computer tasks.

![](/artifacts/demos-1.png)

## Check out our paper! 

Our paper is available on [Arxiv](https://arxiv.org/abs/2303.17491v1). If you use this code in your research, we kindly ask that you cite our paper.

```bibtex
@article{kim2023language,
      title={Language Models can Solve Computer Tasks}, 
      author={Geunwoo Kim and Pierre Baldi and Stephen McAleer},
      journal={arXiv preprint arXiv:2303.17491},
      year={2023},
}
```