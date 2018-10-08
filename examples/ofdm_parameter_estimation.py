#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Ofdm Parameter Estimation
# Generated: Wed Jun  6 00:16:38 2018
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import channels
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import inspector
import numpy
import ofdm_param_estim
import sip
import sys
from gnuradio import qtgui


class ofdm_parameter_estimation(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Ofdm Parameter Estimation")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Ofdm Parameter Estimation")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "ofdm_parameter_estimation")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000
        self.fft_len = fft_len = 256
        self.cp_len = cp_len = 32
        self.SNR = SNR = 15

        ##################################################
        # Blocks
        ##################################################
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=2,
                decimation=1,
                taps=((0.8, 0.01, 0.02, 0.01, 0.01, 0.08, 0.07)),
                fractional_bw=None,
        )
        self.ofdm_param_estim_ofdm_param_estimation_c_0 = ofdm_param_estim.ofdm_param_estimation_c(samp_rate, 0, 7000, ([16, 32, 64, 128, 256, 512, 1024]), ([4, 8, 16, 32]))
        self.inspector_signal_detector_cvf_0 = inspector.signal_detector_cvf(samp_rate,  1024, firdes.WIN_BLACKMAN_hARRIS,
            -35,  0.2, False, 0.8, 0.0001, 1000, '')
        self.inspector_qtgui_sink_vf_0 = inspector.qtgui_inspector_sink_vf(samp_rate, 1024, 0, 1000, 1, True)
        self._inspector_qtgui_sink_vf_0_win = sip.wrapinstance(self.inspector_qtgui_sink_vf_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._inspector_qtgui_sink_vf_0_win)
        self.digital_ofdm_tx_0 = digital.ofdm_tx(
        	  fft_len=fft_len, cp_len=cp_len,
        	  packet_length_tag_key='length',
        	  occupied_carriers=(range(-128/2,0)+range(1,128/2),),
        	  bps_header=1,
        	  bps_payload=1,
        	  rolloff=0,
        	  debug_log=False,
        	  scramble_bits=False
        	 )
        self.channels_channel_model_0 = channels.channel_model(
        	noise_voltage=numpy.sqrt(20000*(10**(-SNR/10.0))),
        	frequency_offset=0.0,
        	epsilon=0.8,
        	taps=(numpy.random.rand(1,10)[0] + 1j*numpy.random.rand(1,10)[0]),
        	noise_seed=0,
        	block_tags=False
        )
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, 6400,True)
        self.blocks_stream_to_tagged_stream_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, 50, 'length')
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 256, 10000000)), True)



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.inspector_signal_detector_cvf_0, 'map_out'), (self.inspector_qtgui_sink_vf_0, 'map_in'))
        self.msg_connect((self.ofdm_param_estim_ofdm_param_estimation_c_0, 'ofdm_out'), (self.inspector_qtgui_sink_vf_0, 'analysis_in'))
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_stream_to_tagged_stream_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.digital_ofdm_tx_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.channels_channel_model_0, 0), (self.inspector_signal_detector_cvf_0, 0))
        self.connect((self.channels_channel_model_0, 0), (self.ofdm_param_estim_ofdm_param_estimation_c_0, 0))
        self.connect((self.digital_ofdm_tx_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.inspector_signal_detector_cvf_0, 0), (self.inspector_qtgui_sink_vf_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.channels_channel_model_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "ofdm_parameter_estimation")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.ofdm_param_estim_ofdm_param_estimation_c_0.set_samp_rate(self.samp_rate)
        self.inspector_signal_detector_cvf_0.set_samp_rate(self.samp_rate)
        self.inspector_qtgui_sink_vf_0.set_samp_rate(self.samp_rate)

    def get_fft_len(self):
        return self.fft_len

    def set_fft_len(self, fft_len):
        self.fft_len = fft_len

    def get_cp_len(self):
        return self.cp_len

    def set_cp_len(self, cp_len):
        self.cp_len = cp_len

    def get_SNR(self):
        return self.SNR

    def set_SNR(self, SNR):
        self.SNR = SNR
        self.channels_channel_model_0.set_noise_voltage(numpy.sqrt(20000*(10**(-self.SNR/10.0))))


def main(top_block_cls=ofdm_parameter_estimation, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
