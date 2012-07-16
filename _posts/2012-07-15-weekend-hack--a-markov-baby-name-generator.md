---
layout: post
title: ! 'Weekend Hack: A Markov Baby Name Generator in Jekyll'
published: true
date: 2012-07-15 18:00:11
tags:
- hack
- technical
- parody
---

Had a few hours free this weekend.  Came up with a [Markov Chain](http://en.wikipedia.org/wiki/Markov_chain) baby name generator that comes up with new baby names based on existing popular baby names.  Why not.

**The result**: [Follow @markovbaby on Twitter](http://twitter.com/markovbaby).

<script src="http://storify.com/alexeymk/sample-names.js"></script><noscript>[<a href="http://storify.com/alexeymk/sample-names" target="_blank">View the story "Sample Names" on Storify</a>]</noscript>

What is a Markov Chain?
-----------------------
Read [the wikipedia entry](http://en.wikipedia.org/wiki/Markov_chain) for a more thorough introduction, but in our case, a Markov Chain is a simple random process to generate text that looks sort of like other text.

For example: as we're generating baby names, say we have the letter "C" so far. What characters tend to follow 'c'?  From our sample set of baby names, we know this to be as follows:

<img src="/images/letters_after_c.png"></img>

Pick a 'next' character with the same probability with which it appears. Let's say we picked 'h'. Now we have 'ch', an the process continues: which characters tend to appear after h?  So it goes.

The result are a rather eclectic set of names, and may be suitable for an expecting couple with just the appropriate amount of eccentricity and love of statistics.

The code
--------

[Is available on my github](https://github.com/AlexeyMK/markov-baby-names).  Hopefully nothing too complicated; I got a little fancy with advanced Python features I had been meaning to try.  random.choice and collections.defaultdict proved rather helpful.

<script src="https://gist.github.com/3119751.js"> </script>

Possible extensions
-------------------

- Favorite or RT your favorite baby names, and I'll put up a leaderboard for favorite ones.
- Apply the same techniques (and same code) to startup names, using crunchbase: Markov 2.0.

If you've got a twitter bot missing in your life, [follow @markovbaby on Twitter](http://twitter.com/markovbaby).  Or [follow me](http://twitter.com/alexeymk). That would be cool too.
