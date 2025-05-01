.. include:: links.rst

``WaveDetector``
================

Overview
^^^^^^^^

|WaveDetector|_ is a burst detection class designed to operate on a streaming sequence of spike frames. It identifies periods of coordinated neural activity (bursts), tracks where in space the burst began (on the chip), and estimates the time and direction of the burst propagation.

| 
This detection is **frame-by-frame**, updating internal metadata as the system evolves. Bursts are determined based on a thresholded spike count that must be exceeded for a minimum duration.

|

Conceptual Timeline
^^^^^^^^^^^^^^^^^^^

A conceptual example showing spike counts and thresholds over time:

.. code-block:: none

   Time (frames)  → 
   Spike Count    ──────────────────────────────────────────────
                    ___        ___________
                   /  ↑\      /           \
                  /   | \____/             \___
                 ↑    |                     ↑
                 |    |                     |
          burstStart   burstPeak         burstEnd
                       (maxSpikes)
|

Key Features
^^^^^^^^^^^^

- Detects bursts that exceed a **spike count threshold**
- Tracks:
  - When the burst starts
  - Where on the chip it starts (`burstStartLocation`)
  - Where the peak occurs (`maxSpikesLoc`)
  - How long the burst lasts
- Determines direction:
  - If peak is **right of start**, `burstOnLeft` is returned
  - If peak is **left of start**, `burstOnRight` is returned

|

Typical Usage
^^^^^^^^^^^^^

.. code-block:: c++

   WaveDetector sensor(WINDOW, configPath.c_str(), framesPerSec,
                       burst_size_threshold, burst_dur_threshold, 0.5);
   ChannelWindow *window = sensor.getWindow();

   for (int i = 0; i < total_frames; i++) {
       maxlab::FilteredFrameData frameData;
       auto status = maxlab::DataStreamerFiltered_receiveNextFrame(&frameData);
       if (status != maxlab::Status::MAXLAB_OK) continue;

       int waveVal = sensor.processFrame(frameData, i);

       if (waveVal == Wave::burstOnLeft || waveVal == Wave::burstOnRight) {
           WaveMetadata metadata = sensor.getMetadata();
           std::cout << "Burst started at: " << metadata.burstStartFrame
                     << ", Peak location: " << metadata.maxSpikesLoc << std::endl;
       }
   }

|

Burst Detection Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^

- `burst_size_threshold`: percentage of active electrodes that must spike
- `burst_dur_threshold`: minimum duration (in seconds) above threshold
- `BurstFinishedThreshold`: time (in seconds) system must be quiet before the burst is considered over

|

Return Values
^^^^^^^^^^^^^

From `processFrame()` / `checkBurst()`:

- `Wave::noBurst`: no burst activity detected
- `Wave::burstStart`: new burst detected
- `Wave::bursting`: mid-burst
- `Wave::burstOnLeft`: completed burst with left-to-right propagation
- `Wave::burstOnRight`: completed burst with right-to-left propagation
- `Wave::endShortBurst`: detected activity that did not meet burst duration threshold

Members 
^^^^^^^

.. doxygenclass:: WaveDetector
    :members:

.. doxygenstruct:: WaveMetadata
    :members:

.. doxygenenum:: Wave
    :project: HAL


Old Example 
^^^^^^^^^^^

Someone should change this (me). 

.. container:: toggle

    .. container:: header

        Example closed-loop program
    
    .. code-block:: c
        :linenos:

        #include <iostream>
        #include "hal.h"

        #define SYS_START_BUFFER 50000

        int main(int argc, char *argv[]) {
            maxlab::verifyStatus(maxlab::DataStreamerFiltered_open(maxlab::FilterType::IIR));

            int sampleRate = 10000;

            // ignore system startup activity
            for (int i = 0; i < SYS_START_BUFFER; i++) {
                maxlab::FilteredFrameData frameData;
                maxlab::Status status = maxlab::DataStreamerFiltered_receiveNextFrame(&frameData);

                if (status == maxlab::Status::MAXLAB_NO_FRAME) {
                    i--;
                    continue;
                }
            }

            char *configPath = "/home/mxwbio/config.cfg";

            // window length, configuration path, burst threshold, min length, hz
            WaveDetector wd = WaveDetector(200, configPath, 0.1, 1000, sampleRate);

            // examine the culture for 20 seconds
            for (int i = 0; i < 200000; i++) {
                maxlab::FilteredFrameData frameData;
                maxlab::Status status = maxlab::DataStreamerFiltered_receiveNextFrame(&frameData);

                if (status == maxlab::Status::MAXLAB_NO_FRAME) {
                    i--;
                    continue;
                }

                // extend the window and check for burst waves
                int val = wd.processFrame(frame, i + 200 + SYS_START_BUFFER);

                if (val == Wave::leftToRight) {
                    cout << "Culture bursted left to right!" << endl;
                } else if (val == Wave::rightToLeft) {
                    cout << "Culture bursted right to left!" << endl;
                }
            }

            maxlab::verifyStatus(maxlab::DataStreamerFiltered_close());
        }

See Also
^^^^^^^^

- :doc:`ChannelWindow <channelWindow>` — window of frames used to calculate spike rate
- :doc:`StimVector <stimVector>` — delivers stimulations based on burst direction


