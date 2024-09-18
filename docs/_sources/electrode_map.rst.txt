``ElectrodeMap``
================

Overview 
^^^^^^^^

If a configuration with less than 1024 electrodes is uploaded to the MaxOne or 
MaxTwo via the API, the system will send data from *other electrodes* that were
not chosen when reading in data with the C++ API. This class was made in order 
to combat this; it can be used to filter out activity that does not originate
from the routed configuration file.

Members 
^^^^^^^

.. doxygenclass:: ElectrodeMap
    :members: