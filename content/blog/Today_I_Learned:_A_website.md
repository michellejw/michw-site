---
title: "Today I Learned: A website"
date: 2024-11-18
draft: false
---

**TLDR; [Click to go straight to the TIL site!](https://waveform-til.vercel.app/)**

I'm excited to share a project I've been working on – a "Today I Learned" (TIL) website!

This project actually serves two purposes: first, it's a place where I can keep track of interesting little coding tidbits I stumble upon - those things where I'm sure future me is going to want to remember it. Second, I wanted to learn React and Next.js, and what better way to learn than by building something I'll actually use? (Spoiler alert: it's working! I'm actually using it! 🎉)

Is it more fun to build a thing than to use it? Maybe. While collecting and organizing my programming discoveries has been great, I've found that building the underlying architecture has been surprisingly fun. One of my favorite features is the command-line tool to help add new entries. Here's what it does:

- Guides you through a series of questions to set up a new TIL entry
- Automatically creates a properly formatted markdown file
- Validates the content to make sure everything is structured correctly
- Opens your default editor when it's done!

## Technical bits...

The site is built with:
- Next.js for the framework
- React for the UI components
- Markdown for content
- TypeScript for type safety
- A sprinkle of command-line magic for content management

