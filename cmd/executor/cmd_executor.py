import subprocess

from cmd import Command

class CommandOutputConsumer:

    def consum(self, output_line: str):
        pass

class CommandExecutor:

    def __init__(self, creator: CommandCreator, output_consumer: CommandOutputConsumer):
        self.creator = creator
        self.output_consumer = output_consumer

    def execute(self, command: Command):
        print('running command: ', ' '.join(command.as_list()))

        process = subprocess.Popen(
            command.as_list(),
            stdout=subprocess.PIPE,
            universal_newlines=True)

        while True:
            output_line = process.stdout.readline()
            self.output_consumer.consum(output_line.strip())
            return_code = process.poll()
            if return_code is not None:
                print('RETURN CODE', return_code)
                # Process has finished, read rest of the output
                for output_line in process.stdout.readlines():
                    self.output_consumer.consum(output_line.strip())
                break

class ConsoleCommandOutputConsumer(CommandOutputConsumer):

    def __init__(self, file_name: str):
        self.file_name = file_name

    def consum(self, output_line: str):
        print('# ' + output_line)

class FileCommandOutputConsumer(CommandOutputConsumer):

    def __init__(self, file_name: str):
        self.file_name = file_name

    def consum(self, output_line: str):
        with open(self.file_name, 'a') as file:
            file.write(output_line + '\n')
