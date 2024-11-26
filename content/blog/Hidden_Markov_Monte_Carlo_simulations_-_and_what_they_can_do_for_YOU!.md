---
title: "Hidden Markov Monte Carlo simulations - and what they can do for YOU!"
date: 2023-10-22
draft: false
---

Almost every day for the past 6-ish years I've used a numerical model that falls under the category of "Hidden Markov Monte Carlo simulations". And I almost never think about what it actually means, like, big picture. And so, now, under the additional category of "dorky things nobody asked for", I will tell you all about it. I probably have no business trying to explain this but I'm gonna do it anyway buds. 

Let's split it into two parts: the Hidden Markov and the Monte Carlo. 

## Hidden Markov Model

The Hidden Markov Model sets up a problem that has a series of "states" that are hidden. The classic example problem is the weather conditions in some faraway place that you don't have access to. I guess this problem was dreamed up before the internet or cell phones or TV because clearly you could just look it up in any number of easy and accurate ways... but I digress. 

Anyway so you want to know about the weather but all you have is a telephone and a friend who lives in that place. But weirdly that friend will not tell you what the weather is. RUDE. They will only tell you what they're doing that day, and you have to use that information to figure out what the weather is. Look it's a really weird friendship. (is the friend weird for not telling you about the weather when you clearly want to know about it? or are YOU rude for fixating on the weather instead of the things your friend actually wants to share with you?)

So about those "hidden states": you don’t know what those states are, but you do know something about how the system transitions from one state to another. You also know the probability that any given state will lead to any particular observation. You can then gather up all those observations and infer what the hidden state of the system was. 

## The Monte Carlo simulation

The model I work on is actually a Monte Carlo simulation of a Markov model.  In a way it's kind of the reverse of the normal Hidden Markov setup. You use information that you have about the behaviors and transition probabilities to generate the "hidden state" (so... not actually hidden this time). You then use that state model to generate your "observations" or your fake data, essentially. 

So let's take that very realistic and not at all awkward or contrived example above, and make it EVEN WEIRDER. Let's say that you don't have the observations. You don't have any information about what your friend is doing day to day, but you do know about the general weather patterns and what your friend is likely to do given a certain type of weather. Then you can generate a bunch of "fake" consecutive weather days and predict what your friend will do, so you get a general idea of what they are doing overall day-to-day. (Although tbh if your friend doesn't want to tell you about their day, every day, maybe just give them some space and don't build a complex numerical model to predict and quantify their daily activities?? Just a thought)

## Animal movement and underwater sound exposure

The specific Hidden Markov Monte Carlo simulation that I've used (and helped develop and maintain) for 6 years predicts marine mammal and sea turtle exposure to sound from things like construction or vessel traffic. In this case the "state" basically describes how the marine animals move through a modeled sound field, and how they transition between different behaviors. At each time step, the position is updated and the "observed" sound level is logged. This is done tens of thousands of times for each simulation, and that collection of observations is used to predict the potential effects of the sound on nearby animals. 

So there you have it! 

Next time you want to simulate what someone is doing based on a probabilistic model of their local weather patterns, you will know just what to do. ENJOY!

<!-- Placeholder for images -->
