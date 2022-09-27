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


class SubparserABC(ABC):
    def __init__(self, parser) -> None:
        new_subparser = self.add_subparser(parser)
        self.add_arguments(new_subparser)

    @abstractmethod
    def add_subparser(self, parser) -> ArgumentParser:
        pass

    @abstractmethod
    def add_arguments(self, new_subparser) -> None:
        pass
