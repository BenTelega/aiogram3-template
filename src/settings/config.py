from dotenv import load_dotenv 
from os import getenv
from . import json_config

json = lambda: json_config.Config.parse_file('./settings/config.json')

load_dotenv('../.env')

# getting
BOT_TOKEN = getenv('BOT_TOKEN')