import argparse
import random
import computergym
import gym
from llm_agent import LLMAgent
import logging

logging.basicConfig(level=logging.INFO)

def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument("--env", type=str, default="click-button")
    parser.add_argument("--num-episodes", type=int, default=10)
    parser.add_argument("--llm", type=str, default="chatgpt")
    parser.add_argument("--erci", type=int, default=0)
    parser.add_argument("--step", type=int, default=-1)
    parser.add_argument("--irci", type=int, default=1)
    parser.add_argument("--sgrounding", action="store_true", default=False)
    parser.add_argument("--headless", action="store_true", default=True)

    opt = parser.parse_args()

    return opt

def miniwob(opt):
    env = gym.make("MiniWoBEnv-v0", env_name=opt.env, headless=opt.headless)

    success = 0
    for round in range(opt.num_episodes):
        llm_agent = LLMAgent(
            opt.env,
            rci_plan_loop=opt.erci,
            rci_limit=opt.irci,
            llm=opt.llm,
            state_grounding=opt.sgrounding,
        )
        # initialize environment
        states = env.reset(seeds=[random.random()], record_screenshots=True)
        llm_agent.set_goal(states[0].utterance)
        html_state = get_html_state(opt, states)

        llm_agent.update_html_state(html_state)

        try:
            llm_agent.initialize_plan()
        except Exception as e:
            logging.error(f"Failed to initialize plan: {e}")
            continue

        if opt.step == -1:
            step = llm_agent.get_plan_step()
        else:
            step = opt.step

        logging.info(f"The number of generated action steps: {step}")

        for _ in range(step):
            assert len(states) == 1
            try:
                instruction = llm_agent.generate_action()
                logging.info(f"The executed instruction: {instruction}")

                miniwob_action = llm_agent.convert_to_miniwob_action(instruction)

                states, rewards, dones, _ = env.step([miniwob_action])
            except ValueError:
                print("Invalid action or rci action fail")
                rewards = [0]
                dones = [True]
                break

            if rewards[0] != 0:
                break

            if all(dones):  # or llm_agent.check_finish_plan():
                break

            html_state = get_html_state(opt, states)
            llm_agent.update_html_state(html_state)

        if rewards[0] > 0:
            success += 1
            llm_agent.save_result(True)
        else:
            llm_agent.save_result(False)

        print(f"success rate: {success} / {round + 1} = {success / (round + 1)}")

    env.close()


def get_html_state(opt, states):
    extra_html_task = [
        "click-dialog",
        "click-dialog-2",
        "use-autocomplete",
        "choose-date",
    ]

    html_body = states[0].html_body
    if opt.env in extra_html_task:
        html_body += states[0].html_extra
    return html_body


if __name__ == "__main__":
    opt = parse_opt()
    miniwob(opt)
