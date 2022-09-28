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

from cli.parser_composer_abc import ParserComposerABC
from .setup_auto_sourcing import SetupAutoSourcingCommandParser


class ComposeSetupCommand(ParserComposerABC):
    def create_parser(self, subparsers) -> ArgumentParser:
        # create the parser for the "setup" sub-command
        setup_command_parser = subparsers.add_parser("setup", help="Setup auto-sourcing or ")
        return setup_command_parser

    def add_arguments(self, parser) -> None:
        pass

    def create_subparser_group(self, setup_command_parser) -> Any:
        # create sub-parser group for sub-command setup
        setup_command_subparsers = setup_command_parser.add_subparsers(
            help="Create new-workspace or new-package."
        )
        return setup_command_subparsers

    def compose_subparsers(self, setup_command_subparsers) -> None:
        SetupAutoSourcingCommandParser(setup_command_subparsers)
