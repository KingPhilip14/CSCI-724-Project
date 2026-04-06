import base64
import os
import unittest
import json

import serialize
import utils
from enums import SimMode
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

    def test_serialize_and_data_read(self) -> None:
        """
        Checks if the `human_trial_1.json` file is created and contains the expected data. Then read it with the
        get_json_data function.
        :return: None
        """
        self.serialize.serialize(self.score, self.turns, self.mem_space, self.exec_time)

        data_path: str = utils.get_data_file_path(self.serialize.curr_mode_name, self.serialize.trial_num)

        # test if the json file was created
        self.assertTrue(os.path.exists(data_path))

        # read the data from the file and test if it matches what was written
        data = self.serialize.get_json_data()

        self.assertEqual(data['score'], self.score)
        self.assertEqual(data['turns'], self.turns)
        self.assertEqual(data['mem_space'], self.mem_space)
        self.assertEqual(data['exec_time'], self.exec_time)


    def test_get_json_data_raised_error(self) -> None:
        """
        Checks if the dijk_trial_1.json file is created, fails, then evaluates the exception message.
        """
        # use an enum that doesn't have an existing file
        self.serialize: Serialize = Serialize(curr_mode=SimMode.DIJK)

        data_path: str = utils.get_data_file_path(self.serialize.curr_mode_name, self.serialize.trial_num)

        with self.assertRaises(FileNotFoundError) as e:
            self.serialize.get_json_data()
        self.assertEqual(str(e.exception), f'File in path "{data_path}" does not exist')
