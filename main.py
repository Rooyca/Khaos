"""

MIT License

Copyright (c) 2021 Rooyca

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

import os
import rcc
import uuid
import json
import string
import random
import secrets
import requests
import hashlib

from os import urandom
from random import randint
from typing import Optional, List
from lor_deckcodes import LoRDeck
from fastapi import FastAPI, HTTPException, Query

app = FastAPI()

@app.get('/v1/random/uuid')
async def random_uuid():
	return {"success":True,
			"uuid":uuid.uuid4()}

@app.get('/v1/random/password')
async def random_password(numb: int=1, leng: int=12, include: str = "ULNS"):
	passwords = []
	chars = ""

	if "U" in include:
		chars = chars + string.ascii_uppercase

	if "L" in include:
		chars = chars + string.ascii_lowercase

	if "N" in include:
		chars = chars + string.digits

	if "S" in include:
		chars = chars + '`!”?$?%}^&*()_–+={[]:;@‘~#|<,>.?/'

	def generate_password(length):
		try:
			return "".join(chars[c % len(chars)] for c in urandom(length))
		except:
			raise HTTPException(status_code=400, detail={"success":False,
										"description":f"{include} are not valid options",
										"valid_options":["(U)ppercase", "(L)owercase", "(N)umbers","(S)imbols"]
										})

	if leng >= 12:
		for _ in range(numb):
			passwords.append(generate_password(leng))
	else:
		raise HTTPException(status_code=400, detail="The password has to be at least 12 characters long")

	def password_security():
		if len(chars) >=50 and leng >= 12:
			return {"status":"Passwords are secure!",
					"Advice":"Don't use a password more than one time and try to change it at leats one every 3 months"}
		return {"status": "WARNING! I cannot guarantee the security of these passwords. Checkout here: https://howsecureismypassword.net/",
				"Advice":"You should use at least 3 types of characters(ULNS) or a bigger length"}

	return {"success":True,
		"info":{
		"passwords_security":password_security(),
		"password_length":leng,
		"passwords_number":numb,
		"passwords":passwords}}


@app.get('/v1/random/cc')
async def random_cc(numb: int = Query(..., ge=1, le=10)):

	random_cc = []
	for _ in range(numb):
		new_cc = random_cc.append(rcc.generate_credit_card())

	return {"success":True,
			"cc_number":numb,
			"info":random_cc}

@app.get('/v1/random/word')
async def random_word(numb: int = Query(..., ge=1, le=10)):
	en_dictionary = os.path.join(os.path.dirname(__file__), 'static/dictionary_alpha_arrays.json')

	with open(en_dictionary) as dictio:
		dictionary = json.load(dictio)
	random_words = []

	for _ in range(numb):
		random_letter = random.choice(dictionary)
		new_word = random_words.append(random.choice(list(random_letter.items())))

	return {"success":True,
			"word_number":numb,
			"words":random_words}

url = "https://www.1secmail.com/api/v1/"

@app.get('/v1/random/email')
async def random_email(user: Optional[str]=None):
	
	def creating_email(username):
		domains_list = requests.get(url,"action=getDomainList")
		domain = random.choice(domains_list.json())
		return {"email":username+"@"+domain}

	if not user:
		name = "".join(random.choice(string.ascii_lowercase)for _ in range(7))
		return creating_email(name)

	return creating_email(user)

@app.get('/v1/random/email/inbox')
async def reading_inbox(email: str):
		username = email.split("@")[0]
		domain = email.split("@")[1]
		getting_inbox = requests.get(url, f"action=getMessages&login={username}&domain={domain}")
		return {"info":getting_inbox.json()}

@app.get('/v1/random/color')
async def random_color(numb: int = 1, using: str = "hex"):
	colores = {"code":{
			   "hex":[],
			   "rgb":[]
			   }}

	def hex_color():
		new_color = colores['code']['hex'].append("#"+secrets.token_hex(3))

	def rgb_color():
		new_color = colores['code']['rgb'].append(str(randint(0,255))for _ in range(3))

	for _ in range(numb):
		hex_color()
		rgb_color()

	try:
		if using == "all":
			return {"colors":colores['code']} 
		return {"colors":colores['code'][using]}

	except:
		raise HTTPException(status_code=400, 
							detail="Make sure that you are using the correct value(hex, rgb or all)")

@app.get('/v1/random/userdata')
async def random_userdata():
	states_data = os.path.join(os.path.dirname(__file__), 'static/states_data.json')
	first_name = os.path.join(os.path.dirname(__file__), 'static/first-names.json')
	last_name = os.path.join(os.path.dirname(__file__), 'static/names.json')
	domain_name = os.path.join(os.path.dirname(__file__), 'static/domains_whitelist.txt')

	with open(states_data) as states_d:
		states = json.load(states_d)

	with open(first_name) as first_n:
		first = json.load(first_n)

	with open(last_name) as last_n:
		last = json.load(last_n)

	with open(domain_name, 'r') as domain:
		domain_n = domain.readlines()

	user_location = random.choice(list(random.choice(states).items()))

	data = {
			  "firstName": "",
			  "lastName": "",
			  "emailAddress": "",
			  "phoneNumber": "",
			  "country": "USA",
			  "state":"",
			  "birthDate": "",
			  "gender": ""
			}

	data['firstName'] = ''.join(random.choice(first))
	data['lastName'] = ''.join(random.choice(last))
	data['state'] = user_location[0]
	data['phoneNumber'] = "("+str(random.choice(user_location[1]['area_codes']))+")"+str(randint(100,999))+"-"+str(randint(1000,9999))
	data['birthDate'] = str(randint(1,12))+"/"+str(randint(1,31))+"/"+str(randint(1930,2001))
	data['emailAddress'] = data['firstName']+data['birthDate'].split("/")[-1]+"@"+random.choice(domain_n).replace('\n','')
	data['gender'] = ''.join(random.choice(["Male","Female"]))

	return data

@app.get('/v1/random/choice')
async def random_choice(option: List[str] = Query(...)):

	return {"success":True,
			"description":{
			"optionsNumber":len(option),
			"randomChoice":random.choice(option)
			}
		}

@app.get('/v1/random/lordeck')
async def random_lordeck():
	card_number = []
	cards = []
	factions = ["BC","BW","DE","FR","IO","NX","PZ","SH","SI","MT"]
	reg_one = random.choice(factions)
	reg_two = random.choice(factions)

	while True:
	    if sum(card_number) > 40:
	        card_number.remove(random.choice(card_number))
	    if sum(card_number) < 40:
	        card_number.append(random.randint(1,3))
	    if sum(card_number) == 40:
	        break

	with open("static/Factions/"+reg_one, "r") as ro:
	    region_one = ro.readlines()

	with open("static/Factions/"+reg_two, "r") as rt:
	    region_two = rt.readlines()

	for i in range(len(card_number)):
	    def get_card():
	        return random.sample(random.choice([region_one, region_two]),1)
	    value = get_card()
	    for card in cards:
	        if value[0] == card[2:]:
	            value = get_card()
	    new_card = cards.append(str(card_number[i])+":"+value[0])

	deck = LoRDeck(cards)

	return {"success":True,
			"description":{
			"regions":reg_one+"/"+reg_two,
			"cardNumber":len(card_number),
			"deckCode":deck.encode()
			}
		}

@app.get('/v1/random/phrase')
async def random_phrase(ussing: Optional[str] = "AN", numb: Optional[int] = 1):

	with open("static/en/en-adjectives.txt","r") as adj:
		adjective = adj.readlines()

	with open("static/en/en-nouns.txt", "r") as nou:
		noun = nou.readlines()

	with open("static/en/en-verbs-all.json", errors="ignore") as v:
		verb = json.load(v)

	phrase = {"AN":[],
			  "NN":[],
			  "VN":[]}

	try:
		if ussing == "AN":
			for _ in range(numb):
				phrase["AN"].append(random.choice(adjective).replace('\n',' ').capitalize()+random.choice(noun).replace('\n',''))
		
		if ussing == "NN":
			for _ in range(numb):
				phrase["NN"].append(random.choice(noun).replace('\n',' ').capitalize()+random.choice(noun).replace('\n',''))

		if ussing == "VN":
			for _ in range(numb):
				phrase["VN"].append(random.choice(verb)[0].capitalize()+" "+random.choice(noun).replace('\n',''))

		return {"success":True,
				"description":{
				"phrase":phrase[ussing]
				}
			}

	except:
		raise HTTPException(status_code=400, 
			detail="Please select a valid option: AN (Adjective + Noun), NN (Noun + Noun) or VN (Verb + Noun)")

@app.get('/v1/random/passphrase')
async def random_passphrase(n_words: int = Query(7, ge=7), esp: bool = False):
	sentence_ = []

	if esp:
		with open("static/bip/spanish.txt", "r") as esp:
			palabras = esp.readlines()
			for _ in range(n_words):
				sentence_.append(random.choice(palabras))
			return {"success":True,
					"detalles":{
					"numero_de_palabras":n_words,
					"passphrase":' '.join(w for w in sentence_).replace('\n','')
					}
				}

	with open("static/bip/eff_large_wordlist.txt") as mn:
		mnemo = mn.readlines()

	def new_word():
		dn = []
		for _ in range(5):
			dn.append(random.randint(1,6))
		return dn

	for _ in range(n_words):
		index_w = new_word()

		if index_w in sentence_:
			index_w = new_word()

		indx_ = ''.join(str(e) for e in index_w)

		for word in mnemo:
			if int(word[:5]) == int(indx_):
				sentence_.append(word[5:].replace('\t','').replace('\n',''))
				break

	return {"success":True,
			"description":{
			"pass_length":n_words,
			"passphrase":' '.join(w for w in sentence_)
			}
		}