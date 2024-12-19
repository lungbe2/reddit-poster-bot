# post_class.py

class POST:
    def __init__(self, status, schedule, subreddit, title, url, tim):
        self.status = status
        self.schedule = schedule
        self.subreddit = subreddit
        self.title = title
        self.url = url
        self.timestamp = tim

    def get_status(self):
        return self.status

    def get_schedule(self):
        return self.schedule

    def get_title(self):
        return self.title

    def get_url(self):
        return self.url

    def get_timestamp(self):
        return float(self.timestamp)

    def get_subreddit(self):
        return self.subreddit

    def get_hash(self):
        return hash(self.subreddit + self.title + self.url)

    def __str__(self):
        return f"Status: {self.status}\nSche.: {self.schedule}\nSubreddit: {self.subreddit}\nTitle: {self.title}\nURL: {self.url}\nTime: {self.timestamp}"
