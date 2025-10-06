from .models import VideoClip


class BrollSelector:
    def pick_clip(self, duration: float) -> "VideoClip":
        """Return a background video clip of the given length"""
        raise NotImplementedError
