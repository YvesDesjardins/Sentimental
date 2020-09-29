from services.reddit import getClient

reddit = getClient()

# assume you have a reddit instance bound to variable `reddit`
subreddit = reddit.subreddit("wallstreetbets")

for submission in subreddit.hot(limit=5):
    print("Post -----------------")
    print(submission.title)     # Output: the submission's title
    print(submission.score)     # Output: the submission's score
    print(submission.selftext)  # Output: the submission's selftext
    print(submission.url)       # Output: the URL the submission points to
                                # or the submission's URL if it's a self post
    print("Top Comment ----------")
    comment = submission.comments[0]
    print(comment.author)
    print(comment.score)
    print(comment.body)
