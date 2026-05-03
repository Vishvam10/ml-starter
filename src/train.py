from __future__ import annotations

from pathlib import Path

import torch
import torch.nn as nn
from rich.console import Console
from safetensors.torch import save_file
from torch.utils.tensorboard import SummaryWriter
from tqdm import tqdm

from src.data import get_dataloaders
from src.model import MLP
from src.utils import make_run_dir, set_seed

console = Console()


def train(config: dict) -> Path:
    set_seed(config["seed"])
    run_dir = make_run_dir(config)

    train_loader, _ = get_dataloaders(
        config["data"]["root"],
        config["data"]["batch_size"],
        config["data"]["num_workers"],
    )

    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = MLP().to(device)
    opt = torch.optim.AdamW(
        model.parameters(),
        lr=config["train"]["lr"],
        weight_decay=config["train"]["weight_decay"],
    )
    criterion = nn.CrossEntropyLoss()
    writer = SummaryWriter(log_dir=run_dir / "logs")

    model.train()
    for epoch in range(config["train"]["epochs"]):
        total_loss = 0.0
        for x, y in tqdm(train_loader, desc=f"epoch {epoch+1}"):
            x, y = x.to(device), y.to(device)
            opt.zero_grad()
            logits = model(x)
            loss = criterion(logits, y)
            loss.backward()
            opt.step()
            total_loss += loss.item()

        avg_loss = total_loss / len(train_loader)
        writer.add_scalar("train/loss", avg_loss, epoch)
        console.print(f"[green]epoch {epoch+1}[/green] loss={avg_loss:.4f}")

    save_file(model.state_dict(), str(run_dir / "model.safetensors"))
    writer.close()
    return run_dir