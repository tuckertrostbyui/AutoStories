from .models import AudioFile, SubtitleFile, VideoClip, VideoFile


class VideoCompositor:
    def compose(
        self, audio: "AudioFile", subtitles: "SubtitleFile", broll: "VideoClip"
    ) -> "VideoFile":
        """Merge everything into a final video edit"""
        raise NotImplementedError
