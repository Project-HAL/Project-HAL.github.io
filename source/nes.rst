``NES``
=======

Overview 
^^^^^^^^

The NES class is designed to detect button presses from 2 buttons (A and B). It 
inherits from the ``Controller`` class, allowing for manual button manipulation.

**CSV output**
""""""""""""""

The ``NES`` class will automatically create and update a csv during the 
experiment. There are 12 columns in the csv (``<button>`` means that there is a 
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