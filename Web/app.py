import asyncio  # Использовать await and async
import aiohttp  # Использовать для запросов на веб сервисы
import ssl
from config import TOKEN

TOKEN = TOKEN
URL = f"https://api.telegram.org/bot{TOKEN}/"

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE


async def send_message(chat_id, text):
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl_context=ssl_context)) as session:
        params = {'chat_id': chat_id, 'text': text}
        async with session.get(URL + 'sendMessage', params=params) as response:  # Fixed 'data' to 'params'
            await response.text()


async def handle_updates(update):
    message = update.get('message', False)
    if message:
        chat_id = message['chat']['id']
        text = message.get('text', False)
        if text:
            await send_message(chat_id, f'Эхо: {text}')
        else:
            await send_message(chat_id, "I'm working only with the text!")


async def get_updates():
    offset = None
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl_context=ssl_context)) as session:
        while True:  # Бесконечный запрос на сервер телеграмма, это и называется поллинг, опрос
            params = {'timeout': 10, 'offset': offset}
            async with session.post(URL + 'getUpdates', data=params) as response:  # используем пост запрос
                updates = await response.json()
                if len(updates['result']) > 0:
                    offset = updates['result'][-1]['update_id'] + 1
                    for update in updates['result']:
                        await handle_updates(update)

                        for_print = update.copy()
                        print(for_print)


async def main():
    await get_updates()


asyncio.run(main())
