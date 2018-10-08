/* -*- c++ -*- */

#define OFDM_PARAM_ESTIM_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "ofdm_param_estim_swig_doc.i"

%include "std_map.i"

namespace std {
  %template(map_float_vector) map<float, vector<float> >;
};

%{
#include "ofdm_param_estim/ofdm_param_estimation_c.h"
%}


%include "ofdm_param_estim/ofdm_param_estimation_c.h"
GR_SWIG_BLOCK_MAGIC2(ofdm_param_estim, ofdm_param_estimation_c);
