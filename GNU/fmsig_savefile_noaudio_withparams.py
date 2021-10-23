#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Direction Finding - Read FM signal to file
# Author: Keagan Chasenski
# GNU Radio version: 3.8.2.0

from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import limesdr


class fmsig_savefile_noaudio(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Direction Finding - Read FM signal to file")

        ##################################################
        # Blocks
        ##################################################
        self.limesdr_source_0 = limesdr.source('000907060246091F', 2, '')


        self.limesdr_source_0.set_sample_rate(2e6)


        self.limesdr_source_0.set_center_freq(89e6, 0)

        self.limesdr_source_0.set_bandwidth(2e6, 0)

        self.limesdr_source_0.set_bandwidth(2e6, 1)

        self.limesdr_source_0.set_digital_filter(2e6, 0)

        self.limesdr_source_0.set_digital_filter(2e6, 1)

        self.limesdr_source_0.set_gain(45, 0)

        self.limesdr_source_0.set_gain(45, 1)

        self.limesdr_source_0.set_antenna(2, 0)

        self.limesdr_source_0.set_antenna(2, 1)

        self.limesdr_source_0.calibrate(2.5e6, 0)

        self.limesdr_source_0.calibrate(2.5e6, 1)
        self.blocks_stream_to_vector_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, 2)
        self.blocks_stream_to_vector_0_0.set_block_alias("vector_stream_antenna1")
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, 2)
        self.blocks_stream_to_vector_0.set_block_alias("vector_stream_antenna2")
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_gr_complex*2, '/home/keagan/Desktop/Testing/a1_data.iq', False)
        self.blocks_file_sink_0_0.set_unbuffered(False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*2, '/home/keagan/Desktop/Testing/a2_data.iq', False)
        self.blocks_file_sink_0.set_unbuffered(False)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_stream_to_vector_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_stream_to_vector_0_0, 0), (self.blocks_file_sink_0_0, 0))
        self.connect((self.limesdr_source_0, 1), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.limesdr_source_0, 0), (self.blocks_stream_to_vector_0_0, 0))






def main(top_block_cls=fmsig_savefile_noaudio, options=None):
    tb = top_block_cls()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    tb.start()

    try:
        input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
