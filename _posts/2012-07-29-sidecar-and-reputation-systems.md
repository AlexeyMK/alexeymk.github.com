---
layout: post
title: Sidecar and Digial Reputation Systems
published: true
date: 2012-07-29 23:23:57
tags:
- cool products
- review
- behavioral economics
---

For the past few months I've been using [Sidecar](side.cr) whenever I'm in SF.  The service is a sort of Uber meets [Gypsy cabs](http://en.wikipedia.org/wiki/Illegal_taxicab_operation), allowing ordering on-demand **everyday drivers**, who will give you a ride across town at a price comparable or slightly cheaper than a Taxi.

<img src="/images/Sidecar.png"></img>

A post about the service's legal standing is probably worthwhile but not for me to write.  Should you use Sidecar?  Yes, if you're looking for Uber-like service at Taxi-like prices and aren't made uncomfortable by just how sketchy the whole thing feels.  The service is invite-only for now, but if you're in SF: [here, have an invite (and 10 bucks)](http://go.side.cr/oCz).

The Reputation of ETAs
=================
I am fascinated by digital reputation systems, having focused on them in my senior thesis.

**Wait times matter**.  In the taxi world (where a few of the driver's I've met come from), operators keep track of passengers who repeatedly order cabs and then don't show up.  After a couple of no-shows, a phone number or address gets the equivalent of [Hellbanned](http://en.wikipedia.org/wiki/Hellbanning) - if they order a cab again, the operator will tell them the cab is on its way and then just not send anybody, leaving the passenger stranded.  It's a cruel sort of system, but in lieu of a real-world consumer reputation system, it's the only way I can think of for a cab company to punish poor behavior, like a waiter spitting in food.

In Sidecar's reputation system, a passenger is rated 1-5 by drivers, but only once a ride is complete.  A cancelled ride, then, is not globally stored within Sidecar's system, at least in a way visible to drivers.  The driver that was telling me this story compensates by "just remembering people" once they have skipped out on a ride or two.  In one case, he accepted a ride that claimed to be fifteen minutes away and proceeded to "walk into a deli, order a sandwich and some chips, make small-talk with the owner, and then eventually come pick the guy up."

The Solution
============
In Sidecar's case, I propose a reasonably straightforward solution: give passengers a reasonable window within which to cancel (90 seconds? 120?).  If they don't cancel, add the notification to their reputation system (late-cancelled 6% of Sidecars).  Let both parties know that this is criteria that drivers will see.  You'll get fewer cancellation and fewer drivers having to "remember people" and punish them passive-aggressively.
