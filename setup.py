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

from setuptools import find_packages, setup

setup(
    name="rtw",
    version="1.0.0",
    description="Ros Team Workspace (rtw) is a framework for boosting collaboration in teams when developing software for robots using Robot Operating System (ROS). It supports both ROS1 and ROS2. Its main goal is to optimize the workflow of development teams and focus more on programming robots.",
    url="https://stoglrobotics.github.io/ros_team_workspace/master/index.html",
    author="Stogl Robotics Consulting UG (haftungsbeschränkt)",
    author_email="denis.stogl@stoglrobotics.de",
    packages=find_packages(exclude=["test"]),
    include_package_data=True,
    install_requires=[],
)
