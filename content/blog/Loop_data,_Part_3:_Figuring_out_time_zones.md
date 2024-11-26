---
title: "Loop data, Part 3: Figuring out time zones"
date: 2023-10-25
draft: false
---

The time zone thing is sort of a detail I could have skipped for the time being - I was already converting CGM times from "UTC" to "US/Eastern", and it would have been fine for the foreseeable future... until we decided to travel someplace that is in a different time zone, and then it would have all gone wrong. So I'm trying to get out ahead of that and just doing the time zone shift on the fly based on the time zone listed in the loop profile settings. 

It sort of feels like I'm stuck in the weeds of the data prep, but I guess that's how it always goes! It's a little more involved than when I was just grabbing stuff from Glooko - there wasn't much to look at there! This time I'm actually pulling from an actual database instead of from a bunch of csv files and there are a lot of things unpack.

<!-- Placeholder for images -->
