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

from .commands.create import ComposeCreateCommand
from .commands.setup import ComposeSetupCommand


class RtwParserComposer:
    def __new__(cls):
        parser = ArgumentParser(prog="rtw")
        parser.add_argument("--version", action="version", version="%(prog)s 1.0")
        sub_commands_parsers = parser.add_subparsers()
        ComposeCreateCommand(sub_commands_parsers)
        ComposeSetupCommand(sub_commands_parsers)
        return parser
