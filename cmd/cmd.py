class Command:

    def __init__(self, name: str, args: [str]):
        self.name = name
        self.args = args

    def as_list(self):
        return [name] + args

class CommandCreator:

    def create(self) -> Command:
        pass
