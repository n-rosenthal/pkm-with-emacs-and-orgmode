#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""writers/YouTubeVideoWriters.py

Applies data extracted from YouTube video URLs to the templates for media logging.
@see:      extractors/YouTubeVideoExtractor
@date:     2026-07-30
"""

__version__ = "0.1"
__author__  = "n-rosenthal"

from Types  import ActivityData, TagStream
from models import YouTubeVideo

def compose_YouTubeVideo_activity(data: YouTubeVideo | dict[str, str], activity_data: ActivityData | dict[str, str]) -> dict[str, str]:
    """Composes the data obtained programatically from a YouTube video with the data necessary to define an `Activity` object"""
    # convert both entries to dicts
    if(type(data) == YouTubeVideo): data = data.to_dict();
    if(type(activity_data) == ActivityData): activity_data = activity_data.to_dict();

    # generate `name` activity field
    name: str = r'media/youtube-video';

    # converts seconds to minutes
    m, s          = divmod(int(data["duration"]), 60);
    duration: str = f'{m}m{s}s';

    # generate `description` activity field
    # in a Activity, the description field specifies the video
    #   it is not properly a description of the contents of the video
    #   but only of it's title and uploader
    description: str = f'{data["title"]} ({data["author"]}, {data["publishing_date"][:4]}, {duration})';

    # `tags` appears as a string of values separated by SPACE
    tags: TagStream = TagStream(activity_data["tags"]);
    
    return { "id" : activity_data["identifier"], "btime" : activity_data["btime"], "etime" : activity_data["etime"], "title" : name, "description" : description, "tags" : tags };

def write_YouTubeVideo_activity(activity: dict) -> str:
    """Returns an `Activity` object formatted as a org-mode table row

    Args
        :param activity: dictionary containing the necessary fields for an activity
        :type  activity: dict[str, str]

    Returns
        :returns:        table row formatted string
        :rtype:          str

    Raises
        :exception:      if `activity` doesn't contain all necessary fields
    """
    # obrigatory fields for an `Activity` object
    activity_fields: list[str] = ['id', 'btime', 'etime', 'title', 'description', 'tags'];

    # checks if param `activity` contains all fields necessary
    for f in activity_fields:
        if f not in activity.keys():
            raise IndexError(f"field {f} not defined");

    # returns the formatted string
    return f"| {activity['id']} | {activity['btime']} | {activity['etime']} | {activity['title']} | {activity['description']} | {str(activity['tags'])} |\n";


