from post_class import POST  # Import POST from the new module

def read_post_file(filename):
    POSTS_LIST = []
    print(f"[DEBUG] Reading file: {filename}")  # Debug message
    try:
        with open(filename, 'r') as fd:
            for line in fd:
                line = line.strip()
                print(f"[DEBUG] Line read: {line}")  # Debug message
                if not line:  # Skip empty lines
                    continue
                try:
                    subreddit, title, url, schedule = line.split('~')
                    post = POST('queue', schedule, subreddit, title, url, 0)
                    POSTS_LIST.append(post)
                except ValueError as e:
                    print(f"Error parsing line: {line} | {e}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    return POSTS_LIST

