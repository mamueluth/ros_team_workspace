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

from cli.subparser_abc import SubparserABC


class CreateNewWorkspaceCommandParser(SubparserABC):
    def __init__(self, parser) -> None:
        super().__init__(parser)

    def add_subparser(self, sub_parser) -> argparse.ArgumentParser:
        # create sub-command "crazy" for sub-command cool
        new_workspace_parser = sub_parser.add_parser(
            "new_workspace", help="new_workspace [Workspace name, ros distribution]."
        )

        return new_workspace_parser

    def add_arguments(self, new_workspace_parser) -> None:

        new_workspace_parser.add_argument(
            "num", nargs="+", type=str, help="Provide workspace_name."
        )

        return
