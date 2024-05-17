from celery import shared_task
from django.core.mail import send_mail

from .models import Pedido


@shared_task
def order_created(pedido_id):
    pedido = Pedido.objects.get(id=pedido_id)
    subject = f'Pedido nr. {pedido.id}'
    message = (
        f'Estimado {pedido.nombre},\n\n'
        f'Ha realizado correctamente un pedido.'
        f'Su ID de pedido es el {pedido.id}.'
    )
    mail_sent = send_mail(
        subject, message, 'nachoDamDjango@gmail.com', [pedido.email]
    )
    return mail_sent
