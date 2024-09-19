.. include:: links.rst

``NES``
=======

Overview 
^^^^^^^^

The |NES|_ class is designed to detect button presses from 2 buttons (A and B). It 
inherits from the |Controller|_ class, allowing for manual button manipulation.

An |NES|_ object compares the activity in two buttons: ``A`` and ``B``. They can 
be created with one of the constructors, or can be added manually (e.g. if the buttons 
need to have different window lengths). Many buttons can be added to an |NES|_ object; 
however, for now, it will *only* compare buttons with the names ``A`` and ``B``.

CSV output
""""""""""

An |NES|_ object will automatically create and update a csv during the 
experiment. There are 12 columns in the csv (``<button>`` indicates that there is a 
column for each button):

    - ``frame number``: frame at which the button pressed occurred
    - ``button pressed``: the button that was pressed (0 if neither was pressed, 1 if ``A`` was pressed, and 2 if ``B`` was pressed)
    - ``percent fired <button>``: the percentage of the button that fired, calculated with *(total # spikes)/(total # channels)*
    - ``firing rate <button>``: the firing rate of the button, calculated with *(total # spikes)/(frames)*
    - ``avg FR <button>``: the average firing rate over the saved windows
    - ``SD <button>``: standard deviation of the buttons firing rate 
    - ``Z score <button>``: z score of the buttons firing rate

Members 
^^^^^^^

.. doxygenclass:: NES
    :members: