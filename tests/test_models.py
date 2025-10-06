# from pathlib import Path
# from autoshorts.core.models import (
#     Story,
#     AudioFile,
#     SubtitleLine,
#     SubtitleFile,
#     VideoClip,
#     VideoFile,
# )


# def test_models_construct():
#     story = Story(id="abc123", title="Test", text="Hello World", source="reddit")
#     assert story.title == "Test"

#     audio = AudioFile(path=Path("out/test.wav"), duration_sec=2.5)
#     assert audio.sample_rate == 44100

#     sub = SubtitleFile(path=Path("out/test.srt"))
#     sub.lines.append(SubtitleLine(0.0, 1.0, "Hello"))
#     assert sub.lines[0].test == "Hello"

#     clip = VideoClip(
#         path=Path("assets/clip.mp4"), duration_sec=3.0, width=1080, height=1920, fps=30
#     )
#     out = VideoFile(path=Path("out/final.mp4"), duration_sec=3.0, width=1080, height=1920, fps=30)
#     assert out.fps == 30
