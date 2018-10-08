#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/cssdr/gr-ofdm_param_estim/python
export PATH=/home/cssdr/gr-ofdm_param_estim/build/python:$PATH
export LD_LIBRARY_PATH=/home/cssdr/gr-ofdm_param_estim/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=/home/cssdr/gr-ofdm_param_estim/build/swig:$PYTHONPATH
/usr/bin/python2 /home/cssdr/gr-ofdm_param_estim/python/qa_ofdm_param_estimation_c.py 
