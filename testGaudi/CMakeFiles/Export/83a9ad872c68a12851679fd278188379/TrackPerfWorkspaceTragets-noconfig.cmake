#----------------------------------------------------------------
# Generated CMake target import file.
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "TrackPerfWorkspace::ACTSTrackingPlugins" for configuration ""
set_property(TARGET TrackPerfWorkspace::ACTSTrackingPlugins APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(TrackPerfWorkspace::ACTSTrackingPlugins PROPERTIES
  IMPORTED_COMMON_LANGUAGE_RUNTIME_NOCONFIG ""
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/libACTSTrackingPlugins.so"
  IMPORTED_NO_SONAME_NOCONFIG "TRUE"
  )

list(APPEND _cmake_import_check_targets TrackPerfWorkspace::ACTSTrackingPlugins )
list(APPEND _cmake_import_check_files_for_TrackPerfWorkspace::ACTSTrackingPlugins "${_IMPORT_PREFIX}/lib/libACTSTrackingPlugins.so" )

# Import target "TrackPerfWorkspace::TrackPerfPlugins" for configuration ""
set_property(TARGET TrackPerfWorkspace::TrackPerfPlugins APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(TrackPerfWorkspace::TrackPerfPlugins PROPERTIES
  IMPORTED_COMMON_LANGUAGE_RUNTIME_NOCONFIG ""
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/libTrackPerfPlugins.so"
  IMPORTED_NO_SONAME_NOCONFIG "TRUE"
  )

list(APPEND _cmake_import_check_targets TrackPerfWorkspace::TrackPerfPlugins )
list(APPEND _cmake_import_check_files_for_TrackPerfWorkspace::TrackPerfPlugins "${_IMPORT_PREFIX}/lib/libTrackPerfPlugins.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
