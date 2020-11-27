import email
import unittest
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from unittest.mock import patch

from .santa_email import email_santa_pairing
from .secret_santa import (
    Participant,
    SantaPair
)


class SantaEmailTestCase(unittest.TestCase):
    """
    A suite of tests surrounding the santa email logic.
    """

    @patch("smtplib.SMTP_SSL")
    def test_email_santa_pairing(self, mock_smtp):
        """
        Test that emails are populated and sent out correctly.
        """

        # Build the santa pair to use for testing.
        giver: Participant = Participant('giver', 'giver@email.com')
        receiver: Participant = Participant('receiver', 'receiver@email.com')
        giver_receiver_pair = SantaPair(giver, receiver)

        # The organiser details.
        organiser_name = 'Organiser Name'
        organiser_email = 'organiser@email.com'
        organiser_password = 'organiser_password'

        # The email expected to be sent by email_santa_pairing()
        expected_email_message: MIMEMultipart = MIMEMultipart('alternative')
        expected_email_message['Subject'] = 'Secret Santa!'
        expected_email_message['From'] = (
            organiser_name + ' <' + organiser_email + '>'
        )
        expected_email_message['To'] = giver.email
        expected_email_message_content = (
            'Hi giver,\n\n'
            'Thanks for taking part in our secret santa!\n\n'
            'You will be choosing a gift for receiver.\n\n'
            'Remember, the budget is £5.\n\n'
            'Choose wisely!'
        )
        expected_email_message.attach(MIMEText(expected_email_message_content))

        # Make the call to send an email for the santa pair.
        email_santa_pairing(
            giver_receiver_pair,
            organiser_name,
            organiser_email,
            organiser_password
        )

        # TODO: We should really test the smtp details provided but
        # they're hardcoded for gmail right now.

        # We have to access the mocks a little differently as we're using
        # a context see: https://bit.ly/3q05Wdw (StackOverflow link)
        context = mock_smtp.return_value.__enter__.return_value

        # Check login was performed with correct details.
        context.login.assert_called_with(organiser_email, organiser_password)

        # Check sendmail was called exactly once.
        context.sendmail.assert_called_once()

        # Get all arguments passed to sendmail.
        org_email_arg, giver_email_arg, email_arg = \
            context.sendmail.call_args[0]

        # Check FROM/TO arguments were set correctly.
        self.assertEqual(organiser_email, org_email_arg)
        self.assertEqual(giver.email, giver_email_arg)

        # Reconstruct email message object and check all fields are set
        # correctly.
        actual_email_message: email.message = email.message_from_bytes(
            email_arg
        )
        self.assertEqual(
            expected_email_message['Subject'],
            actual_email_message['Subject']
        )
        self.assertEqual(
            expected_email_message['From'],
            actual_email_message['From']
        )
        self.assertEqual(
            expected_email_message['To'],
            actual_email_message['To']
        )

        # TODO: check email message is correct.


if __name__ == '__main__':
    unittest.main()
