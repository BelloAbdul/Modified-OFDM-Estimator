INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_OFDM_PARAM_ESTIM ofdm_param_estim)

FIND_PATH(
    OFDM_PARAM_ESTIM_INCLUDE_DIRS
    NAMES ofdm_param_estim/api.h
    HINTS $ENV{OFDM_PARAM_ESTIM_DIR}/include
        ${PC_OFDM_PARAM_ESTIM_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    OFDM_PARAM_ESTIM_LIBRARIES
    NAMES gnuradio-ofdm_param_estim
    HINTS $ENV{OFDM_PARAM_ESTIM_DIR}/lib
        ${PC_OFDM_PARAM_ESTIM_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(OFDM_PARAM_ESTIM DEFAULT_MSG OFDM_PARAM_ESTIM_LIBRARIES OFDM_PARAM_ESTIM_INCLUDE_DIRS)
MARK_AS_ADVANCED(OFDM_PARAM_ESTIM_LIBRARIES OFDM_PARAM_ESTIM_INCLUDE_DIRS)

