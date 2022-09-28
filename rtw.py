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

from cli.rtw_parser import RtwParser
from cli.script_executor import ScriptExecutor


class CreateNewPackageCommand:
    def __init__(self) -> None:
        self._script_path = (
            "/home/stogl-robotics/workspaces/rtw/ros_team_workspace/scripts/test_script.bash"
        )
        self._script_executor = ScriptExecutor(self._script_path)

    def execute(self):
        self._script_executor.execute()


def main():
    # create the top-level parser
    parser = RtwParser()
    options = parser.parse_args(args=None if sys.argv[1:] else ["--help"])
    print("#" * 10)
    print(f"Command:{options.command} {options.subcommand}")
    print(f"with Options:{options}")
    print("#" * 10)
    if options.command == "create" and options.subcommand == "new-workspace":
        pkg_cmd = CreateNewPackageCommand()
        pkg_cmd.execute()


if __name__ == "__main__":
    main()
