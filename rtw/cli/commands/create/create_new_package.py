# Copyright (c) 2022, Stogl Robotics Consulting UG (haftungsbeschränkt)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from argparse import ArgumentParser
from functools import reduce
from pathlib import Path

from rtw.cli.command_executor_abc import CommandExecutor
from rtw.cli.script_executor import ScriptExecutor
from rtw.cli.subparser_abc import SubparserABC
from rtw.definitions import PATHS


class CreateNewPackageCommand(CommandExecutor):
    def __init__(self) -> None:
        self._script_path = Path(PATHS.get("scripts"), "test_script.bash")
        self._script_executor = ScriptExecutor()

    def execute(self, args):
        description = reduce(lambda x, y: x + " " + y, args.description)
        self._script_executor.execute(self._script_path, args.pkg_name, description)


class CreateNewPackageCommandParser(SubparserABC):
    def add_subparser(self, subparser_group) -> ArgumentParser:
        # create sub-command "new_package" for sub-command create
        new_package_parser = subparser_group.add_parser(
            "new-package",
            help="Creates a new ros package. Usage: rtw create new-package workspace_name pkg_name description",
        )

        return new_package_parser

    def add_arguments(self, new_package_parser) -> None:

        new_package_parser.add_argument(
            "pkg_name", type=str, help="Provide the name of the package you would like to create."
        )
        new_package_parser.add_argument(
            "description", type=str, nargs="+", help="Provide a description of your package."
        )
        return
