import yaml
from path_manager import PathResolver

def parse_bar():
    paths = PathResolver()
    config_path = paths.common_framework / 'config/bar.yml'
    with config_path.open() as f:
        data = yaml.safe_load(f)
        return data
