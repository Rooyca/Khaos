'''
You can checkout the CC module here: https://github.com/naijopkr/credit-card-generator
And the english dictionary here: https://github.com/matthewreagan/WebstersEnglishDictionary
'''

import os
import uuid
import json
import string
import random
import rcc

from os import urandom
from fastapi import FastAPI, HTTPException, Query

app = FastAPI()

@app.get('/v1/random/uuid')
async def random_uuid():
	return {"success":True,
			"uuid":uuid.uuid4()}

@app.get('/v1/random/password')
async def random_password(numb: int=1, leng: int=12):
	passwords = []

	def generate_password(length):
		chars = string.ascii_letters + string.digits + '-_@#$%&!?'
		return "".join(chars[c % len(chars)] for c in urandom(length))

	if leng >= 12:
		for _ in range(numb):
			passwords.append(generate_password(leng))
	else:
		raise HTTPException(status_code=400, detail="The password has to be at least 12 characters long")

	return {"success":True,
			"info":{
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
