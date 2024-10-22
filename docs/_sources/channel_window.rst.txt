.. include:: links.rst

``ChannelWindow``
=================

Overview 
^^^^^^^^

|ChannelWindow|_ stores frames as a sequence so they can be processed at the 
same time. A |ChannelWindow|_ of length ``N`` is initialized with the first 
``N`` frames of the experiment.

.. image:: images/window.png
    :align: center

| 
Chip activity data can be extracted from the window, such as the firing rate 
and the average x-position of the spikes. For each new frame added to the 
window, the oldest frame is removed.

.. image:: images/window-change.png
    :align: center

| 
If specified, the |ChannelWindow|_ will save the data for ``P`` number of *past 
windows*. Data is saved for each *unique* window, which means that none of the 
frames in the current window are in the most recent past window. 

For example, 
if the window is 200 frames long, then frames 0 through 199 are saved as the 
first past window. The next window that will be saved will contain frames 200 
through 299, since that is the first set of frames where there is no overlap 
with the most recently saved window.

Similar to how |ChannelWindow|_ deals with frames, when there are ``P`` past
windows and a new window is saved, the oldest window will be removed.

Currently, the only window data that is saved is the firing rate, but can 
easily be extended.


.. image:: images/past-windows.png


Members 
^^^^^^^

.. doxygenclass:: ChannelWindow
    :members: