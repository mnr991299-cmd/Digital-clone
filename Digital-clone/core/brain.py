from core.plugins import PluginManager

class Brain:
    def __init__(self):
        self.plugins = PluginManager()

    def think(self, text):
        return self.plugins.process(text)