# TheRiddler

Discord bot that serves random riddles on command.

# Development

It is recommended to use a Python virtual environment.

### Set Environment

| Name                 | Required | Default             | Description |
|----------------------|----------|---------------------|-------------|
| BASE_RIDDLES_API_URL | &#9745;  |                     | The base API URL to retrieve riddles from. |
| DISCORD_BOT_TOKEN    | &#9745;  |                     | The token of the R6 Stats Discord Bot. |
| LOG_LEVEL            |          | `INFO`              | Level of logging to display/save. Can be one of `DEBUG`, `INFO`, `WARN`, `ERROR` |

### Install Dependencies

`poetry install --with dev`

### Activate Bot

`python -m bot`
