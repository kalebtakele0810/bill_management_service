from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events
from loguru import logger
from django.utils import timezone
from base.models import Bill
from django.core.mail import EmailMessage


#send reminder before 2 days of due date
def send_reminder_email():
    logger.info("Scheduled task started!")
    bills = Bill.objects.filter(status='PENDING', 
                                dueDate = timezone.now().date() + timezone.timedelta(days=2)
                                )
    for bill in bills:
        send_email_with_attachment(to=bill.customer.email)
        logger.info("Sending reminder email to: {}", bill.customer.email)
   


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), 'default')
    scheduler.add_job(send_reminder_email, trigger='interval', hours=24, name='send_reminders', jobstore='default')
    register_events(scheduler)
    scheduler.start()

def send_email_with_attachment(to):
    logger.info("Sending email: {}",to)
    subject = 'Bill Payment Approaching'
    message = 'Dear customer, plese pay you payment for bill in 48 hours.'
    from_email = 'admin@freesmtpservers.com'
    recipient_list = [to]

    email = EmailMessage(subject, message, from_email, recipient_list)
    email.send()

    return True