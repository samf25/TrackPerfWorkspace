# Install script for directory: /isilon/export/home/sferrar2/TrackPerfWorkspace/packages/TrackPerf

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "0")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set default install directory permissions.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/usr/bin/objdump")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libTrackPerfPlugins.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libTrackPerfPlugins.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libTrackPerfPlugins.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE MODULE FILES "/isilon/export/home/sferrar2/TrackPerfWorkspace/testGaudi/packages/TrackPerf/libTrackPerfPlugins.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libTrackPerfPlugins.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libTrackPerfPlugins.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libTrackPerfPlugins.so"
         OLD_RPATH "/isilon/export/home/sferrar2/TrackPerfWorkspace/testGaudi/.plugins:/opt/spack/opt/spack/x86_64-almalinux9-gcc11.4.1-opt/edm4hep/0.10.5-mklr6c/lib64:/opt/spack/opt/spack/x86_64-almalinux9-gcc11.4.1-opt/root/6.30.06-txowyc/lib/root:/opt/spack/opt/spack/x86_64-almalinux9-gcc11.4.1-opt/dd4hep/1.29-yo6bcn/lib:/opt/spack/opt/spack/x86_64-almalinux9-gcc11.4.1-opt/k4fwcore/1.0pre19-6g5lgt/lib:/opt/spack/opt/spack/x86_64-almalinux9-gcc11.4.1-opt/xerces-c/3.2.5-wvnu3a/lib:/opt/spack/opt/spack/x86_64-almalinux9-gcc11.4.1-opt/gaudi/38.1-f5ejkb/lib:/opt/spack/opt/spack/x86_64-almalinux9-gcc11.4.1-opt/boost/1.85.0-yk62hj/lib:/opt/spack/opt/spack/x86_64-almalinux9-gcc11.4.1-opt/python/3.10.13-vrpxgy/lib:/opt/spack/opt/spack/x86_64-almalinux9-gcc11.4.1-opt/clhep/2.4.7.1-f7bkzk/lib:/opt/spack/opt/spack/x86_64-almalinux9-gcc11.4.1-opt/podio/0.99-q5wdpn/lib64:/opt/spack/opt/spack/x86_64-almalinux9-gcc11.4.1-opt/vdt/0.4.4-7tytgy/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libTrackPerfPlugins.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/python/TrackPerf" TYPE FILE FILES
    "/isilon/export/home/sferrar2/TrackPerfWorkspace/testGaudi/packages/TrackPerf/genConfDir/TrackPerf/TrackPerfPluginsConf.py"
    "/isilon/export/home/sferrar2/TrackPerfWorkspace/testGaudi/packages/TrackPerf/genConfDir/TrackPerf/__init__.py"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "shlib" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libTrackPerfPlugins.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libTrackPerfPlugins.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libTrackPerfPlugins.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE MODULE FILES "/isilon/export/home/sferrar2/TrackPerfWorkspace/testGaudi/packages/TrackPerf/libTrackPerfPlugins.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libTrackPerfPlugins.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libTrackPerfPlugins.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libTrackPerfPlugins.so"
         OLD_RPATH "/isilon/export/home/sferrar2/TrackPerfWorkspace/testGaudi/.plugins:/opt/spack/opt/spack/x86_64-almalinux9-gcc11.4.1-opt/edm4hep/0.10.5-mklr6c/lib64:/opt/spack/opt/spack/x86_64-almalinux9-gcc11.4.1-opt/root/6.30.06-txowyc/lib/root:/opt/spack/opt/spack/x86_64-almalinux9-gcc11.4.1-opt/dd4hep/1.29-yo6bcn/lib:/opt/spack/opt/spack/x86_64-almalinux9-gcc11.4.1-opt/k4fwcore/1.0pre19-6g5lgt/lib:/opt/spack/opt/spack/x86_64-almalinux9-gcc11.4.1-opt/xerces-c/3.2.5-wvnu3a/lib:/opt/spack/opt/spack/x86_64-almalinux9-gcc11.4.1-opt/gaudi/38.1-f5ejkb/lib:/opt/spack/opt/spack/x86_64-almalinux9-gcc11.4.1-opt/boost/1.85.0-yk62hj/lib:/opt/spack/opt/spack/x86_64-almalinux9-gcc11.4.1-opt/python/3.10.13-vrpxgy/lib:/opt/spack/opt/spack/x86_64-almalinux9-gcc11.4.1-opt/clhep/2.4.7.1-f7bkzk/lib:/opt/spack/opt/spack/x86_64-almalinux9-gcc11.4.1-opt/podio/0.99-q5wdpn/lib64:/opt/spack/opt/spack/x86_64-almalinux9-gcc11.4.1-opt/vdt/0.4.4-7tytgy/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libTrackPerfPlugins.so")
    endif()
  endif()
endif()

