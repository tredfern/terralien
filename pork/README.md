Pyglet on Rails, Kinda
======================

PoRK is a pretty strange idea I had after drinking a bunch of wine and
waking up early in the morning with a dull throb in my head. I was 
thinking of Terralien and wondering if I was overbuilding things and that
maybe there was a game engine out there I could use when I realized what
I hated about game engines. They all seem to force you to think heavily
about the engine and line things up in the way they expect.

Maybe it's for performance, but in reality performance isn't what hurts
games today it's gameplay and stability. If games could be more testable
and constructed in a fashion focusing on game logic (recognize that from
business logic?) maybe things would be easier to build and provide more
focus on what we are building instead of what we are drawing.

Of course, there needs to be a certain amount of performance and ultimately
python may be too slow for constructing a project in this fashion but I'm
willing to stupidly plow ahead and see where I end up.

I'm going to follow the principles of convention over configuration, DRY,
and also the testability of game logic by removing complexities that rendering
and user input provide.

MVC
---

The stateless web version of MVC obviously won't work in this context, at 
the same time they still provide a good foundation of where things go:

*Models* are everything from your bad and good guys, bullets, etc... to 
your levels, to your high score list. Long term goal is to provide some
persistable format. Basically, the blocks of your game.

*Controllers* do more than traditional rails controllers. These are where
the game is played. They control the interaction of models and will receive
information on user input. This is the interactions of your game. 

*Views* can be screens, images, 3D models, animations, etc... Again we are
be flexible in the definition but we are still segmenting things that are
drawn to here. This is the visualization of your game. Might include sound
for the aural view.

PorkRack
--------

The backend engine. Ok, maybe having too much fun with sharing terminology,
but here is where the engine is really running and utilizes your controllers
to provide input about what is happening on the current state of your game.
