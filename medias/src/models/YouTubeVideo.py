#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""models/YouTubeVideo.py

Data model for the programatic extraction of data from YouTube videos.
@date:     2026-07-29
"""

__version__ = "0.1"
__author__  = "n-rosenthal"

from dataclasses import dataclass


@dataclass
class YouTubeVideo:
    # título do vídeo
    title: str

    # autor (nome do canal)
    author: str

    # data de publicação
    publishing_date: str

    # duração, em segundos
    duration: int

    # URL para o vídeo
    video_url: str

    # URL para o canal
    channel_url: str

    def to_dict(self) -> dict:
        return {"title": self.title, "author": self.author, "publishing_date": self.publishing_date, "duration": self.duration, "video_url": self.video_url, "channel_url": self.channel_url}
