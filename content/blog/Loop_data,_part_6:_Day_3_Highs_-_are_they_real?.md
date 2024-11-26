---
title: "Loop data, part 6: Day 3 Highs - are they real?"
date: 2023-11-24
draft: false
---

I'm trying to figure out if I'm just imagining it, or if Alma's blood sugar is consistently high on the last day of her Omnipod.

For anyone who's less familiar with insulin pumps and how they work, Alma wears an Omnipod Dash pump. It's a little plastic pod that sticks to her body for three days and doses her with insulin when she needs it. It gets swapped out every three days. So every three days we refill it with fresh insulin. 

We've been noticing over the last few weeks that she has been consistently high on the third day, basically all day. I decided to dig into the data to see if I could show it as a pattern, and I ended up with this:

It sure looks like a pattern. But it's only a month of data so really only about 10 pod cycles. I started wondering if this pattern showed up while using the Omnipod 5 (O5) controller, rather than looping. After a bit of digging around I did manage to find the data to look at that (before Looping I was looking at O5 data downloaded from Glooko). Here's what it looks like for a month of O5 data:

This is interesting because it kinda looks like something's going on - is the insulin becoming less effective the longer it sits in the pod? Is this something that is corrected for in the Omnipod 5 but not in the Loop algorithm? 

I'm not sure - just speculating on this. But I also am wary about drawing too many conclusions from this comparison. I'm not looking at enough data for a start. Also there are A LOT of things that can affect blood sugar and I may be seeing something else playing out in this view. 

I have thought about some possible things I could take a closer look at. 

Plotting out a longer time period

Plot the these same views in segments somehow so that I could see if the amount of change over pod age changes over time. 

Normalize the values so we are looking at deviation from mean BG rather than absolute value. This may make comparisons easier. 

Code!

As usual, here's the Jupyter notebook that goes along with this bit of analysis.

<!-- Placeholder for images -->
