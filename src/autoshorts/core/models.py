from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional


# ---- Stories -----------------------------------


@dataclass
class Story:
    """The text we will narate, plus useful metadata"""

    id: str
    title: str
    text: str
    subreddit: str
    author: Optional[str] = None
    url: Optional[str] = None
    nsfw: bool = False
    est_read_seconds: Optional[float] = None
    subreddit: Optional[str] = None
    score: Optional[int] = None
    ai_title: Optional[str] = None
    ai_text: Optional[str] = None


# ---- Audio -----------------------------------


@dataclass
class AudioFile:
    """A rendered narration on disk"""

    path: Path
    duration_sec: float
    sample_rate: int = 44100
    channels: int = 2


# ---- Subtitles -----------------------------------


@dataclass
class SubtitleLine:
    """One caption line with timecodes"""

    start_sec: float
    end_sec: float
    text: str


@dataclass
class SubtitleFile:
    """The subtitles file on disk"""

    path: Path
    format: str = "srt"
    lines: List[SubtitleLine] = field(default_factory=list)


# ---- Video -----------------------------------


@dataclass
class VideoClip:
    """A background (b-roll) clip to overlay with audio and captions"""

    path: Path
    duration_sec: float
    width: int
    height: int
    fps: int


@dataclass
class VideoFile:
    """The final exported video"""

    path: Path
    duration_sec: float
    width: int
    height: int
    fps: int
