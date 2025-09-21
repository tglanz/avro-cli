import json
import click

from avro_cli.services.avro_service import AvroService


@click.command()
@click.argument("file_path", type=click.Path(exists=True))
def inspect(file_path: str):
    try:
        service = AvroService(file_path)
        inspection_data = service.inspect_file()
        click.echo(json.dumps(inspection_data, indent=2))
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)
        raise click.Abort()
