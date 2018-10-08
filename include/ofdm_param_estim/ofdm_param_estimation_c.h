/* -*- c++ -*- */
/* 
 * Copyright 2018 gr-ofdm_param_estim author.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */


#ifndef INCLUDED_OFDM_PARAM_ESTIM_OFDM_PARAM_ESTIMATION_C_H
#define INCLUDED_OFDM_PARAM_ESTIM_OFDM_PARAM_ESTIMATION_C_H

#include <ofdm_param_estim/api.h>
#include <gnuradio/sync_block.h>

namespace gr {
  namespace ofdm_param_estim {

    /*!
     * \brief <+description of block+>
     * \ingroup ofdm_param_estim
     *
     */
    class OFDM_PARAM_ESTIM_API ofdm_param_estimation_c : virtual public gr::sync_block
    {
     public:
      typedef boost::shared_ptr<ofdm_param_estimation_c> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of ofdm_param_estim::ofdm_param_estimation_c.
       *
       * To avoid accidental use of raw pointers, ofdm_param_estim::ofdm_param_estimation_c's
       * constructor is in a private implementation
       * class. ofdm_param_estim::ofdm_param_estimation_c::make is the public interface for
       * creating new instances.
       */
      static sptr make(double samp_rate, int signal, int min_items, const std::vector<int> &typ_len, const std::vector<int> &typ_cp);
	virtual void set_samp_rate(double d_samp_rate) = 0;
    };

  } // namespace ofdm_param_estim
} // namespace gr

#endif /* INCLUDED_OFDM_PARAM_ESTIM_OFDM_PARAM_ESTIMATION_C_H */

