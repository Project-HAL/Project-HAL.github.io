.. include:: links.rst

Getting Started
===============

Folder Structure 
----------------
Each trial of an experiment has a variety of data stored along with it (h5, 
csv, etc.), and it is all saved in a specific folder system. When an experiment
is created and run, the folling folder structure is created:

| (parent_folder)
|   └>(experiment_name)
|       └>(chip_ID)
|           └>experiment_name.json
|           └>(date)
|               └>(trial_number)
|                   └>(wellN)
|                       └> experiment_name.h5
|                       └> experiment_name_well_N.cfg
|                       └> arguments.json
|                       └> other data files

experiment_name, parent_folder and chip_ID are values that are taken in the GUI and are 
stored in experiment_name.json. If an experiment with the same name and 
parent folder but a different chip ID is selected, then another subdirectory
named with the new chip ID is created under experiment_name. 

Each time an experiment runs, a new trial folder is created (and date folder 
for the first trial of the day), with a folder for each selected well to store 
associated data. There are 3 files that are guaranteed to be in each well 
folder: the h5 file that hold the recording data, the config that was used for 
the well (and passed to the closed-loop C++ program), and arguments.json, a 
copy of the original experiment json. The path of the well folder is passed to
the C++ program, so any data created in a closed-loop program can be saved 
accordingly.