from abc import ABC, abstractmethod

from cli.script_executor import ScriptExecutor


class CommandExecutor:
    @abstractmethod
    def execute(self, args):
        pass
