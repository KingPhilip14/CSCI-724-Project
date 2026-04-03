import os
from typing import Any

from enums import SimMode
from utils import create_dirs
import json
from utils import get_data_file_path
import base64


class Serialize:
    def __init__(self, curr_mode: SimMode = SimMode.HUMAN):
        self.curr_mode = curr_mode
        self.curr_mode_name: str = curr_mode.name.lower()
        self.trial_num = 1
        self.data_file_path: str = get_data_file_path(self.curr_mode_name, self.trial_num)

    def serialize(self, score: int, turns: int, mem_space: bytes, exec_time: float) -> None:
        """
        Collects all major data points needed for metric analysis and stores them as JSON files in the data directory.
        :param score: The total score gained for the current execution run.
        :param turns: The total turns it took to complete the current execution run.
        :param mem_space: The total memory space used by the used algorithm.
        :param exec_time: The total time it took to complete the current execution run.
        :return: None
        """
        create_dirs()

        # a dictionary that will store all the data to write to the JSON file
        data: dict = {
            'score': score,
            'turns': turns,
            'mem_space': base64.b64encode(mem_space).decode('utf-8'),
            'exec_time': exec_time,
        }

        # write the data to the JSON file in the specified path
        # example: ./data/bfs/bfs_trial_1.json
        with open(self.data_file_path, 'w') as f:
            json.dump(data, f)
            f.close()

    def get_json_data(self) -> dict[str, Any]:
        """
        Reads the data file and returns a dictionary with all the data points collected. Raises an error if the
        file does not exist.
        :return: A dict with all the data points
        """
        path: str = get_data_file_path(self.curr_mode_name, self.trial_num)

        if not os.path.exists(path):
            raise FileNotFoundError(f'File in path "{path}" does not exist')

        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        return {
            'score': data['score'],
            'turns': data['turns'],
            'mem_space': base64.b64decode(data['mem_space']),
            'exec_time': data['exec_time'],
        }
