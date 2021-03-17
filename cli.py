r"""
Command Line Interface
=======================
   Commands:
   - preprocess: Pre-process the original CSV file, with multiple steps available.
   - getMetadata: Fetch meta-data related to the original dataset.
   - personify: Generate the Persona-Chat formatted file.
"""
import click
from os import cpu_count
from preprocessor import preprocess
from metadataExtractor import getMetadata
from personifier import personify


@click.group()
def cli():
    pass


@cli.command(name="preprocess")
@click.option(
    "--in_filename",
    default="twitter_corpora/twitter/twcs.csv",
    help="CSV input filename",
)
@click.option(
    "--out_filename",
    default="preprocessed.csv",
    help="Preprocessed CSV output filename",
)
@click.option("--emojis", default=True, help="Remove emojis", type=bool)
@click.option("--emoticons", default=True, help="Remove emoticons", type=bool)
@click.option("--urls", default=True, help="Tag URLs -> (URL)", type=bool)
@click.option("--html_tags", default=True, help="Remove html tags", type=bool)
@click.option("--acronyms", default=True, help="Convert acronyms to meaning", type=bool)
@click.option("--spelling", default=False, help="Spellcheck", type=bool)
@click.option("--usernames", default=False, help="Tag usernames", type=bool)
@click.option(
    "--max_workers",
    default=cpu_count(),
    help="Maximum number of workers to spawn",
    type=int,
)
@click.option(
    "--chunksize",
    default=-1,
    help="Size of chunks sent to worker processes",
    type=int,
)
def preprocessCSV(
    in_filename: str,
    out_filename: str,
    emojis: bool,
    emoticons: bool,
    urls: bool,
    html_tags: bool,
    acronyms: bool,
    spelling: bool,
    usernames: bool,
    max_workers: int,
    chunksize: int,
) -> None:

    preprocess(
        in_filename,
        out_filename,
        emojis,
        emoticons,
        urls,
        html_tags,
        acronyms,
        spelling,
        usernames,
        max_workers,
        chunksize,
    )


@cli.command(name="getMetadata")
@click.option(
    "--in_filename", default="twitter_corpora/twitter/twcs.csv", help="CSV filename"
)
def extractMetadata(in_filename: str) -> None:
    getMetadata(in_filename)


@cli.command(name="personify")
@click.option(
    "--in_filename", default="preprocessed.csv", help="Preprocessed CSV filename"
)
@click.option("--brand", default=None, help="Name of the brand ")
@click.option("--limit", default=-1, help="Max number of conversations")
@click.option(
    "--out_filename", default="personaChatCS.json", help="Name of the generated file"
)
def personifyCS(in_filename: str, brand: str, limit: int, out_filename: str) -> None:
    personify(in_filename, out_filename, brand, limit)


if __name__ == "__main__":
    cli()
