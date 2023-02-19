.. makkulupy documentation master file, created by
   sphinx-quickstart on Sun Feb 19 10:48:22 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

makkulupy
=====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

**makkulupy** is a lightweight tool for accessing the makkulu dictionary API and returning its data in a Pythonic way.

Getting started
-------------------------------------

::

   import makkulupy

   words = makkulupy.get_words(headword="makkulu")

   for word in words:
      print(f"{word.headword} means {word.definition}")

Reference
-------------------------------------
.. automodule:: makkulupy
   :members:
