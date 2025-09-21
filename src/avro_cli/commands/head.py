import json
import click

from avro_cli.services.avro_service import AvroService


@click.command()
@click.argument("file_path", type=click.Path(exists=True))
@click.option(
    "-n", "--num-records", default=5, help="Number of records to show (default: 5)"
)
def head(file_path: str, num_records: int):
    try:
        service = AvroService(file_path)
        output_data = service.get_head_records(num_records)
        click.echo(json.dumps(output_data, indent=2))
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)
        raise click.Abort()
