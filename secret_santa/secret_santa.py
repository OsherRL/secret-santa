import csv
import random
from typing import NamedTuple


class Participant(NamedTuple):
    """
    Simple container for participant information.
    """
    name: str
    email: str


class SantaPair(NamedTuple):
    """
    A matched pair of giver and receiver.
    """
    giver: Participant
    receiver: Participant


def parse_participant_file(participant_list_file_path: str) -> [Participant]:
    """
    Reads all participants from the file at the supplied path and returns
    them.

    :param participant_list_file_path: the path to the participant list file
    :return: a list of Participant NamedTuple's
    """
    participants: [Participant] = []

    with open(participant_list_file_path) as participant_list_file:
        csv_reader = csv.reader(participant_list_file, delimiter=',')
        for row in csv_reader:
            participants.append(Participant(row[0], row[1]))

    return participants


def generate_santa_pairings(participants: [Participant]) -> [SantaPair]:
    """
    Assigns pairs of givers and receivers randomly from a list of participants
    and returns them.

    :param participants: the participants in the secret santa.
    :return: a list of SantaPair NamedTuple's representing the secret santa
        pairings.
    """
    santa_pairings: [SantaPair] = []

    random.shuffle(participants)

    for i in range(len(participants)):
        giver: Participant = participants[i]
        receiver: Participant = participants[(i + 1) % len(participants)]
        santa_pairings.append(SantaPair(giver, receiver))

    return santa_pairings
