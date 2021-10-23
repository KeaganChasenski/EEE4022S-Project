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
import time


class fmsig_savefile_noaudio(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Direction Finding - Read FM signal to file")

        ##################################################
        # Blocks
        ##################################################
        self.limesdr_source_0 = limesdr.source('000907060246091F', 2, '/home/pi/Desktop/Thesis/Testing/limesdr_init')
        self.blocks_stream_to_vector_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, 2)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, 2)
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_gr_complex*2, '/home/pi/Desktop/Thesis/Testing/a1_data.iq', False)
        self.blocks_file_sink_0_0.set_unbuffered(False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*2, '/home/pi/Desktop/Thesis/Testing/a2_data.iq', False)
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
    
    tb.start()
    
    time.sleep(0.1)    
        
    tb.stop()
    tb.wait()
    #sys.exit(0)


if __name__ == '__main__':
    main()
