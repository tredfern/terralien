# Terralien Development

This file details the changes and experiences going through
developing this project. Frequently I lose track of what
I'm working on and where I am going. So hopefully by writing
notes I can detail what I've been learning and provide a point
to develop a more robust overview of this project in the future.

## April 2nd

It's a small improvement but a good one. I've lightly integrated the pyglet-gui
project so that I can start building an actual user interface around the project.
The implementation is difficult to manage at this point for what I need to do but
I did integrate the event log into this pyglet gui and have it update the document.
I'd like it to just append the text or show the last ten events or something, but
whatever. This is good enough for now.

![Terralien Graphics](screenshots/terralien20140402.png)


## April 1st

Plugged in pyglet-gui and have a basic document element rendering. Next step
will be to tie it to the event log and let the log fill up with events and just
append them in a scrollable log. That'll be kind of cool.

## March 31st

A simple cursor is now controllable that moves around the screen. Currently it
doesn't provide any information or ability to input anything interesting but
it is a sprite on the map that is user controlled and should allow some manipulation
of the world at this point. I'm avoiding mouse for a little bit since I think
keyboard is the long term goal for this project. But some mouse manipulate will
be available at some point.

Next I'd like to start drawing more user interface elements onto the screen.


## March 23rd

So in trying to implement more interesting AI ran into troubles of figuring out
where other objects are and what are they. I have implemented a pretty brutal
but effective for this stage repository that deals with entities in the world.
While it does not track motion of them (only really works with static objects)
it does allow for some pretty flexible searching through the ability to pass
custom filters.

Also, I've begun to break out the AI logic code. Actors will
behave with two basic levels of behavior.
 * First off they will have a task they are trying to complete. This will be
     handled by the AI component. It makes decisions about what the actor should
     be doing in order to fulfill the task, but doesn't control the rules of
     accomplishing the task
 * Orders will be created that will determine what the character is actually doing
     For example, if a task requires the character to move somewhere, it will
     give that order to the actor. The order knows how to fulfill the actual
     mechanism of moving or whatever the other task might be. When an order is
     completed the next step for a task will be called. Once all orders have
     been completed the task will be completed and the actor will find a different
     task to do.

There will probably need to be some global behaviors characters work off of in
order to give them more rounded characteristics, but this will cover the core
mechanisms for simulating the world.

## March 19th

In pygsty I created a ModelRepository to handle the dealing with models and
interactions. I'm thinking this is where queries would be run for things like:

 * Did I collide with something?
 * Where is the closest enemy?
 * Where can I find food?

This also allows for the possibility of adding hooks or a publisher/subscribe
type system from the repository when models are added/removed or if major events
happen. Right now, it's just wrapping a set which keeps the instance around and
makes it possible to track the item is there, but I will begin adding a tree
to make it easier to find models by position.

Also, looking into some object store databases. Might be overkill and really not
necessary at this point. It was kind of a side track while I poke around at what
opportunities are out there for handling that kind of work. Saving might be an
interesting thing to integrate sooner than later though because it is such a
pain.

## March 14th

Outlining some goals for the weekend:

 * Limit number of trees on a tile to one
 * Create some simple supply chain mechanics. Like chopping down a tree and taking
     it to a stockpile. Then have something like a sawmill turn it into lumber
     and put it back in the stockpile. Not sure what will happen then, but it
     is showing the main complex elements for a supply line game.

## March 10th

It's still a pretty brutal map generator, but I made it a bit more configurable
and moved some of the code out into the generators area. Forests are more consistent
and the lakes are larger. Of course, this breaks the dummy path finding game
going on right now a bit more but it's starting to look a little more interesting.

![Terralien Graphics](screenshots/terralien20140310.png)

## March 9th

Set up some build processes for Terralien and Pygsty. Probably not the most important
thing but I think those things are always better to set up early because it's easy
when there isn't much work for them to do. Considering just merging the projects
again but I think I'll avoid that. Also, came across a pyglet-gui project that looks
interesting and could really jump up the level of the user interface without needing
to build it all from scratch.

For the game, added a very brutal name generator and gave actors names. Going to
work on creating an event log that will allow the characters to log what they are
thinking about, which isn't much at this point.

## March 8th, 2014

Came across some open tilesets and tried force rendering one and it work out
really well and rendered in the appropriate location pretty easily. So I'll
be looking at utilizing this for the various elements instead of the brutal
color rendering I've currently been doing. This should actually simplify code
down considerable since I won't need to manage vertex data so much but instead
should be able to just point to images.

Ok, simple animations (not in very programmatic way) Images for terrain and
actors now. Pretty cool.

![Terralien Graphics](screenshots/terralien20140308-1.png)

## March 6th, 2014

Added some logging to pygsty to track root events, also sort of have logging working
out so that game events could be logged out but it didn't quite work. Python
default logging works a little differently than I expected so once an logger
has been created, things start mucking together more than I anticipated. At least
in a weird way. Might just not understand something, but there is definitely
a mixup going on with multiple loggers in separate modules. Will work through it.

On the cool side, making a new controller is dead simple so being able to construct
more interesting user interface elements should be a breeze with a bit more thought
on controls and elements.


## March 5th, 2014

Fixed a bad test in actors to run. Models are probably going to end up referencing each other
extensively. Maybe this isn't a bad thing now that I think about it. Actually, I
just was sleepy and being down on it. I think we are good. AI might be the weird
one out at this point since it extends model functionality. But it could be isolated
in a clean fashion in the long run.

Got some brutal trees on the map. Well, upside down triangles anyway. Fine for a start but
am starting to see some annoyances with world vs screen/render coordinates coming up
on a regular basis. I'd like to avoid a matrix for every little blip but maybe that's
the easiest way for now.

![Terralien Trees](screenshots/terralien20140305-1.png)

## March 3rd, 2014

Minor update but actors don't move through the water anymore so that's nice. Except
they get stuck now because I shortened the length of the path search so much.
Came up with an idea for them to move around it though by having them hold on
to their old searches to use when they need to search. So there will always be the
ability to use previous path information. Also read about graphs and waypoints to
help with the calculation performance and appearance. But that's probably a few
releases down the line.

### Goal for next update

  * All tests passing
  * Static elements on the map like some trees and plants
  * Some information to the screen like the total number of actors in it or something just to get the UI developing


## March 2nd, 2014

Characters now pick a destination and move towards it, when they get there they
pick a different location and move towards that. It is running around 30FPS with
100 characters moving about and finding paths. So not bad but not good enough.
Made some basic optimizations that sped things up but the downside is that it
seems sometimes the actors can get stuck in some circular loops. I'll need to
spend more time here, but for the time being the main objective is complete.

Looking into adding some different terrain types now.


## March 1st, 2014

Not much progress but hey, accomplished the goals. I have some characters
that move about randomly. Well, it's a white square, but they can move
any random direction. Not exactly where the code needs to lay for all this
stuff, but the controller lightly directs them and things are happening also

![Terralien Random](screenshots/terralien20140301-1.png)

### Goals for next update
  * Characters pick a goal to move to some random location
  * Characters move to location
  * Upon arrival they pick a different goal and move towards that


## February 28th, 2014

Here is where things ended up at the end of last night:

![Terralien Grassy](screenshots/terralien20140228-1.png)

So what is going on that is interesting? Basically this is rendering out
a tilemap as a single batch where each tile can have it's own color. Not
the most exciting thing on the planet, but it allows for scaling this up
to have different kinds of terrain, and also we can start putting characters
into this pasturic paradise.


### Goals for next update
  * Show a character on the map
  * Character should be able to move about randomly
