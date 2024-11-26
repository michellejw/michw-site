---
title: "Extract loop settings at specific times - part 2"
date: 2023-10-25
draft: false
---

I should probably explain what I'm even trying to do here. I mean, my main goal is, of course, to improve the way I'm treating my daughter's type 1 diabetes. But the question is - how?

One of the amazing benefits of the loop system is that you have control over so many variables. With Omnipod 5 (which is also great!), there's quite a lot less you can tweak - you can set a few things but it's a bit of a black box. Lots of people prefer it that way, no judgement here! On the flip side, while it's more difficult to get things set up with loop, you can do pretty much any tweak you want. Which is amazing! But does involve a lot more effort in the beginning. 

What I'm hoping to do, to start out at least, is to split the data out into dependent and independent variables, here's how I picture it:

Independent variables

carb ratio

insulin sensitivity

basal rate (or basal + temp basal)

time/date

Dependent variables

blood glucose level 

time in range (per time unit)

max slope

variability (CV or st.dev?)

peak after eating

lowest after bolus

What it boils down to is: how can I adjust the treatments (independent variables) to best keep her numbers (dependent variables) in check, whatever that may look like to us. And then I can start looking at potential models that might explain those relationships. 

In the notebook, below, I create a function to extract the various loop settings for a series (or array or list) of requested times. I look at it, now that it's done, and I'm sure that there are far better ways to solve this problem, nicer ways to write this code, but ya gotta start somewhere! I initially only wrote it to extract carb ratios but then realized that the insulin sensitivity and basal rate (and a couple of other things) are stored in the exact same way. So I made the function accept different requested settings. 

Next steps

I think this is decent progress but absolute next thing on my list is to figure out time zones. Times are mostly logged in GMT but many treatment settings are set based on the time of day, which is - of course - local to the person being treated. In our case it's GMT-4, or Eastern time. 

PS: I'll be honest, I'm a little self-conscious about how over-commented my code is, but I've found that it helps me to have pretty much an entire novel to explain my own code back to me because I'll forget what I'm doing. Is all of this a larger reflection on the quality of my code? Perhaps. Let's not worry about that too much though, shall we?

<!-- Placeholder for images -->
