import subprocess
from typing import overload

from cmd.cmd import Command

from datetime import date


class CommandOutputConsumer:

    @overload
    def consum(self, output_line: str):
        pass


class CommandExecutor:

    def __init__(self, output_consumer: CommandOutputConsumer):
        self.output_consumer = output_consumer

    def execute(self, command: Command):
        print('running command:', ' '.join(command.as_list()))

        process = subprocess.Popen(
            command.as_list(),
            stdout=subprocess.PIPE,
            universal_newlines=True)

        while True:
            output_line = process.stdout.readline()
            self._write_output_line(output_line.strip())
            return_code = process.poll()
            if return_code is not None:
                print('RETURN CODE', return_code)
                # Process has finished, read rest of the output
                for output_line in process.stdout.readlines():
                    self._write_output_line(output_line.strip())
                return

    def _write_output_line(self, output_line: str):
        if len(output_line.strip()) > 0:
            self.output_consumer.consum(output_line.strip())


class BufferCommandOutputConsumer(CommandOutputConsumer):

    def __init__(self):
        self.output_lines = []

    def consum(self, output_line: str):
        self.output_lines.append(output_line)


class ConsoleCommandOutputConsumer(CommandOutputConsumer):

    def __init__(self, prefix='> '):
        self.prefix = prefix

    def consum(self, output_line: str):
        print(self.prefix + output_line)


class FileCommandOutputConsumer(CommandOutputConsumer):

    def __init__(self, file_name: str):
        self.file_name = file_name

    def consum(self, output_line: str):
        with open(_extend_file_name_with_today_date(self.file_name), 'a') as file:
            file.write(output_line + '\n')


def _extend_file_name_with_today_date(file_name: str) -> str:
    file_extension_index = file_name.rindex('.')
    return file_name[:file_extension_index] \
           + '_' + str(date.today()) \
           + file_name[file_extension_index:]
