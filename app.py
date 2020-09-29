from services.reddit import get_client

reddit = getClient()
subreddit = reddit.subreddit("wallstreetbets")
posts = subreddit.hot(limit=10)


for post in posts:
    print("Post -----------------")
    print(post.title)     # Output: the post's title
    print(post.score)     # Output: the post's score
    print(post.selftext)  # Output: the post's selftext
    print(post.url)       # Output: the URL the post points to
                                # or the post's URL if it's a self post
    print("Top Comment ----------")
    comment = post.comments[0]
    print(comment.author)
    print(comment.score)
    print(comment.body)
