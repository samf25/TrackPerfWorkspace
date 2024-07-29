######################################################
# cmake file for building Gaudi Packages
# @author Samuel Ferraro
CMAKE_MINIMUM_REQUIRED(VERSION 3.15 FATAL_ERROR)
######################################################

PROJECT(TrackPerfWorkspace VERSION 2.0.0)

### DEPENDENCIES #####################################
FIND_PACKAGE( Gaudi REQUIRED )
FIND_PACKAGE( EDM4HEP REQUIRED )
FIND_PACKAGE( DD4hep REQUIRED COMPONENTS DDCore )
FIND_PACKAGE( ROOT REQUIRED )
FIND_PACKAGE( Acts REQUIRED COMPONENTS Core PluginJson PluginTGeo )
FIND_PACKAGE( k4FWCore REQUIRED )
INCLUDE(GNUInstallDirs)

### DOCUMENTATION ###################################
OPTION( INSTALL_DOC "Set to OFF to skip build/install Documentation" OFF )

IF( INSTALL_DOC AND EXISTS "${PROJECT_SOURCE_DIR}/doc/CMakeLists.txt" )
    ADD_SUBDIRECTORY( ./doc )
ENDIF()

#
# Find and add all packages
FILE(GLOB packages RELATIVE ${CMAKE_CURRENT_LIST_DIR} packages/*)
FOREACH(package ${packages})
  IF(IS_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/${package})
    MESSAGE("Add package ${package}")
    ADD_SUBDIRECTORY(${package})
  ENDIF()
ENDFOREACH()

install(EXPORT ${PROJECT_NAME}Targets
	NAMESPACE ${PROJECT_NAME}::
	FILE "${PROJECT_NAME}Tragets.cmake"
	DESTINATION "${CMAKE_INSTALL_LIBDIR}/cmake/${PROJECT_NAME}/"
)

gaudi_install(CMAKE cmake/${PROJECT_NAME}Config.cmake)
