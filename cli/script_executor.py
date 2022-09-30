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
    def __init__(self, script: str) -> None:
        self.script = script
        self._shell = "sh"

    @property
    def script(self):
        return self._script

    @script.setter
    def script(self, script):
        if not Path(script).is_file():
            raise FileNotFoundError(
                errno.ENOENT,
                os.strerror(errno.ENOENT),
                f'The script:"{script}" passed to the ScriptExecutor does not exist.',
            )
        self._script = script

    def execute(self, args=None):
        try:
            subprocess.call([self._shell, self.script])
        except:
            pass
