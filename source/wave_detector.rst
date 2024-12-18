.. include:: links.rst

``WaveDetector``
================

Overview 
^^^^^^^^

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

Members 
^^^^^^^

.. doxygenclass:: WaveDetector
    :members:

.. doxygenstruct:: WaveMetadata
    :members:

.. doxygenenum:: Wave
    :project: HAL

