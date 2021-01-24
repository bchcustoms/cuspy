"""Console script for meursing."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for meursing."""
    click.echo("Meursing is only relevant to certain agri-food commodities being imported to a European Union (EU) country from a 3rd country")
    click.echo("This project is also a proof of concept (PoC) for other customs and trade data-driven initiatives, some open source and some not")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
