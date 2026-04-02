import unittest
from mock import patch
import json
from serialize import Serialize


class TestSerialize(unittest.TestCase):
    """
    Tests the functions defined in serialize.py.
    """

    def setUp(self) -> None:
        self.serialize: Serialize = Serialize()
        self.score: int = 1
        self.turns: int = 5

        # a fake value for testing bytes; no actual significance or relation to the expected mem size
        self.mem_space: bytes = bytes('a', 'utf-8')

        self.exec_time: float = 10.0


    @patch('serialize.json.dump')
    def test_serialize_human_data(self, mock_dump) -> None:
        """
        Mocks the json.dump function used in the serialize object.
        :return: None
        """
        self.serialize.serialize(self.score, self.turns, self.mem_space, self.exec_time)

        self.assertEqual(mock_dump.call_count, 1)
