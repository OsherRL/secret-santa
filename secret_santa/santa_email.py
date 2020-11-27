import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Tags to replace in the email templates.
from secret_santa.secret_santa import SantaPair

GIVER_TAG: str = '<giver>'
RECEIVER_TAG: str = '<receiver>'

# Create the plain-text and HTML version of your message
email_template: str = """
Hi <giver>,

Thanks for taking part in our secret santa!

You will be choosing a gift for <receiver>.

Remember, the budget is £5.

Choose wisely!"""


def email_santa_pairing(
    santa_pairing: SantaPair,
    organiser_name: str,
    organiser_email: str,
    organiser_password: str
) -> None:
    """
    Emails all the givers in a list of santa pairings to inform them who they
    will be giving the gifts to.

    :param santa_pairing: the santa pairing to email
    :param organiser_name: the name of the secret santa event
    :param organiser_email: the email address of the secret santa organiser
        from which to send the email.
    :param organiser_password: the password of the email address from which to
        send the email
    """
    # Build the santa email.
    santa_message: MIMEMultipart = MIMEMultipart('alternative')
    santa_message['Subject'] = 'Secret Santa!'
    santa_message['From'] = organiser_name + ' <' + organiser_email + '>'
    santa_message['To'] = santa_pairing.giver.email

    # Add the correct names to the template.
    message_content: str = email_template \
        .replace(GIVER_TAG, santa_pairing.giver.name) \
        .replace(RECEIVER_TAG, santa_pairing.receiver.name)

    # Add the message content to the email.
    santa_message.attach(MIMEText(message_content, "plain"))

    # Create secure connection with server and send email
    with smtplib.SMTP_SSL(
        'smtp.gmail.com',
        465
    ) as server:
        server.login(organiser_email, organiser_password)
        server.sendmail(
            organiser_email,
            santa_pairing.receiver.email,
            santa_message.as_string()
        )
