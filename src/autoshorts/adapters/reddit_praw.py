# This adapter grabs a story from reddit

import os
import praw
from autoshorts.core.models import Story
from autoshorts.core.story import StorySource
from autoshorts.core.ai.gemini_rewrite import rewrite_title_text


class RedditStorySource(StorySource):
    def __init__(
        self,
        *,
        subreddit: str,
        sort: str = "top",
        time_filter: str = "day",
        limit: int = 1,
        allow_nsfw: bool = False,
        min_chars: int = 300,
        max_chars: int = 3000,
        use_gemini: bool = True,
        gemini_model: str = "gemini-2.5-flash",
    ):
        self.subreddit = subreddit
        self.sort = sort
        self.time_filter = time_filter
        self.allow_nsfw = allow_nsfw
        self.min_chars = min_chars
        self.max_chars = max_chars
        self.use_gemini = use_gemini
        self.gemini_model = gemini_model

        self._reddit = praw.Reddit(
            client_id=os.environ["REDDIT_CLIENT_ID"],
            client_secret=os.environ["REDDIT_CLIENT_SECRET"],
            user_agent=os.environ["REDDIT_USER_AGENT"],
        )

    def get_story(self) -> Story:
        sub = self._reddit.subreddit(self.subreddit)

        if self.sort == "top":
            posts = sub.top(self.time_filter, limit=1)
        elif self.sort == "hot":
            posts = sub.hot(limit=1)
        elif self.sort == "best":
            posts = sub.best(limit=1)
        elif self.sort == "new":
            posts = sub.new(limit=1)
        else:
            posts = sub.rising(limit=1)

        candidates = list(posts)
        if not candidates:
            raise RuntimeError("No Posts Returned")

        post = candidates[0]

        body = (post.selftext or "").strip()
        if not body:
            raise RuntimeError("Post has no body text")
        if not self.allow_nsfw and getattr(post, "over_18", False):
            raise RuntimeError("Post is NSFW")
        if not (self.min_chars <= len(body) <= self.max_chars):
            raise RuntimeError("Post length is outside allowed range")

        title = str(post.title or "").strip()

        if self.use_gemini:
            ai_title, ai_text = rewrite_title_text(title, body, self.gemini_model)

        return Story(
            id=str(post.id),
            title=str(post.title or "").strip(),
            text=body,
            subreddit=str(post.subreddit),
            author=str(post.author),
            score=int(post.score),
            ai_title=ai_title,
            ai_text=ai_text,
        )
