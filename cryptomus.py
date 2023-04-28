import base64
import hashlib
import json
import os

import aiohttp
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def get_header(payload):
    api_key = os.getenv('CRYPTO_API_KEY')
    merchant_id = os.getenv('CRYPTO_MERCHANT_ID')
    json_payload = json.dumps(payload, separators=(',', ':'))
    json_payload_binary = json_payload.encode('utf-8')
    sign = hashlib.md5(base64.b64encode(json_payload_binary) + api_key.encode('utf-8')).hexdigest()
    header = {
        "Content-Type": "application/json;charset=UTF-8",
        "merchant": merchant_id,
        "sign": sign,
    }
    return header


async def create_payment(amount, order_id):
    try:
        payload = {
            "amount": str(amount),
            "currency": "USD",
            "order_id": order_id,
        }
        async with aiohttp.ClientSession() as session:
            data = await session.post('https://api.cryptomus.com/v1/payment',
                                      data=json.dumps(payload, separators=(',', ':')),
                                      headers=get_header(payload),)
            return data
    except Exception as e:
        raise f'Problems with requests library {e}'


async def check_payment(uuid):
    try:
        payload = {
            'uuid': uuid
        }
        async with aiohttp.ClientSession() as session:
            data = await session.post('https://api.cryptomus.com/v1/payment/info',
                                      data=payload,
                                      headers=get_header(payload))
            return data
    except Exception as e:
        raise f'Problems with requests library {e}'
