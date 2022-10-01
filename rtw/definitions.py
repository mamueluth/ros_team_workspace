from pathlib import Path

FRAMEWORK = {"name": "ros_team_workspace", "short_name": "rtw"}

PATHS = {
    "framework_base_path": Path(__file__).parent.parent.absolute(),
    "scripts": Path(Path(__file__).parent.parent, "scripts").absolute(),
    "templates": Path(Path(__file__).parent.parent, "templates").absolute(),
}
