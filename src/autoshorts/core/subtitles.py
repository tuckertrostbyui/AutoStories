from .models import AudioFile, SubtitleFile


class SubtitleGenerator:
    def generate(self, text: str, audio: "AudioFile") -> "SubtitleFile":
        """Align text with audio and return subtitles"""
        raise NotImplementedError
