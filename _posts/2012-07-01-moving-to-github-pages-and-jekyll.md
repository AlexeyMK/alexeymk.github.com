---
layout: post
title: Migrating from Posterous to Jekyll on GitHub Pages
published: true
date: :2012-07-01 23:30:00
tags:
- technical
- writing
---

I may be a bit late to the [Jekyll](http://jekyllrb.com) party, but with Posterous being acquired by twitter a few months ago, I figured why not try it out. Two weekends later I've migrated enough that I'm comfortable shipping, though I imagine a bunch of silly bugs will remain. Please [email me](mailto:alexey-at-alexeymk.com) with any issues you find, and I'll get to them when I can.

In the meantime...

#### Moving from Posterous to Jekyll: What you need to know.

- **[Jekyll](http://jekyllrb.com)** is a static site generator created by GitHub for GitHub Pages.  It is rather extensible, so people have built things like [Jekyll-Bootstrap](http://str8.to/jekyll-boostrap) and [Octopress](http://str8.to/jekyll-octopress) on top of it.  I sort of half-used the former (adapted a theme) and didn't know about the latter until it was too late.  Maybe/probably use Octopress if you go this route.
- **Migrating from Posterous** kinda-sorta works.  The migrator that includes images/permalinks is [on github here](https://github.com/pepijndevos/jekyll/blob/patch-1/lib/jekyll/migrators/posterous.rb).  Some ruby required.  Here's [my hacky version](https://github.com/AlexeyMK/alexeymk.github.com/blob/master/posterous_import.rb), with a couple of updates.
- **Comments** I haven't moved mine yet but a [guide to move posterous comments to disqus](http://blog.jrmoran.com/blog/2012/01/31/importing-posterous-comments-into-disqus/) is available.  The decision to have comments (even moderated ones) is not one I've made yet. We'll see.
- **RSS** Here's the [jekyll+feedburner guide](http://recursive-design.com/blog/2010/09/14/integrating-jekyll-with-feedburner/)
- **Developing Locally** I used [guard to auto re-generate pages](https://github.com/therabidbanana/guard-jekyll) as I was iterating on the CSS hackery.  Pretty useful, especially if you're already reasonably comfortable with guard.
- **Hosting** GitHub Pages will host for you at yourusername.github.com + let you host on your domain [if you add a CNAME to your distribution](http://imakewebthings.com/blog/github-pages-email/).  I'm about to try it.  Fingers crossed.  Also, I don't know how much I trust GitHub to be so generous in the long run, but my next migration is going to be far less painful - "it's just static content".  **Note**: I was worried about where to stick draft posts, since the repo needs to be public, and my solution was to have both a public and a private repository, so releasing is "git commit -a && git push public master."
- **Markdown** I admit I'm not too experienced with Markdown. Here's [my cheatsheet](http://nestacms.com/docs/creating-content/markdown-cheat-sheet).
