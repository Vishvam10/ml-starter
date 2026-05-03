from __future__ import annotations

import typer
from rich.console import Console

from src.evaluate import evaluate
from src.predict import predict
from src.train import train
from src.utils import load_config

app = typer.Typer()
console = Console()


@app.command()
def run() -> None:
    print("Hello from ml-starter!")


@app.command()
def train_cmd(config: str = "configs/default.yaml") -> None:
    cfg = load_config(config)
    run_dir = train(cfg)
    console.print(f"[bold green]saved to[/bold green] {run_dir}")


@app.command()
def eval_cmd(config: str = "configs/default.yaml") -> None:
    cfg = load_config(config)
    acc = evaluate(cfg)
    console.print(f"[bold blue]accuracy:[/bold blue] {acc:.4f}")


@app.command()
def predict_cmd(config: str = "configs/default.yaml") -> None:
    cfg = load_config(config)
    predict(cfg)


if __name__ == "__main__":
    app()