import os
from enums import SimMode
from utils import create_dirs
import json
from config import TOTAL_TRIALS


class Serialize:
    def __init__(self, curr_mode: SimMode = SimMode.HUMAN):
        self.curr_mode = curr_mode
        self.curr_mode_name: str = curr_mode.name.lower()
        self.trial_num = 1
        self.base_data_dir: str = './data'

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
            'mem_space': mem_space,
            'exec_time': exec_time,
        }

        # path example: ./data/bfs/bfs_trial_1.json
        data_path: str = os.path.join(self.base_data_dir, self.curr_mode_name,
                                      f'{self.curr_mode_name}_trial_{self.trial_num}.json')

        # write the data to the JSON file in the specified path
        with open(f'./data/{self.curr_mode.name.lower()}/data.json', 'w') as f:
            json.dump(data, f)
            f.close()

        # if the Serialize object's trial number is not the total trial number, increment it for the next loop
        if self.trial_num != TOTAL_TRIALS:
            self.trial_num += 1
