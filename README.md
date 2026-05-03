# ml-template

My minimal PyTorch ML template with training, evaluation, configs, and optional app UIs.

### Setup

```bash
git clone https://github.com/Vishvam10/ml-starter

uv venv --python 3.14.2
uv sync

mkdir -p data/{raw,processed,external} notebooks artifacts/{checkpoints,logs,figures}

# touch data/raw/.gitkeep data/processed/.gitkeep data/external/.gitkeep
# touch notebooks/.gitkeep
# touch artifacts/checkpoints/.gitkeep artifacts/logs/.gitkeep artifacts/figures/.gitkeep
```

### Running Experiments

```bash
python -m src.cli train-cmd --config configs/default.yaml
python -m src.cli eval-cmd --config configs/default.yaml
python -m src.cli predict-cmd --config configs/default.yaml
```

#### Tensorboard

```bash
tensorboard --logdir artifacts/logs
```

### Development

#### Testing

```bash
pytest
```

#### Lint and Format

```bash
ruff check --fix --config pyproject.toml
ruff check --select I --fix . --config pyproject.toml
ruff format --config pyproject.toml
```