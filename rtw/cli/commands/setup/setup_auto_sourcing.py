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

from rtw.cli.subparser_abc import SubparserABC


class SetupAutoSourcingCommandParser(SubparserABC):
    def __init__(self, parser) -> None:
        super().__init__(parser)

    def add_subparser(self, sub_parser) -> ArgumentParser:
        # create sub-command "new_package" for sub-command create
        auto_sourcing_parser = sub_parser.add_parser(
            "auto-sourcing",
            help="Automatic sourcing of the .ros_team_ws_rc is added to your .bashrc file. Usage: rtw setup auto-sourcing.",
        )

        return auto_sourcing_parser

    def add_arguments(self, auto_sourcing_parser) -> None:
        return
