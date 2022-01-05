
import json

def run(**args):
    print('[$] Enter Stage 2')
    basic_config =json.dumps([{"module" : "shell_module"}])
    return basic_config
                            