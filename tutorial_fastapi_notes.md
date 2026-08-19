# FastApi official Tutorial
## UV Setup
1. uv init project folder
  uv init project_name --bare
2. cd and uv add "fastapi[standard]"

## UV setup in existing directory
uv init
uv init path/to/existing-dir

## Run dev server
uv run fastapi dev [path.py]  // looks for main.py, app.py, api.py, app/main, app/app app/api

## Configure entrypoint in .toml file
[tool.fastapi]
entrypoint = "main:app"

## Deploy
uv run fastapi deploy
### update deploy
uv lock is there are new dependencies
uv run fastapi deploy
