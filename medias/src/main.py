import random
import string
from models     import  YouTubeVideo
from Types      import  ActivityData, JournalEntry
from extractors import  extract
from writers    import  compose_YouTubeVideo_activity as compose
from writers    import  write_YouTubeVideo_activity   as write
import random
import string
from dataclasses import dataclass
from datetime    import datetime
from typing      import ClassVar

def String(size: int) -> str:
    """returns a random STRING of given SIZE, using lowercase ascii letters."""
    return "".join(random.choices(string.ascii_lowercase, k=size))


def RandomTags(n: int = 2) -> list[str]:
    """returns a list of N random 'tag-like' strings, for populating test fixtures."""
    return [String(6) for _ in range(n)]


def RandomTimePair() -> tuple[str, str]:
    """returns a (btime, etime) pair in the 'HHhMM' format used across the project."""
    bh, bm = random.randint(0, 22), random.randint(0, 59)
    eh, em = bh + random.randint(0, 1), random.randint(0, 59)
    return f"{bh:02d}h{bm:02d}", f"{min(eh, 23):02d}h{em:02d}"

def TID() -> str:
    return f"2026{random.choices([str(M) for M in range(1, 13)])}{random.choices([str(D) for D in range(1, 31)])}{random.choices([str(h) for h in range(0, 24)])}{random.choices([str(m) for m in range(1, 60)])}"

def Activity() -> ActivityData:
    btime, etime = RandomTimePair()
    return ActivityData(
        identifier=TID(),
        btime=btime,
        etime=etime,
        description=String(16),
        tags=RandomTags(4)
    )

def random_JournalEntry() -> JournalEntry:
    """Builds a JournalEntry with randomized fields, for testing/fixtures."""
    def _rand_str(size: int) -> str:
        return "".join(random.choices(string.ascii_lowercase, k=size))

    now = datetime.now()
    return JournalEntry(
        identifier=TID(),
        time=now.strftime("%H:%M"),
        tags=RandomTags(3),
        content=String(40),
        cdate=now,
        mdate=now,
        adate=now,
        parent=TID(),
    )

if __name__ == '__main__':
    print(Activity());
    print(random_JournalEntry());
