import os
import importlib

class PluginManager:
    def __init__(self):
        self.skills = []
        self.load_all_skills()

    def load_all_skills(self):
        skills_dir = os.path.join(os.path.dirname(__file__), "skills")

        if not os.path.exists(skills_dir):
            print("Skills folder missing:", skills_dir)
            return

        for file in os.listdir(skills_dir):
            if file.endswith("_skill.py"):
                module_name = f"core.skills.{file[:-3]}"
                module = importlib.import_module(module_name)
                self.skills.append(module)

    def process(self, text):
        text = text.lower()

        for skill in self.skills:
            if skill.can_handle(text):
                return skill.handle(text)

        return "I don't understand that yet." 