from .models import AudioFile


class TTSProvider:
    def speak(self, text: str) -> "AudioFile":
        """Turn text into speech audio"""
        raise NotImplementedError
