import sys

sys.path.append('../')
import numpy as np
import torch

from bc_learn.Config import Config
from bc_learn.main import main
from rl_train.Examples import get_example_by_id, get_example_by_name

if __name__ == '__main__':
    torch.manual_seed(2025)
    torch.cuda.manual_seed(2025)
    np.random.seed(2025)

    ex = get_example_by_name('Academic_3D')
    with open(f'../controller/{ex.name}.txt', 'r', encoding='utf-8') as f:
        controller = f.readline()

    opts = {
        'example': ex,
        'lr': 0.1,
        'batch_size': 300,
        'margin': 1,
        'hidden_neurons': [10],
        'activation': ['SKIP']
    }
    config = Config(**opts)
    main(config, controller, epoch=5, l=6, config_fine=(100, 10, 0.5, 500, 10), adaptive_margin=True)
