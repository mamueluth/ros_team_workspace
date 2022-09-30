from cli.commands.create.create_new_package import CreateNewPackageCommand


class MapToCommand:
    def map_to_executor(self, command):
        command_executor = {"create new-workspace": CreateNewPackageCommand}

        def raise_unknown_executor():
            raise NotImplementedError()

        return command_executor.get(command, raise_unknown_executor)()
