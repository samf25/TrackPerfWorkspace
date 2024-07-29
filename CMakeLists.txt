CMAKE_MINIMUM_REQUIRED(VERSION 3.15 FATAL_ERROR)

PROJECT(TrackPerfWorkspace)

#
# Find and add all packages
FILE(GLOB packages RELATIVE ${CMAKE_CURRENT_LIST_DIR} packages/*)
FOREACH(package ${packages})
  IF(IS_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/${package})
    MESSAGE("Add package ${package}")
    ADD_SUBDIRECTORY(${package})
  ENDIF()
ENDFOREACH()

# Data
# ADD_SUBDIRECTORY(data)

#--- The genConf directory has been renamed to genConfDir in Gaudi 35r1
#--- See https://gitlab.cern.ch/gaudi/Gaudi/-/merge_requests/1158
set(GAUDI_GENCONF_DIR "genConfDir")
#if (${Gaudi_VERSION} VERSION_LESS 35.1)
#  set(GAUDI_GENCONF_DIR "genConf")
#endif()

gaudi_install(CMAKE cmake/${PROJECT_NAME}Config.cmake)
