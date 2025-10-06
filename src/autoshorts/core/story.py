from .models import Story


class StorySource:
    def get_story(self) -> "Story":
        """Return a Story object with text and metadata"""
        raise NotImplementedError
