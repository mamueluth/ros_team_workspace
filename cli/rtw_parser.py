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

import argparse

from .commands.create import ComposeCreateCommand


class RtwParserComposer:
    def compose_parser(self):
        parser = argparse.ArgumentParser(prog="rtw")
        self.add_rtw_command_arguments(parser)
        # create sub-parser
        create_sub_parsers = parser.add_subparsers(
            help="The created command is used for setting up new workspaces or packages."
        )
        ComposeCreateCommand(create_sub_parsers)
        return parser

    def add_rtw_command_arguments(self, parser):
        parser.add_argument("--version", action="version", version="%(prog)s 1.0")
