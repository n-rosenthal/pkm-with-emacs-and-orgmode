#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""extractors/YouTubeVideoExtractor.py

Extracts useful information for media capturing of a YouTube video.
@date:     2026-07-29
"""

__version__ = "0.1"
__author__  = "n-rosenthal"

# Library for downloading YouTube videos and/or getting data
from yt_dlp       import YoutubeDL
from yt_dlp.utils import DownloadError

# Datamodel
from models import YouTubeVideo

# Options for only getting metadata and not downloading the video
YDL_OPTIONS = {
    "quiet":         True,
    "skip_download": True,
}

def extract(url: str) -> YouTubeVideo | None:
    """Given an URL to a YouTube video, returns a data model containing the information currently needed for capturing the media/youtube-video

    Args:
        :param url: URL of a YouTube videos
        :type  url: str
    
    Returns:
        :returns:   dataclass model for YouTube videos or None
        :rtype:     YouTubeVideo | None
    
    Raises:
        DownloadError, if the URL is invalid
    """
    with YoutubeDL(YDL_OPTIONS) as ydl:
        try:
            data = ydl.extract_info(url, download=False);
        except DownloadError as e:
            print(f"[media-logging::YouTubeVideoExtractor::extract() ERROR]: {e}");
            return None;

        # Create a new `YouTubeVideo` instance with the extracted data
        record: YouTubeVideo = YouTubeVideo(title=data["title"], author=data["uploader"], publishing_date=data["upload_date"], duration=data["duration"], video_url=url, channel_url=data["channel_url"]);
        return record;
