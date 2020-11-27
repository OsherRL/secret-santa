import unittest
from typing import Dict
from unittest.mock import patch, mock_open

from .secret_santa import (
    Participant,
    SantaPair,
    parse_participant_file,
    generate_santa_pairings
)


class SecretSantaTestCase(unittest.TestCase):
    """
    A suite of tests surrounding the secret santa core logic.
    """

    def test_parse_participant_file(self):
        """
        Test that participant file are parsed correctly.
        """
        # Set up the path and data for the mock participant file.
        mock_file_path: str = 'path/to/participant_file.csv'
        mock_file_data: str = 'Participant 1, participant1@email.com\n' \
                              'Participant 2, participant2@email.com\n' \
                              'Participant 3, participant3@email.com\n' \
                              'Participant 4, participant4@email.com\n' \
                              'Participant 5, participant5@email.com\n'

        expected_result: [Participant] = [
            Participant('Participant 1', ' participant1@email.com'),
            Participant('Participant 2', ' participant2@email.com'),
            Participant('Participant 3', ' participant3@email.com'),
            Participant('Participant 4', ' participant4@email.com'),
            Participant('Participant 5', ' participant5@email.com'),
        ]

        # Patch the open() method to return the mock participant file.
        with patch(
            "builtins.open",
            mock_open(read_data=mock_file_data)
        ) as mock_file:
            # Call parse_participant_file with our mock file path to get a
            # list of participant objects
            actual_result: [Participant] = parse_participant_file(
                mock_file_path)

            # Check open was called with the correct file path.
            mock_file.assert_called_with(mock_file_path)

            # Check the participant list returned is as expected.
            self.assertListEqual(expected_result, actual_result)

    def test_generate_santa_pairings(self):
        """
        Test that secret santa pairings are generated correctly.
        """
        participant_list: [Participant] = [
            Participant('Participant 1', ' participant1@email.com'),
            Participant('Participant 2', ' participant2@email.com'),
            Participant('Participant 3', ' participant3@email.com'),
            Participant('Participant 4', ' participant4@email.com'),
            Participant('Participant 5', ' participant5@email.com'),
        ]

        pairings: [SantaPair] = generate_santa_pairings(participant_list)

        # Dictionary to keep track of how many times each participant has
        # been listed as a giver or receiver in the generated pairings.
        participant_pairing_dict: Dict[Participant, Dict[str, int]] = {
            participant: {'giver_count': 0, 'receiver_count': 0}
            for participant in participant_list
        }

        for pair in pairings:
            # Check that no participant is paired with themself.
            self.assertNotEqual(pair.giver, pair.receiver)

            # Populate participant_pairing_dict with correct counts.
            participant_pairing_dict[pair.giver]['giver_count'] += 1
            participant_pairing_dict[pair.receiver]['receiver_count'] += 1

        # Make sure all participants are assigned exactly once as
        # a giver and once as a receiver.
        for count_dict in participant_pairing_dict.values():
            self.assertEqual(1, count_dict['giver_count'])
            self.assertEqual(1, count_dict['receiver_count'])


if __name__ == '__main__':
    unittest.main()
