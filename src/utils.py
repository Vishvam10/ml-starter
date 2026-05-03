from __future__ import annotations

import random
from datetime import datetime
from pathlib import Path

import numpy as np
import torch
import yaml


def now_str() -> str:
    return datetime.now().strftime("%Y-%m-%d-%H-%M")


def load_config(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def set_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def get_experiment_name(config: dict) -> str:
    return config.get("experiment", {}).get("name", "ml-exp")


def make_run_dir(config: dict) -> Path:
    model_name = get_experiment_name(config)
    run_dir = Path("artifacts") / model_name / now_str()
    run_dir.mkdir(parents=True, exist_ok=True)
    return run_dir