---
created: 2022-12-31
description: 社交媒体获取器
tags: #twitter, #mastodon
type: product/done
---

## Project Meta
  - [ ] #canceled #project Get social media about Thread.net and Weibo. [link](https://app.todoist.com/app/task/8852804562) #todoist %%[todoist_id:: 8852804562]%%
    - 利用 RSSHUB + RSSTT 替代
    - [ ] #wait [Introducing Threads: A New Way to Share With Text | Meta (fb.com)](https://about.fb.com/news/2023/07/introducing-threads-new-app-text-sharing/) [link](https://app.todoist.com/app/task/8852804597) #todoist %%[todoist_id:: 8852804597]%%
      - [New App - Threads API Documentation - 开发者帮助论坛 - Meta 开发者 (facebook.com)](https://developers.facebook.com/community/threads/1277329089818470/)
      - [Threads API (coursendy.com)](https://coursendy.com/threads-api)
  - query-table: false
    #+BEGIN_QUERY
    {:title [:h3 "Tasks related to Get social media"]
     :query [:find (pull ?b [*])
       :in $ ?current-page
       :where
       [?p :block/name ?current-page]
       [?b :block/marker ?marker]
    [?p :block/alias ?al]
    (or [?b :block/refs ?p] [?b :block/refs ?al])
    (or
       [(= "NOW" ?marker)]
       [(= "DOING" ?marker)]
       [(= "WAITING" ?marker)]
       [(= "LATER" ?marker)]
    )
    (not [?b :block/page ?p])
    ]
     :inputs [:current-page]
    :result-transform (fn [result]
                        (sort-by (fn [b]
                                   (get b :block/priority "Z")) result))
    :breadcrumb-show? false
    :table-view? false
    }
    #+END_QUERY
  - query-table: false
    #+BEGIN_QUERY
    {:title [:h3 "Checklist"]
     :query (and (todo todo) (page Get social media))
    :result-transform (fn [result]
                        (sort-by (fn [b]
                                   (get b :block/priority "Z")) result))
    :breadcrumb-show? false
    :table-view? false
    }
    #+END_QUERY
## Why
## How
  - [x] #todo  Now the main function is done, which build with [[python]]. Check [Github Gist](https://gist.github.com/bGZo/f3c4876e230308fc3d2b2bc8db9dd55e) [link](https://app.todoist.com/app/task/8852804637) #todoist %%[todoist_id:: 8852804637]%%
```shell
    echo %cd%
    # Dropped to shortcut
    E:\OneDrive\workspace\scripts\get_twitter_mastodon
    # Dropped to source file
    C:\Users\15517\Desktop
```
    - 总结起来就是，拖到文件上执行的时候，目录会切到脚本所在的目录，而执行源文件的时候不会。
      - 切到脚本所在的目录就会让整个脚本的路径映射正确；
      - 但是如果直接托在源文件，不更改目录的话，文件映射失败，执行错误；
    - > First, %~dp0 can only be used in bat file while %CD% can be used on command line.
      Second, for %CD%, the **current directory** means the directory when executing the command line or the batch file. For %~dp0, the __current directory__ is the directory where the bat file resides
      — [The difference between %CD% and %~dp0](https://myprogrammingnotes.com/cd-dp0.html)
  - [ ] #wait Use JS/TS rewrite the scripts and build it in web application online. [link](https://app.todoist.com/app/task/8852804743) #todoist %%[todoist_id:: 8852804743]%%
## What
### Design Notes
#### Description / Highlights
#### Input
        - a tweet link
#### Output
        - get a tweet content
      - Do not complete your operation, make other tools to make yourself flow. In case, don't paste in your browser and copy tweet again. Write a tool guys.
        #thought #flow
#### Solution
      - ~~[Give Up] Offical~~
        - The twitter web used the graph SQL. Seem like leetcode, and I don't know how to imitate it.
        - Target repo via [jalalazimi/tweet-fetch: Get Tweet with related data by URL from Twitter in NodeJS](https://github.com/jalalazimi/tweet-fetch)
        - Refs
          - [Twitter Developers](https://developer.twitter.com/en/portal/dashboard)
          - [Tweepy Documentation — tweepy 4.12.1 documentation](https://docs.tweepy.org/en/stable/index.html)
          - [How to get Tweets using Python and Twitter API](https://blog.quantinsti.com/python-twitter-api/)
          - [Use Twitter's API and a Few Command Line Tools to Pick a Random Reply from a Tweet - YouTube](https://www.youtube.com/watch?v=OaPqV0L9kZk)
      - [x] #todo  `[404: This page could not be found](https://tweetpik.com/api/tweets/id`) [link](https://app.todoist.com/app/task/8852804769) #todoist %%[todoist_id:: 8852804769]%%
```python
          import requests
          import re
          base_url = 'https://tweetpik.com/api/tweets'
          f = open ('input')
          line = f.readline()
          while(line):
              split_line = line.split('/')
              url = base_url + '/' + split_line[5]
              url = re.sub(" ", "", url)
              res = requests.get(url, headers={
                  'Accept-Encoding': 'gzip, deflate',
                  'Accept': '*/*',
                  'Connection': 'keep-alive',
                  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38',
              }).json()
              output = open('export', 'a')
              tweet = res['text']
              tweet = re.sub("\n", "\n  ", tweet)
              output.write('- ' + tweet + '\n  by ' + res['name'] + \
                          ' at '+ res['created_at'] +'with likes ' + \
                          str(res['like_count']) + ' & retweet ' + \
                          str(res['retweet_count']) + ' & reply_count '+ \
                          str(res['reply_count']) + 'via: [twitter](https://twitter.com/' + \
                          res['username'] + '/status/' + res['id'] + ');\n')
              if 'media' in res and 'url' in res['media'][0]:
                  for media in res['media']:
                      output.write('  ![]('+ media['url']+')')
                  output.write('\n')
              output.close()
              output = open('output', 'a')
              output.write(str(res)+'\n')
              output.close()
              line = f.readline()
```
```js
          if (res.data.media[0].type == "photo"){}
          if ((res.data.media[0].type == "animated_gif") || (res.data.media[0].type == "video")){}
          url : `${BASE_URL}/${TWEET_ID}/video`
```
          via: [twitter-direct-url/index.js at main · victorsouzaleal/twitter-direct-url · GitHub](https://github.com/victorsouzaleal/twitter-direct-url/blob/main/src/index.js)
      - [ ] #todo **Build a Repo like the above api**, run with Github-Action and your token. [link](https://app.todoist.com/app/task/8852804867) #todoist %%[todoist_id:: 8852804867]%%
        - Github Action + Tweet + Readme
        - **Example**
```
            GET [404: This page could not be found](https://tweetpik.com/api/tweets/1604623830189838337)
            {"id":"1604623830189838337","text":"As a company from eastern Germany, we know that building a wall to try and keep people from leaving isn't a good idea. https://t.co/jxlbO9s0Pk","created_at":"2022-12-18T23:45:08.000Z","like_count":51467,"retweet_count":13773,"reply_count":551,"urls":[{"start":119,"end":142,"url":"https://t.co/jxlbO9s0Pk","expanded_url":"https://twitter.com/TwitterSupport/status/1604531261791522817","display_url":"twitter.com/TwitterSupport…"}],"name":"Mastodon (@Mastodon@mastodon.social)","username":"joinmastodon","profile_image_url":"https://pbs.twimg.com/profile_images/1542256027348918278/7FXNAQK4_normal.jpg","verified":false,"users":[{"profile_image_url":"https://pbs.twimg.com/profile_images/1542256027348918278/7FXNAQK4_normal.jpg","username":"joinmastodon","id":"875882643614814208","verified":false,"name":"Mastodon (@Mastodon@mastodon.social)"}]}
```
        - Search `twitter API`, there is a lot of libraries, so see that next time.
      - [x] #todo  [[html5]] to [[markdown]] [link](https://app.todoist.com/app/task/8852804906) #todoist %%[todoist_id:: 8852804906]%%
        - [How to Convert HTML to Markdown in Python? - GeeksforGeeks](https://www.geeksforgeeks.org/how-to-convert-html-to-markdown-in-python/)
        - [markdownify · PyPI](https://pypi.org/project/markdownify/)]
      - 好像 Python `re.sub` 无法使用定界符，以下代码不生效
```python
          post_content = re.sub(r'\n\n', '\n', md(res['content']))
```
      - [file - What is the perfect counterpart in Python for "while not EOF" - Stack Overflow](https://stackoverflow.com/questions/15599639/what-is-the-perfect-counterpart-in-python-for-while-not-eof)]
#### Alternatives
  - [Python 按键(key)或值(value)对字典进行排序 | 菜鸟教程 (runoob.com)](https://www.runoob.com/python3/python-sort-dictionaries-by-key-or-value.html)
-