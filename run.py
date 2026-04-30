from ordotools import LiturgicalCalendar
# from rich import print  ## this "pretty prints" the exiting print statements
from rich.console import Console
from rich.table import Table
# from rich import box

# TODO: turn the entire run into a class and we can choose the output

console = Console()

# TODO: we need to add the language
data = LiturgicalCalendar(2025, "roman", "la").build()

# TODO: I don't think that this is working...
truncate = lambda s: s if len(s) <= 20 else s[:17] + "..."


def num_coms(feast):
    if feast.com_1["name"] is None:
        return "0"
    elif feast.com_2["name"] is None:
        return "1"
    elif feast.com_3["name"] is None:
        return "2"
    else:
        return "3"


table = Table(
    show_header=True,
    header_style="bold red",
    expand=True,
    row_styles=['dim', 'none']
)

# Feasts and number of commemoratins
table.add_column("Date", width=12)  # style="dim", width=12)
table.add_column("Feast Name")
table.add_column("Rank", justify="center")
table.add_column("Verbose Rank", justify="left")
table.add_column("Commemorations", justify="left")
# table.add_column("2 Com", justify="left")
# table.add_column("3 Com", justify="left")

for feast in data:

    if feast.date.strftime("%a") == "Sun":
        table.add_section()

    first_com = ""

    try:
        first_com = feast.commemorations[0]["id"]
    except IndexError:
        first_com = ""

    # feasts and number of commemorations
    table.add_row(
        feast.date.strftime('%b %d, %Y'),
        # truncate(feast.name),
        feast.id,  # TODO: this has to be the feast eventually...
        str(feast.rank_numeric),
        feast.rank_verbose,
        # TODO: we have renamed our commemoriations to be a list...
        str(first_com)
    )

console.print(table)
