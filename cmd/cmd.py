class Command:

    def __init__(self, name: str, args: [str]):
        splitted_name = name.split()
        self.name = splitted_name[0]
        self.args = splitted_name[1:] + args

    def __str__(self) -> str:
        return 'Command{' \
               + 'name=' + self.name \
               + ', args=' + self.args \
               + '}'

    def as_list(self):
        return [self.name] + self.args
