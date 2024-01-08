===============
Getting Started
===============

Welcome to MusPy! We will go through some basic concepts in this tutorial.

.. Hint:: Be sure you have MusPy installed. To install MusPy, please run ``pip install muspy``.

In the following example, we will use `this JSON file <https://github.com/salu133445/muspy/blob/master/examples/example.json>`_ as an example.

First of all, let's import the MusPy library. ::

    import muspy

Now, let's load the example JSON file into a Music object. ::

    music = muspy.load("example.json")
    print(music)

Here's what we got.