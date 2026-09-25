"""templates/activities

Templates for `Activity` objects in journal entries and other org-mode documents.
@date:     2026-07-31
"""
__version__ = "0.1"
__author__  = "n-rosenthal"


ACTIVITIES_TABLE_HEADER: str = '| ID | Begin | End | Title | Description | Tags |\n|----+-------+-----+-------+-------------+------|'
"""Template para o header da TABELA de ATIVIDADES, atualmente renderizada como uma SECÇÃO do DIÁRIO."""

def get_activity_row(**args: str) -> str:
    """Aplica a template sobre um DICT[STR, STR] para gerar um REGISTRO em uma TABELA de ATIVIDADES com os ARGUMENTOS passados."""
    return (
        f"| {args['identifier']} | "
        f"{args['btime']} | "
        f"{args['etime']} | "
        f"{args['title']} | "
        f"{args['description']} | "
        f"{args['tags']} |\n"
    )

def get_duration(btime: str, etime: str) -> str:
    # Split "08h30" into string pieces
    split = lambda a: a.split('h')
    b_h_str, b_m_str = split(btime)
    e_h_str, e_m_str = split(etime)

    # Convert to integers for math operations
    b_h, b_m = int(b_h_str), int(b_m_str)
    e_h, e_m = int(e_h_str), int(e_m_str)

    # Calculate initial differences
    h = e_h - b_h
    m = e_m - b_m

    # Handle minute borrow condition
    if m < 0:
        m += 60
        h -= 1

    # Format output back into the "01h15" structure
    return f"{h:02d}h{m:02d}"

from datetime import datetime

def now() -> str:
    # Formats to: [2026-07-31 Fri 14:07]
    return datetime.now().strftime("<%Y-%m-%d %a %H:%M>")

def get_activity_entry(**args) -> str:
    """Generates a structured Org-mode activity log string."""
    return f"""*** [{args['identifier']}] ({args['btime']}, {args['etime']}) {args['title']} [{args['tags']}]
    :PROPERTIES:
    :ID:         {args['identifier']}
    :DOCTYPE:    ActivityEntry
    :DURATION:   {get_duration(args['btime'], args['etime'])}
    :TAGS:       {args['tags']}
    :CDATE:      {now()}
    :END:

    {args['description']}
    """


if __name__ == "__main__":
    # Package sample payload dictionary arguments
    sample_activity = {
        "identifier": "act-94827",
        "btime": "08h45",
        "etime": "11h15",
        "title": "Refactor Legacy Database Modules",
        "tags": "work:backend:python",
        "description": "Cleaned up old raw SQL queries. Replaced them with typed ORM calls. Optimized performance indexes."
    }

    # Unpack the dictionary key-value arguments using the ** syntax
    entry_output = get_activity_entry(**sample_activity)
    
    print(entry_output)
