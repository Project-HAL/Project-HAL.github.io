..
    This file contains substitution definitions for all classes. This adds 
    literal (code) style to the name of the text and makes it a hyperlink 
    to the class page. To use in rst:

        |CLASS|_
    
    Where "CLASS" is the name of the class.

    To add more, follow the format of these substitutions.

    To use these subtitutions in a new rst file, include this file using:

        .. include:: links.rst

    Sphinx doesn't have nested inline markup (i.e. there's no easy way to style 
    references to other documents inherent to rst) and Doxygen 
    automatically creates links to classes in this format, so I added this to 
    be consistent. It also just looks nice. 

    NOTE that these links are hard-coded. If you click them on a local copy of 
    this repo, it will take you to the actual website. There's no way to imbed 
    the :doc: or :ref: directives in the substitution definitions. If the link 
    for a class, module or other changes, then these links will fail.

    Author: Trevor Sullivan
    September 2024

.. General Purpose Links

.. |mxwbio| replace:: MaxWell Biosystems
.. _mxwbio: https://www.mxwbio.com/


.. C++ Classes and Modules

.. |ElectrodeMap| replace:: ``ElectrodeMap``
.. _ElectrodeMap: https://project-hal.github.io/electrode_map.html

.. |ChannelWindow| replace:: ``ChannelWindow``
.. _ChannelWindow: https://project-hal.github.io/channel_window.html

.. |WaveDetector| replace:: ``WaveDetector``
.. _WaveDetector: https://project-hal.github.io/wave_detector.html

.. |Controller| replace:: ``Controller``
.. _Controller: https://project-hal.github.io/controller.html

.. |NES| replace:: ``NES``
.. _NES: https://project-hal.github.io/nes.html#

.. |StimVector| replace:: ``StimVector``
.. _StimVector: https://project-hal.github.io/stim_vector.html

.. |WorldState| replace:: ``WorldState``
.. _WorldState: https://project-hal.github.io/world_state.html

.. |Plotter| replace:: ``Plotter``
.. _Plotter: https://project-hal.github.io/plotter_cpp.html

.. |ProgressBar| replace:: ``ProgressBar``
.. _ProgressBar: https://project-hal.github.io/progress_bar.html

.. |argparse| replace:: ``argparse``
.. _argparse: https://project-hal.github.io/argparse.html


.. Python Classes and Modules

.. |Stimulation| replace:: ``Stimulation``
.. _Stimulation: https://project-hal.github.io/stimulation.html

