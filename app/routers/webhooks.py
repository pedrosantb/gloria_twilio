'''
WebHook listener routes
'''
from fastapi import FastAPI, APIRouter, Request, status
# from fastapi.responses import JSONResponse
from services.twilio_services import Twilio

webhook_router = APIRouter(prefix="/webhook")

@webhook_router.post("/gloriaListener")
async def gloria_listener(request: Request):
    data_raw_json = await request.json()
    order_details = data_raw_json["orders"][0]

    client_phone = order_details['client_phone']
    client_first_name = order_details['client_first_name']
    order_type = order_details['type']
    order_status = order_details['status']

    message_body = f'Hello, {client_first_name}. Your order at Juice Guys is {order_status}'

    sms_client = Twilio()
    sms_status = await sms_client.send_message(client_phone, message_body)
    print(sms_status)
    return status.HTTP_200_OK