import praw
import time
import datetime
import os

# Function to authenticate with Reddit API
def authenticate():
    print("[+] Authenticating to Reddit...")
    try:
        reddit = praw.Reddit(
            username="Good-Improvement1044",    # Replace with your Reddit username
            password="Rihaan123@",    # Replace with your Reddit password
            client_id="zkCvo1xhyAVwxmNb8-L7bw",         # Replace with your client ID
            client_secret="TuwY0y7QbUOWTuoC0hXXaqa786UJDw", # Replace with your client secret
            user_agent="u/Good-Improvement1044"   # Descriptive user agent
        )
        print(f"[+] Authentication successful as {reddit.user.me()}")
        return reddit
    except Exception as e:
        print(f"[!] Authentication failed: {e}")
        exit(1)

# Function to read posts from a file
def read_post_file(file_path):
    posts = []
    if not os.path.exists(file_path):
        print(f"[!] Error: File '{file_path}' does not exist.")
        return posts

    try:
        print(f"[DEBUG] Reading file: {file_path}")
        with open(file_path, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    # Format: subreddit~title~url~schedule
                    subreddit, title, url, schedule = line.split("~")
                    posts.append({
                        'subreddit': subreddit.strip(),
                        'title': title.strip(),
                        'url': url.strip(),
                        'schedule': schedule.strip()
                    })
                except ValueError:
                    print(f"[!] Skipping invalid line (incorrect format): {line}")
    except Exception as e:
        print(f"[!] Error reading file: {e}")
    return posts

# Function to calculate scheduled time
def calculate_schedule_timestamp(schedule):
    now = datetime.datetime.now()
    if schedule.startswith("+"):
        try:
            value, unit = int(schedule[1:-1]), schedule[-1]
            if unit == "m":
                return now + datetime.timedelta(minutes=value)
            elif unit == "h":
                return now + datetime.timedelta(hours=value)
            else:
                print(f"[!] Unknown time unit in schedule: {schedule}")
        except ValueError:
            print(f"[!] Invalid schedule format: {schedule}")
    elif schedule.lower() == "immediate":
        return now
    else:
        print(f"[!] Unsupported schedule format: {schedule}")
    return None

# Function to submit posts to Reddit
def post_to_reddit(reddit, subreddit_name, title, url):
    try:
        subreddit = reddit.subreddit(subreddit_name)
        if url.lower() == "no url" or not url:
            print(f"[+] Submitting text post to r/{subreddit_name}: '{title}'")
            submission = subreddit.submit(title, selftext="")
        else:
            print(f"[+] Submitting link post to r/{subreddit_name}: '{title}' | {url}")
            submission = subreddit.submit(title, url=url)
        print(f"[+] Post successful! View it here: {submission.url}")
    except Exception as e:
        print(f"[!] Error posting to r/{subreddit_name}: {e}")

# Main function to coordinate the posting process
def main():
    # Authenticate with Reddit
    reddit = authenticate()

    # Path to the post file
    postfile_path = "postfile.txt"
    posts = read_post_file(postfile_path)

    if not posts:
        print("[!] No valid posts found. Exiting.")
        return

    for post in posts:
        subreddit = post['subreddit']
        title = post['title']
        url = post['url']
        schedule = post['schedule']

        # Calculate when to post
        post_time = calculate_schedule_timestamp(schedule)
        if not post_time:
            print(f"[!] Skipping post with invalid schedule: {schedule}")
            continue

        current_time = datetime.datetime.now()
        wait_time = (post_time - current_time).total_seconds()

        if wait_time > 0:
            print(f"[+] Scheduled to post to r/{subreddit} at {post_time} ({wait_time:.2f} seconds from now)")
            time.sleep(wait_time)
        else:
            print(f"[+] Posting immediately to r/{subreddit}")

        # Submit the post
        post_to_reddit(reddit, subreddit, title, url)

if __name__ == "__main__":
    main()

