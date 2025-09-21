import click

from avro_cli.commands.inspect import inspect
from avro_cli.commands.head import head
from avro_cli.commands.diff import diff


@click.group()
@click.version_option()
def main():
    pass


main.add_command(inspect)
main.add_command(head)
main.add_command(diff)


if __name__ == "__main__":
    main()
