from __future__ import annotations

from sklearn.metrics import accuracy_score


def compute_accuracy(y_true, y_pred) -> float:
    return accuracy_score(y_true, y_pred)