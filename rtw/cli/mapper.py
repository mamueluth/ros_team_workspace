from rtw.cli.commands.create import CreateNewPackageCommand, CreateNewWorkspaceCommand


class MapToCommand:
    def map_to_executor(self, args):
        command = args.command + " " + args.subcommand
        command_executor = {
            # create commands
            "create new-workspace": CreateNewWorkspaceCommand,
            "create new-package": CreateNewPackageCommand,
        }

        def raise_unknown_executor():
            raise NotImplementedError()

        return command_executor.get(command, raise_unknown_executor)()
