import pandas as pd
data = [[1, 'Let us Code'], [2, 'More than fifteen chars are here!']]
tweets = pd.DataFrame(data, columns=['tweet_id', 'content']).astype({'tweet_id':'Int64', 'content':'object'})

"""+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| tweet_id       | int     |
| content        | varchar |
+----------------+---------+
tweet_id is the primary key (column with unique values) for this table.
content consists of characters on an American Keyboard, and no other special characters.
This table contains all the tweets in a social media app.


Write a solution to find the IDs of the invalid tweets. The tweet is invalid if the number of characters used in the content of the tweet is strictly greater than 15.

Return the result table in any order."""

# Approach 1 using for loop
def invalid_tweets1(tweets: pd.DataFrame) -> pd.DataFrame:
    a = []
    for i in range(len(tweets)):
        if len(tweets["content"][i]) > 15:
            a.append(tweets["tweet_id"][i])
    return pd.DataFrame(a , columns = ["tweet_id"])

a = invalid_tweets1(tweets)

# Approach 2 using .str.len() method
def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return tweets[tweets["content"].str.len() > 15][["tweet_id"]]

b = invalid_tweets2(tweets)


"""

The result format is in the following example.
Example 1:

Input: 
Tweets table:
+----------+-----------------------------------+
| tweet_id | content                           |
+----------+-----------------------------------+
| 1        | Let us Code                       |
| 2        | More than fifteen chars are here! |
+----------+-----------------------------------+
Output: 
+----------+
| tweet_id |
+----------+
| 2        |
+----------+
Explanation: 
Tweet 1 has length = 11. It is a valid tweet.
Tweet 2 has length = 33. It is an invalid tweet."""








