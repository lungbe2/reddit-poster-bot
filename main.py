def main():
    # Parsing command line options
    parser = optparse.OptionParser()
    parser.add_option('--dry-run', action="store_true", default=False, help='Dry run mode. No posts will be submitted.')
    parser.add_option('--quit-after', action="store_true", default=False, help='Quit after posting everything.')
    parser.add_option('--command-after', action="store", dest="command", help='Command to execute after all posts are done.')
    parser.add_option('--subreddit', action="store", dest="subreddit", help='Subreddit to operate on.')
    parser.add_option('--best', action="store_true", default=False, help='Print the best time to post in subreddit.')
    parser.add_option('--new', action="store", dest='new', help='Get the first N new posts of subreddit.')
    parser.add_option('--search', action="store", dest='search', help='Search for terms in subreddit.')

    (options, values) = parser.parse_args()

    OPT_DRY_RUN = options.dry_run
    OPT_QUIT = options.quit_after
    OPT_CMD_AFTER = options.command
    OPT_SUBREDDIT = options.subreddit
    OPT_BEST = options.best
    OPT_SEARCH = options.search
    OPT_NEW = options.new

    MyPrint = Print()

    if OPT_DRY_RUN:
        MyPrint.alert('[+] Dry run mode: No posts will be made.')
        
        # Load posts from postfile.txt
        POSTS_LIST = read_post_file(POST_FILE)

        if not POSTS_LIST:
            MyPrint.warn("[+] No posts found in postfile.txt. Check the file content and format.")
            sys.exit()

        # Print loaded posts
        for post in POSTS_LIST:
            print(f"""
[+] Post Details:
Subreddit: {post.get_subreddit()}
Title: {post.get_title()}
URL: {post.get_url()}
Schedule: {post.get_schedule()}
""")
        sys.exit()

    # Other functionality (like --best, --new) remains unchanged

