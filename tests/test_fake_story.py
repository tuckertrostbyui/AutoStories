def test_fake_story_source_returns_story():
    from autoshorts.adapters.fake_story import FakeStorySource

    src = FakeStorySource(min_chars=10, max_chars=2000)
    story = src.get_story()

    assert story.source == "fake"
    assert len(story.text) > 0
