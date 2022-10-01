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
import sys

from rtw.cli.rtw_parser import RtwParser
from rtw.cli.mapper import MapToCommand
from rtw.definitions import PATHS


def main():
    # create the top-level parser

    parser = RtwParser()
    args = parser.parse_args(args=None if sys.argv[1:] else ["--help"])
    print("#" * 10)
    print(f"Command:{args.command} {args.subcommand}")
    print(f"with args:{args}")
    print("#" * 10)
    mapper = MapToCommand()
    executor = mapper.map_to_executor(args)
    executor.execute(args)


if __name__ == "__main__":
    main()
