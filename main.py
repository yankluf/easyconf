import toml
import argparse
from pathlib import Path, PurePath

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
        self.config = self.read_config()


    def safe_filepath(self):
        config_dir = Path.home() / '.config'
        config_dir.mkdir(parents=True, exist_ok=True)
        path = PurePath(config_dir, 'vars.toml')
        return path

    def detect_tables(self, key_arg):
        key_arg.split('.')

    def read_config(self):
        with open(self.file, 'r') as f:
            config = toml.load(f)
        return config

    def update_config(self):
        args.key

    


if __name__ == "__main__":
    args = parse_arguments()
    app = App(args)
    print(app.file)
