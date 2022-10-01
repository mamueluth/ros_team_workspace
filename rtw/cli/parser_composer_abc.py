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

from abc import ABC, abstractmethod
from argparse import ArgumentParser
from typing import Any


class ParserComposerABC(ABC):
    def __init__(self, subparsers) -> None:
        super().__init__()
        self.compose_parser(subparsers)

    def compose_parser(self, subparsers) -> ArgumentParser:
        parser = self.create_parser(subparsers)
        self.add_arguments(parser)
        subsubparsers = self.create_subparser_group(parser)
        self.compose_subparsers(subsubparsers)
        return parser

    @abstractmethod
    def create_parser(self, sub_parsers) -> ArgumentParser:
        pass

    @abstractmethod
    def add_arguments(self, parser) -> None:
        pass

    @abstractmethod
    def create_subparser_group(self, parser) -> Any:
        pass

    @abstractmethod
    def compose_subparsers(self, subsubparsers) -> None:
        pass
