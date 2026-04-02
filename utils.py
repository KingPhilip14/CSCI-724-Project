import os
from config import SIM_MODES

def create_dirs() -> None:
    """
    Creates the data directory and its subfolders if they don't exist.
    :return: None
    """
    if not os.path.exists('./data'):
        os.mkdir('./data')
        print('Created the missing "data" directory to store serialized data')

    for sim_mode in SIM_MODES:
        if not os.path.exists(f'./data/{sim_mode}'):
            os.mkdir(f'./data/{sim_mode}')
            print(f'Created the missing "{sim_mode}" subdirectory to store serialized data for {sim_mode} data"')