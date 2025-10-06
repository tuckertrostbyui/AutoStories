class AnalyticsClient:
    def fetch_stats(self, video_id: str) -> dict:
        """Fetch performance metrics for a video"""
        raise NotImplementedError
