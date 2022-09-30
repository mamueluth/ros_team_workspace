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

from cli.parser_composer_abc import ParserComposerABC
from .create_new_package import CreateNewPackageCommandParser
from .create_new_workspace import CreateNewWorkspaceCommandParser


class ComposeCreateCommand(ParserComposerABC):
    def compose_subparsers(self, sub_parsers):
        # create the parse for the "create" sub-command
        create_command_parser = sub_parsers.add_parser(
            "create", help="Creates new [ros workspaces, ros package]."
        )

        # create sub-parser for sub-command create
        create_command_subparsers = create_command_parser.add_subparsers(
            help="create new_workspace_parser command help"
        )

        CreateNewPackageCommandParser(create_command_subparsers)
        CreateNewWorkspaceCommandParser(create_command_subparsers)
