import getpass
import sys

from secret_santa.santa_email import email_santa_pairing
from secret_santa.secret_santa import (
    Participant, SantaPair,
    parse_participant_file,
    generate_santa_pairings
)


def run(participant_file_path: str) -> None:
    # Get list of participants from the provided file.
    participants: [Participant] = parse_participant_file(
        participant_file_path
    )

    # Match all participants up with a secret santa.
    santa_pairings: [SantaPair] = generate_santa_pairings(participants)

    # Get the email details of the secret santa organiser so emails can be
    # sent from their account.
    organiser_name: str = input('Please enter your name:')
    organiser_email: str = input(
        'Please enter an email from which to notify participants:'
    )
    organiser_password: str = getpass.getpass(
        prompt='Please enter the email password:'
    )

    # Email all participants with their secret santa pairing.
    for santa_pairing in santa_pairings:
        email_santa_pairing(
            santa_pairing,
            organiser_name,
            organiser_email,
            organiser_password
        )


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        raise Exception('Error, no participant list provided.')

    run(sys.argv[1])
