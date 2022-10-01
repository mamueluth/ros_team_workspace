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
import errno
import os
import subprocess

from pathlib import Path


class ScriptExecutor:
    def __init__(self) -> None:
        self._shell = "bash"

    def execute(self, script: Path, *argv):
        if not script.is_file():
            raise FileNotFoundError(
                errno.ENOENT,
                os.strerror(errno.ENOENT),
                f'The script:"{script}" passed to the ScriptExecutor does not exist.',
            )

        cmd = [script] + [arg for arg in argv if arg != None]
        print(cmd)
        try:
            subprocess.run(cmd, check=True, text=True)
        except:
            pass
