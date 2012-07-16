---
layout: post
title: ! 'Weekend Hack: A Markov Baby Name Generator'
published: true
date: 2012-07-15 18:00:11
tags:
- hack
- technical
- parody
---


My weekend hack is a [Markov Chain](http://en.wikipedia.org/wiki/Markov_chain) baby name generator.  [@MarkovBaby](http://twitter.com/markovbaby) will come up with a new baby name once an hour and tweets it out.

**The result**: [Follow @markovbaby on Twitter](http://twitter.com/markovbaby).

<script src="http://storify.com/alexeymk/sample-names.js"></script><noscript>[<a href="http://storify.com/alexeymk/sample-names" target="_blank">View the story "Sample Names" on Storify</a>]</noscript>

What is a Markov Chain?
-----------------------
Read [the wikipedia entry](http://en.wikipedia.org/wiki/Markov_chain) for a more thorough introduction, but in our case, a Markov Chain is a simple random process to generate text that looks sort of like other text.

For example: as we're generating baby names, say we start with the letter "C".  What should be our next letter?  Well, what kind of letters usually come after a "C" in names?  Let's look through our [list of existing names](https://github.com/AlexeyMK/markov-baby-names/blob/master/boys.txt) and see what usually comes next.

<img src="/images/letters_after_c.png"></img>

Great.  Let's pick the next character at random from within this list, weighing each possibility by how often it appears.  If we get 'end of word', we're done.

But let's say we've picked 'h'.  Great - so far the name starts with a 'ch' - let's look for the next character: what tends to follow an 'h' in our existing names?  And so on.

Results
-------

The result are a rather eclectic set of names.  Some are silly and non-sensical (C, Ieahaholijayson), while others seem pretty reasonable (Marin, Gacon).  A lot of them sound like they belong in Middle Earth (Miaviria), to Weseteros (Josth, Mindron).  Occasionaly it'll accidentally recreate a real name. Those are my favorite.

[@MarkovBaby](http://twitter.com/markovbaby) may be suitable for an expecting couple with just the appropriate amount of eccentricity and love of statistics.

The code
--------

[Is available on my github](https://github.com/AlexeyMK/markov-baby-names).  Hopefully nothing too complicated; random.choice and collections.defaultdict proved rather helpful. I hadn't touched Markov Chains since proving things about them in Randomized Algorithms class, so it was good to know that with a bit of clever python you could write one in a few dozen lines.  For reference, mine was an 'order-1' (IE, only look at one previous character) chain.

<script src="https://gist.github.com/3119751.js"> </script>

See also, [a discussion on Markov Chain implementations in Programming Pearls](http://www.cs.bell-labs.com/cm/cs/pearls/sec153.html).

Possible extensions
-------------------

- Favorite or RT your favorite baby names, and I'll put up a leaderboard for favorite ones.
- Apply the same techniques (and same code) to startup names, using crunchbase: Markov 2.0.

If you've got a twitter bot missing in your life, [follow @markovbaby on Twitter](http://twitter.com/markovbaby).  Or [follow me](http://twitter.com/alexeymk). That would be cool too.
