from __future__ import annotations

import torch

from src.data import get_dataloaders
from src.metrics import compute_accuracy
from src.model import MLP


def evaluate(config: dict) -> float:
    _, test_loader = get_dataloaders(
        config["data"]["root"],
        config["data"]["batch_size"],
        config["data"]["num_workers"],
    )

    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = MLP().to(device)
    model.eval()

    y_true, y_pred = [], []

    with torch.no_grad():
        for x, y in test_loader:
            x = x.to(device)
            logits = model(x)
            preds = logits.argmax(dim=1).cpu().tolist()
            y_pred.extend(preds)
            y_true.extend(y.tolist())

    return compute_accuracy(y_true, y_pred)