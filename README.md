This is my blog. I set things up a decade ago and so things are jank. It's mostly fine

# 1. Running Locally
```
bundle install
bundle exec jekyll s
```

# 2. Adding a new post
```
python new_post.py "Title of new post"
```
# 3. Publishing

So this is the tricky bit! Turns out we now have two different repos.

You want `https://github.com/AlexeyMK/alexeymk.github.com`

Basically, take _site and push it to master on that repo.

I have limited faith in `publish.sh` but if you're feeling generous, you could make it work again
