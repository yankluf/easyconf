import argparse
import toml
from collections import defaultdict
from pathlib import Path, PurePath

CONFIG_FILENAME='config.toml'

def parse_arguments():
    parser = argparse.ArgumentParser(
            prog='EasyConf',
            description='A simple CLI tool to manage TOML files.\nBy default, it changes ~/.config/config.toml'
    )

    parser.add_argument('key', help='Name of the key that you want set a value')
    parser.add_argument('value', help='Value that you want to set')
    parser.add_argument('-f', '--file', help='Change the default TOML file')

    return parser.parse_args()

class App():
    def __init__(self, args):
        self.file = args.file or self.safe_filepath()
        self.config = defaultdict(self.read_config)


    def safe_filepath(self):
        config_dir = Path.home() / '.config'
        config_dir.mkdir(parents=True, exist_ok=True)
        file_path = config_dir / CONFIG_FILENAME
        file_path.touch(exist_ok=True)
        return PurePath(file_path)
        
    def calc_sections(self, key_arg):
        return key_arg.split('.')

    def read_config(self):
        with open(self.file, 'r') as f:
            config = toml.load(f)
        return config

    def update_config(self):
        sections = self.calc_sections(args.key)
        if len(sections) == 1:
            self.config[args.key] = args.value
        else:
            func = f'self.config'
            for section in sections:
                func = func + f'["{section}"]'
            exec(f'{func} = "{args.value}"')
    
    def write_config(self):
        with open(self.file, 'w') as f:
            toml.dump(self.config, f)

if __name__ == "__main__":
    args = parse_arguments()
    app = App(args)
    app.update_config()
    app.write_config()
    print(app.config)
