#!/bin/bash
source /home/iccd332-josune/miniforge3/etc/profile.d/conda.sh  # Ruta a mamba.sh
eval "$(conda shell.bash hook)"
conda activate iccd332
python MarburgWeather/main.py
