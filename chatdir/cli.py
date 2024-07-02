import click
import os
from chatdir.core.chat import ChatManager
from chatdir.core.file_handler import FileHandler
from chatdir.core.llm_local import LocalLLM
from chatdir.core.llm_api import APILLM
from chatdir.core.vector_db import VectorDB
from chatdir.utils.config import Config
from chatdir.utils.logger import setup_logger


@click.group()
@click.option('--config', type=click.Path(exists=True), help="Path to custom config file.")
@click.pass_context
def cli(ctx, config):
    """Chat with files in a directory."""
    try:
        config = Config.load_config(config)
        logger = setup_logger(config['logging'])
        ctx.ensure_object(dict)
        ctx.obj['config'] = config
        ctx.obj['logger'] = logger
        ctx.obj['file_handler'] = FileHandler(config['file_path'])
        ctx.obj['vector_db'] = VectorDB(config['vector_db_path'])
        ctx.obj['local_llm'] = LocalLLM(config['local_llm'])
        ctx.obj['api_llm'] = APILLM(config['api_llm'])
    except Exception as e:
        click.echo(f"Error initializing ChatDir: {str(e)}", err=True)
        ctx.exit(1)


@cli.command()
@click.argument('directory', type=click.Path(exists=True))
@click.option('--use-api', is_flag=True, help="Use API-based LLM instead of local LLM.")
@click.option('--model', help="Specify a particular model to use.")
@click.pass_context
def chat(ctx, directory, use_api, model):
    """Chat with files in the specified DIRECTORY."""
    try:
        file_handler = ctx.obj['file_handler']
        vector_db = ctx.obj['vector_db']
        local_llm = ctx.obj['local_llm']
        api_llm = ctx.obj['api_llm']
        logger = ctx.obj['logger']

        file_handler.set_directory(directory)
        files = file_handler.list_files()

        if not files:
            click.echo(f"No files found in directory: {directory}")
            ctx.exit(0)

        if use_api:
            llm = api_llm
        else:
            llm = local_llm

        if model:
            llm.set_model(model)

        chat_manager = ChatManager(files, llm, vector_db)
        logger.info(f"Starting chat session with {'API-based' if use_api else 'local'} LLM.")
        chat_manager.start_chat()
    except Exception as e:
        click.echo(f"Error during chat session: {str(e)}", err=True)
        ctx.exit(1)


@cli.command()
@click.pass_context
def list_models(ctx):
    """List available models for both local and API-based LLMs."""
    local_llm = ctx.obj['local_llm']
    api_llm = ctx.obj['api_llm']

    click.echo("Available Local Models:")
    for model in local_llm.list_models():
        click.echo(f"  - {model}")

    click.echo("\nAvailable API Models:")
    for model in api_llm.list_models():
        click.echo(f"  - {model}")


@cli.command()
@click.argument('directory', type=click.Path(exists=True))
@click.pass_context
def index(ctx, directory):
    """Index files in the specified DIRECTORY."""
    try:
        file_handler = ctx.obj['file_handler']
        vector_db = ctx.obj['vector_db']
        logger = ctx.obj['logger']

        file_handler.set_directory(directory)
        files = file_handler.list_files()

        if not files:
            click.echo(f"No files found in directory: {directory}")
            ctx.exit(0)

        click.echo(f"Indexing {len(files)} files...")
        vector_db.index_files(files)
        click.echo("Indexing complete.")
    except Exception as e:
        click.echo(f"Error during indexing: {str(e)}", err=True)
        ctx.exit(1)


if __name__ == "__main__":
    cli()