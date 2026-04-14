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
        self.peak_mem: int = 123456789

        self.exec_time: float = 10.0

    def test_serialize_and_data_read(self) -> None:
        """
        Checks if the `human_trial_1.json` file is created and contains the expected data. Then read it with the
        get_json_data function.
        :return: None
        """
        self.serialize.serialize(self.score, self.turns, self.peak_mem, self.exec_time)

        data_path: str = utils.get_data_file_path(self.serialize.curr_mode_name, self.serialize.trial_num)

        # test if the json file was created
        self.assertTrue(os.path.exists(data_path))

        # read the data from the file and test if it matches what was written
        # already tests if not given a specific path
        data = self.serialize.get_json_data()

        self.assertEqual(data['score'], self.score)
        self.assertEqual(data['turns'], self.turns)
        self.assertEqual(data['peak_mem'], self.peak_mem)
        self.assertEqual(data['exec_time'], self.exec_time)

    def test_given_new_path(self) -> None:
        """
        Creates `human_trial_2.json` and `human_trial_3.json`. Then, the specified path to `human_trial_3.json`
        is used to extract data.
        :return:
        """
        # create human_trial_2.json
        self.serialize = Serialize(trial_num=2)
        self.serialize.serialize(self.score + 10, self.turns + 10, self.peak_mem, self.exec_time + 50)
        data_path: str = utils.get_data_file_path(self.serialize.curr_mode_name, self.serialize.trial_num)

        # test if the json file was created
        self.assertTrue(os.path.exists(data_path))

        # create human_trial_3.json
        self.serialize = Serialize(trial_num=3)
        self.serialize.serialize(self.score + 17, self.turns + 5, self.peak_mem, self.exec_time + 30)
        data_path = utils.get_data_file_path(self.serialize.curr_mode_name, self.serialize.trial_num)

        # test if the json file was created
        self.assertTrue(os.path.exists(data_path))

        # read the data from the file and test if it matches what was written
        # already tests if not given a specific path
        data = self.serialize.get_json_data(data_path)

        self.assertEqual(data['score'], self.score + 17)
        self.assertEqual(data['turns'], self.turns + 5)
        self.assertEqual(data['peak_mem'], self.peak_mem)
        self.assertEqual(data['exec_time'], self.exec_time + 30)


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
