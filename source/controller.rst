.. include:: links.rst

``Controller``
==============

Overview 
^^^^^^^^

The |Controller|_ class stores |ChannelWindow|_ objects as "buttons", allowing 
for the user to automatically organize, initialize, update, and access many windows at once. 
Instead of adding a frame to each window, the |Controller|_ will add it to all
windows. 

For button-like detection from the window activity, see the subclass |NES|_.


.. image:: images/controller-diagram.png
    :width: 600

Members 
^^^^^^^

.. doxygenclass:: Controller
    :members: