#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Types/Types.py

System-defined types for general use in the data models and extrators.
@date:     2026-07-30
"""

__version__ = "0.1"
__author__  = "n-rosenthal"

import random
import string
from dataclasses import dataclass
from datetime    import datetime
from typing      import ClassVar

@dataclass
class JournalEntry:
    HEADING_LEVEL: ClassVar[int] = 2

    identifier: str
    time:       str
    tags:       list[str]
    content:    str
    cdate:      datetime
    mdate:      datetime
    adate:      datetime
    parent:     str

    @property
    def tagstream(self) -> str:
        return ":" + ":".join(self.tags) + ":"

    @property
    def title(self) -> str:
        return f"<{self.time}>"

    @property
    def heading(self) -> str:
        stars = self.HEADING_LEVEL * '*'
        return f"{stars} {self.title} {self.tagstream}"

    @property
    def as_dict(self) -> dict[str, str]:
        return {
            "identifier": self.identifier,
            "time":       self.time,
            "tags":       " ".join(self.tags),
            "content":    self.content,
            "cdate":      self.cdate.isoformat(),
            "mdate":      self.mdate.isoformat(),
            "adate":      self.adate.isoformat(),
            "parent":     self.parent,
        }

class TagStream:
    """List of tags with methods for string formatting""" 
    tags: list[str];

    def __init__(self, tags: str | list[str]) -> None:
        if isinstance(tags, list): 
            self.tags = tags
        elif isinstance(tags, str):
            self.tags = tags.split(" ")
        self._index = 0

    def __str__(self) -> str:
        """String representation in org-mode format of a LIST of TAGS."""
        return ":" + ":".join(self.tags) + ":";

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self) -> str:
        if self._index >= len(self.tags):
            raise StopIteration
        self._index += 1
        
        return self.tags[self._index - 1]

    def contains(self, value: str) -> bool:
        """VERIFIES if the TagStream contains a certain tag VALUE."""
        return value in self.tags

    def remove(self, value: str) -> None:
        """REMOVES a TAG from the TagStream, if it is contained by it"""
        if self.contains(value): self.tags = [t for t in self.tags if t != value]
        
    def prepend(self, value: str) -> None:
        if self.contains(value):
            self.remove(value)
        self.tags = [value] + self.tags

    def append(self, value: str) -> None:
        if self.contains(value):
            self.remove(value)
        self.tags = self.tags + [value]

from typing import ClassVar

@dataclass
class ActivityData:
    """Record describing an activity, decoupled from its own table representation."""

    # Unique identifier for a activity
    # Currently expects the temporal identifier (`tid`)
    identifier: str

    # timestamps for the beggining and end of the activity
    btime: str
    etime: str

    # description
    description: str

    # tags that categorize the activity
    tags: list[str]

    # SQL statement for creating the corresponding table.
    # ClassVar: not a dataclass field, so it doesn't affect __init__ or field ordering.
    sql_create: ClassVar[str] = """
CREATE TABLE IF NOT EXISTS activity_data (
    identifier  TEXT PRIMARY KEY,
    btime       TEXT NOT NULL,
    etime       TEXT NOT NULL,
    description TEXT,
    tags        TEXT
);
"""

    def to_dict(self) -> dict[str, str]:
        tags = " ".join(self.tags);
        return { "identifier": self.identifier, "btime" : self.btime, "etime" : self.etime, "description" : self.description, "tags": tags }
