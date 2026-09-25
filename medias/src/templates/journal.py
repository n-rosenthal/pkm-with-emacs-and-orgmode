"""templates/journal

@date:     2026-07-31
"""
__version__ = "0.1"
__author__  = "n-rosenthal"

def get_journal_org_header(**args) -> str:
    return (
        ":PROPERTIES:\n"                          \
        +  f":ID:      {args['org-roam-id']}\n"   \
        +  f":TID:     {args['tid']}\n"           \
        +   ":DOCTYPE: Journal\n"                 \
        +   ":END:")

def get_journal_org_attributes(**args) -> str:
    attributes: dict[str, str] = args['org_attributes']
    diretives : list[str]      = []

    for attribute in attributes.keys():
        diretives.append(f'#+{attribute}: {attributes[attribute]}\n')

    return "".join(diretives)

if __name__ == '__main__':
    JOURNAL_ORG_HEADER__TEST: dict[str, str] = {
        'org-roam-id' : '391c595a-e0dd-46bc-ad8b-e894758f73b0',
        'tid'         : '202607312002'
    }

    JOURNAL_ORG_ATTR__TEST: dict[str, str]   = {
        'org_attributes': {
            'title'       :  '2026-07-31',
            'filetags'    :  ':journal:',
        }
    }

    org_header : str = get_journal_org_header(**JOURNAL_ORG_HEADER__TEST)   \
                    + '\n'                                               \
                    + get_journal_org_attributes(**JOURNAL_ORG_ATTR__TEST) \
                    + '\n'

    print(org_header)

JOURNAL_SECTIONS: dict[str, str] = {
    'sections' : {
          'activities' : r'** atividades',
          'entries'    : r'** entradas',
          'medias'     : r'** mídias'
        }
}

from .activities import ACTIVITIES_TABLE_HEADER

def get_journal_activities(activities: list[dict[str, str]]) -> str:
    from .activities import get_activity_row
    rows = "".join(get_activity_row(**a) for a in activities)
    return (
        JOURNAL_SECTIONS['sections']['activities'] + '\n'
        + ACTIVITIES_TABLE_HEADER + '\n'
        + rows
    )

def get_journal_entry(entry: dict[str, str]) -> str:
    return (
        f"*** <{entry['time']}> {entry['tags']}\n" \
        + ":PROPERTIES:\n"                         \
        + f":ID:         {entry['org-roam-id']}\n" \
        + f":TID:        {entry['tid']}\n"         \
        + ":DOCTYPE:    JournalEntry\n"            \
        + f":CDATE:      {entry['cdate']}\n"       \
        + ":END:\n\n"                              \
        + f"{entry['entry']}\n\n"
    )

def get_journal_entries(entries: list[dict[str, str]]) -> str:
    def sort(entries: list[dict[str, str]], key: str = 'time') -> list[dict[str, str]]:
        entries = list(entries)
        n = len(entries)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if entries[j][key] > entries[j + 1][key]:
                    entries[j], entries[j + 1] = entries[j + 1], entries[j]
                    return entries

    return (
        JOURNAL_SECTIONS['sections']['entries'] \
        + '\n'
        + "".join([get_journal_entry(e) for e in sort(entries)])
    )

if __name__ == '__main__':
    print(get_journal_entries([
        {
            'time'         : '2026-07-31 fri 20:34',
            'org-roam-id'  : '391c595a-e0dd-46bc-ad8b-e894758f73b0',
            'tid'          : '202607312035',
            'tags'         : ':personal-knowledge-management:project/journalling:',
            'cdate'        : '2026-07-31 fri 20:34',
            'entry'        : 'implementando escritores para entradas no diário',
        },
        {
            'time'         : '2026-07-31 fri 21:54',
            'org-roam-id'  : '391c595a-e0dd-46bc-ad8b-e894758f73b0',
            'tid'          : '202607312154',
            'tags'         : ':ego:',
            'cdate'        : '2026-07-31 fri 21:54',
            'entry'        : 'indo dormir',
        },
        {
            'time'         : '2026-07-31 fri 23:15',
            'org-roam-id'  : '391c595a-e0dd-46bc-ad8b-e894758f73b0',
            'tid'          : '202607312315',
            'tags'         : ':ego:',
            'cdate'        : '2026-07-31 fri 23:15',
            'entry'        : 'sonhando!!',
        },                
    ]))
