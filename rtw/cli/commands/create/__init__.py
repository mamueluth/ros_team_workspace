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
from typing import Any


from rtw.cli.parser_composer_abc import ParserComposerABC
from .create_new_package import CreateNewPackageCommandParser, CreateNewPackageCommand
from .create_new_workspace import CreateNewWorkspaceCommandParser, CreateNewWorkspaceCommand


class ComposeCreateCommand(ParserComposerABC):
    def create_parser(self, sub_parsers) -> ArgumentParser:
        # create the parser for the "create" sub-command
        create_command_parser = sub_parsers.add_parser(
            "create", help="Create new-workspace or new-package."
        )
        return create_command_parser

    def add_arguments(self, parser) -> None:
        pass

    def create_subparser_group(self, create_command_parser) -> Any:
        # create sub-parser group for sub-command create
        create_command_subparsers = create_command_parser.add_subparsers(
            help="Create new-workspace or new-package.", dest="subcommand"
        )
        return create_command_subparsers

    def compose_subparsers(self, create_command_subparsers) -> None:
        CreateNewPackageCommandParser(create_command_subparsers)
        CreateNewWorkspaceCommandParser(create_command_subparsers)
