# TODO LIST

Breaking out the goals from the change blog because things are starting to
balloon in the possibilities of items to work on and sometimes it's not
always obvious what will come next. I'll also try to break out into different
aspects more so that I can see whether I'm making progress across the board
or just focusing on tiny details of some specific area of the project. *i.e.
spending all my time on graphics instead of working on some game components*

## Visuals
 * Better management of animations and tilesets

## Map
 * Generate more terrain types
 * Transition between tiles for different terrains

## Characters
 * Characters logging thoughts, decisions to event log
 * Different character images

## User Interface
 * Select character
 * Select tile
 * Keyboard controlled cursor
 * Easier control of camera
 * Investigate pyglet-gui in more detail. Could save a lot of building
     interface elements that aren't necessary
 * Some sort of layout for the screen - areas for controls


## Pygsty

 * Update models to hold on to instances. Seems to be trouble in pyglet land when
     things are not held on to references for the vertices or something. Or it
     is just the way it is being managed. This makes a lot of sense in the long
     run anyway to provide a mechanism for tracking created objects in the engine.
     Actually maybe I'll allow you to tag objects for better searching... hmm..
