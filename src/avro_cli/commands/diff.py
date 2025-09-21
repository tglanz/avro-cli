import click

from avro_cli.services.diff_service import DiffService


@click.command()
@click.argument("file1", type=click.Path(exists=True))
@click.argument("file2", type=click.Path(exists=True))
@click.option(
    "--mode",
    type=click.Choice(["data", "schema"]),
    default="data",
    help="What to diff: data or schema (default: data)",
)
def diff(file1: str, file2: str, mode: str):
    try:
        service = DiffService(file1, file2)

        if mode == "schema":
            diff_lines = service.diff_schemas()
        else:
            diff_lines = service.diff_data()

        if diff_lines:
            for line in diff_lines:
                click.echo(line, nl=False)
        else:
            click.echo("No differences found.")

    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)
        raise click.Abort()
