---
title: "Adventures in APIs: A tiny lil' weather app"
date: 2024-01-30
draft: false
---

This is my second app (huzzah!) – and I made it purely for learning purposes. I needed to figure out how to access online data, and weather data is a decent place to start since it’s familiar and there are a lot of well-documented options to choose from. The image above shows the main weather screen and also the secondary "city screen". 

For the insulin dosing app, I have a few different ideas for things to implement, but one of the big ones is to allow users to look up common foods directly inside the app. This was a concept that has been sort of scary to me for a while, mainly because I didn't really have a clue how to do it. Turns out it's not as hard as I thought it would be!&nbsp;

APIs

APIs (Application Programming Interfaces) basically give you a set of rules, or instructions, on how you can talk to other software (or applications). In this weather app example, I'm basically asking a website to pass back some data. It might seem a bit mysterious but all that's really happening is that I'm building a URL (a web address) that requests something and if I do it right, I get some data back.&nbsp;

Look, I'll even prove how simple it is. This is an example API call to the National Weather Service API:

https://api.weather.gov/gridpoints/TOP/31,80/forecast

Go ahead - you can click on it! It just takes you to a (extremely boring) web page that shows the data at that location (31 and 80 are the latitude and longitude in degrees).&nbsp;

A lot of times you'll also have to use a special password, called an "API key" - this is generally so that the owners of the database can either limit the number of calls you can do in say an hour or a day, or else so that they can charge you for the number of calls.

Here's a little screen shot showing the dart file where the weather app accesses the NWS API. It's really just a generic class that has a method for pulling data from any URL and some error checks in case it doesn't work. Dying to see more? I got you, just check out the repo, especially the&nbsp; "lib" folder: https://github.com/michellejw/weather_app.

Things I learned

API's are not scary! (well not as scary as I thought anyway)

While the API calls themselves are ok, the code that wraps around them is often what's called "asynchronous" and that whole deal is a bit of a brain breaker. Again though - not impossible and I think it'll get better with practice.&nbsp;

Next Steps (Insulin dosing app)

Choose a nutrition database to pull from. Preferably one that is open source or at least has a decent free tier.&nbsp;

Re-arrange the insulin dosing app interface to allow users to search for, and select, common foods (or to simply enter nutrition information directly).

Now that I'm wrapping up this mini foray into API's, I'm feeling ready to jump back into the main app, and tackle some of my next steps - both API-related and otherwise. Stay tuned for more updates (if that's your jam) and as always I'm happy to hear from you, especially if you've had similar experiences!&nbsp;

<!-- Placeholder for images -->
