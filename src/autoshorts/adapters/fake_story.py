from autoshorts.core.story import StorySource
from autoshorts.core.models import Story


class FakeStorySource(StorySource):
    def __init__(self, *, min_chars=200, max_chars=1200):
        self.min_chars = min_chars
        self.max_chars = max_chars

    def get_story(self) -> Story:
        text = "This is a fake reddit story for testing"
        return Story(
            id="fake_001",
            title="Fake title for testing",
            text=text,
            source="fake",
            author=None,
            url=None,
            nsfw=False,
            est_read_seconds=45.0,
        )
