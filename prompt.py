import os


class Prompt:
    def __init__(self, env: str = "click-button") -> None:
        self.llm = "davinci"
        self.davinci_type_regex = "^type\s.{1,}$"
        self.chatgpt_type_regex = '^type\s[^"]{1,}$'
        self.press_regex = (
            "^press\s(enter|arrowleft|arrowright|arrowup|arrowdown|backspace)$"
        )
        self.clickxpath_regex = "^clickxpath\s.{1,}$"
        self.clickoption_regex = "^clickoption\s.{1,}$"
        self.movemouse_regex = "^movemouse\s.{1,}$"

        if os.path.exists(f"prompt/{env}/"):
            base_dir = f"prompt/{env}/"
        else:
            base_dir = "prompt/"

        self.example_prompt = self.load_prompt_file(base_dir, "example.txt")
        self.first_action_prompt = self.load_prompt_file(base_dir, "first_action.txt")
        self.base_prompt = self.load_prompt_file(base_dir, "base.txt")
        self.init_plan_prompt = self.load_prompt_file(base_dir, "initialize_plan.txt")
        self.action_prompt = self.load_prompt_file(base_dir, "action.txt")
        self.rci_action_prompt = self.load_prompt_file(base_dir, "rci_action.txt")
        self.update_action = self.load_prompt_file(base_dir, "update_action.txt")

        self.base_prompt = self.replace_regex(self.base_prompt)
        self.rci_action_prompt = self.replace_regex(self.rci_action_prompt)

    def load_prompt_file(self, base_dir, filename):
        prompt_file = os.path.join(base_dir, filename)
        if os.path.exists(prompt_file):
            with open(prompt_file) as f:
                return f.read()
        else:
            with open(os.path.join('prompt/', filename)) as f:
                return f.read()

    def replace_regex(self, base_prompt):
        if self.llm == "chatgpt":
            base_prompt = base_prompt.replace("{type}", self.chatgpt_type_regex)
        elif self.llm == "davinci":
            base_prompt = base_prompt.replace("{type}", self.davinci_type_regex)
        else:
            raise NotImplementedError

        base_prompt = base_prompt.replace("{press}", self.press_regex)
        base_prompt = base_prompt.replace("{clickxpath}", self.clickxpath_regex)
        base_prompt = base_prompt.replace("{clickoption}", self.clickoption_regex)
        base_prompt = base_prompt.replace("{movemouse}", self.movemouse_regex)

        return base_prompt
