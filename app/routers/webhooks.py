'''
WebHook listener routes
'''
from fastapi import FastAPI, APIRouter, Request, status, Depends
from sqlalchemy.orm import Session

from services.twilio_services import Twilio
import services.global_services as service

webhook_router = APIRouter(prefix="/webhook")

@webhook_router.post("/gloriaListener")
async def gloria_listener(request: Request, db: Session = Depends(service.get_db)):
    data_raw_json = await request.json()
    order_details = data_raw_json["orders"][0]

    order = await service.get_order(db, id=order_details['id'])
    
    if not order:
        create_status = await service.create_order(db, order_details)
        if not create_status:
            return status.HTTP_500_INTERNAL_SERVER_ERROR
        order = await service.get_order(db, id=order_details['id'])
        message_body = f'Hello, {order.first_name}. Your order at Juice Guys is {order.status}'
    else:
        if order.status != 'accepted':
            return status.HTTP_200_OK
        message_body = f'Hello, {order.first_name}. Your order at Juice Guys is ready to pickup'

    sms_client = Twilio()
    sms_status = await sms_client.send_message(order.phone_number, message_body)
    print(sms_status)

    return status.HTTP_200_OK


@webhook_router.get("/gloriaListener")
async def gloria_listener_get(request: Request, db: Session = Depends(service.get_db)):
    data_raw_json = await request.json()
    order_details = data_raw_json["orders"][0]

    order = await service.get_order(db, id=order_details['id'])
    
    if not order:
        create_status = await service.create_order(db, order_details)
        if not create_status:
            return status.HTTP_500_INTERNAL_SERVER_ERROR
        order = await service.get_order(db, id=order_details['id'])
        message_body = f'Hello, {order.first_name}. Your order at Juice Guys is {order.status}'
    else:
        if order.status != 'accepted':
            return status.HTTP_200_OK
        message_body = f'Hello, {order.first_name}. Your order at Juice Guys is ready to pickup'

    sms_client = Twilio()
    sms_status = await sms_client.send_message(order.phone_number, message_body)
    print(sms_status)

    return status.HTTP_200_OK