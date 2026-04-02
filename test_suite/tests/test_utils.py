import unittest
from mock import patch
from utils import *


class TestUtils(unittest.TestCase):
    """
    Tests the functions defined in utils.py.
    """

    def setUp(self) -> None:
        # not needed for now, but placing it here in case it's needed in the future
        pass

    @patch('utils.os.mkdir')
    @patch('utils.os.path.exists')
    def test_create_all_dirs(self, mock_mkdir, mock_exists) -> None:
        """
        Mocks the dependencies in the `create_dirs` method to determine if all directories are created as expected.
        :param mock_exists:
        :param mock_mkdir:
        :return: None
        """
        mock_exists.return_value = False

        create_dirs()

        self.assertEqual(mock_mkdir.call_count, 1 + len(SIM_MODES))

    @patch('utils.os.mkdir')
    @patch('utils.os.path.exists')
    def test_create_no_dirs(self, mock_exists, mock_mkdir) -> None:
        """
        Mocks the dependencies in the `create_dirs` method to determine if no directories are created since they'd
        exist already.
        :param mock_exists:
        :param mock_mkdir:
        :return: None
        """
        mock_exists.return_value = True

        create_dirs()

        self.assertEqual(mock_mkdir.call_count, 0)
