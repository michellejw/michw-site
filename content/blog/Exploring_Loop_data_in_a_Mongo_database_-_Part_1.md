---
title: "Exploring Loop data in a Mongo database - Part 1"
date: 2023-10-18
draft: false
---

Now that we have Alma up and running with a DIY Loop system, all of her data live on a MongoDB database. Everything is in there - blood sugar (readings every 5 minutes!) and pump data (boluses, corrections, carb ratios, insulin sensitivities, basal settings, etc). This data could really help to figure out her settings - which would be AMAZING - but it's going to take some time to figure out how to access it all. 

But there are definitely patterns there, and I want to be able to see them!

So the chunk of code below is a Jupyter Notebook stored as a Gist on Github. Feel free to explore the repository in more detail. You can also check out this specific notebook on Github if you like!

In this notebook, I'm using a pretty simple custom python module (mdb_tools - you can find it in my repo) to access the database, load some collections, and then convert (some parts of) those collections to pandas dataframes to help me with analysis.

<!-- Placeholder for images -->
