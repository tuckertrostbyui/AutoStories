from .models import VideoFile


class Uploader:
    def upload(self, video: "VideoFile") -> str:
        """Upload video and return platform ID"""
        raise NotImplementedError
