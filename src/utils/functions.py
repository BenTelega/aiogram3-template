from modules import *

def check_start_command(text: str) -> dict:
	result = {
		'exist': False,
		'data': {
			'command': '',
			'data': ''
		}
	}

	try: text = text.split()[1].split('-')
	except: return result

	try:
		command = text[0]
		data = text[1]
	except: return result

	result['exist'] = True
	result['data']['command'] = command
	result['data']['data'] = data
	
	return result

async def handler_start_command(message: aiogram.types.Message, command: str, data: str, payload: dict=None) -> None:
	if command == 'ref':
		if payload['is_new']:
			pass