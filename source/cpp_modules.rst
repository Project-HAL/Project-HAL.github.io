.. include:: links.rst

C++ Modules 
===========

The HAL C++ modules come in two varieties:

    - **Experiment Logic**: these modules are used at the core of the data processing for the closed-loop experiments

        - :doc:`electrode_map`
        - :doc:`channel_window`
        - :doc:`wave_detector`
        - :doc:`controller`
        - |NES|
        - :doc:`world_state`
    - **General Purpose**: these modules were made to either simplify code or add useful visualizations

        - :doc:`plotter_cpp`
        - :doc:`progress_bar`
        - :doc:`argparse`

|NES|_



Here is an |emphasized hyperlink|_.

.. |emphasized hyperlink| replace:: *emphasized hyperlink*
.. _emphasized hyperlink: https://project-hybrot.github.io/nes.html#_CPPv43NES

Module Index:
^^^^^^^^^^^^^

.. toctree::   
    electrode_map
    channel_window
    wave_detector
    controller
    nes
    world_state
    plotter_cpp
    progress_bar
    argparse