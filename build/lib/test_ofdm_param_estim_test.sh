#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/cssdr/gr-ofdm_param_estim/lib
export PATH=/home/cssdr/gr-ofdm_param_estim/build/lib:$PATH
export LD_LIBRARY_PATH=/home/cssdr/gr-ofdm_param_estim/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH
test-ofdm_param_estim 
