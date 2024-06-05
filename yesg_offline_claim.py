import requests
import threading
import time
def process_data(auth):
    headers = {
        'Accept': 'application/json, text/plain, */*',
		'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en-US,en;q=0.9',
		'Content-Length': '0',
        'Content-Type': 'application/x-www-form-urlencoded',
		'Origin': 'https://www.yescoin.gold',
		'Priority': 'u=1, i',
        'Referer': 'https://www.yescoin.gold/',
		'Sec-Ch-Ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
		'Sec-Ch-Ua-Mobile': '?1',
		'Sec-Ch-Ua-Platform': '"Android"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'Token': auth,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    }


    response = requests.post('https://api.yescoin.gold/game/claimOfflineYesPacBonus', headers=headers)
    print(response.text)

with open('datayesg.txt', 'r') as file:
            for line in file:
                auth = line.strip().split('|')
                threading.Thread(target=process_data, args=(auth)).start()
            time.sleep(5)
