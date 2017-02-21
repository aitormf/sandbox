project (jderobot)

cmake_minimum_required(VERSION 2.8)


# include Modules 
list(APPEND CMAKE_MODULE_PATH "${PROJECT_SOURCE_DIR}/cmake/modules")

include(${PROJECT_SOURCE_DIR}/cmake/modules/pythonAux.cmake)

#check compiller
if("${CMAKE_CXX_COMPILER_ID}" STREQUAL "GNU")
	include(CheckCXXCompilerFlag)
	CHECK_CXX_COMPILER_FLAG("-std=c++11" COMPILER_SUPPORTS_CXX11)
	CHECK_CXX_COMPILER_FLAG("-std=c++0x" COMPILER_SUPPORTS_CXX0X)
	message (version: ${CMAKE_CXX_COMPILER_VERSION})
	if(COMPILER_SUPPORTS_CXX11)
    	set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
	elseif(COMPILER_SUPPORTS_CXX0X)
        #boost have problems with gcc < 4.7 and c++0x
        if(CMAKE_CXX_COMPILER_VERSION VERSION_GREATER "4.7.0")
    		set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++0x")
        endif()
	else()
		    message(STATUS "The compiler ${CMAKE_CXX_COMPILER} has no C++11 support.")
	endif()

endif()

# ENV VARS
SET(gladedir ./)
SET( DEPS_DIR ${CMAKE_CURRENT_SOURCE_DIR}/Deps) # Directory where the dependencies are there
# Folder with ICE cpp interfaces
SET( INTERFACES_CPP_DIR ${CMAKE_CURRENT_BINARY_DIR}/src/interfaces/cpp/jderobot ${CMAKE_CURRENT_BINARY_DIR}/src/interfaces/cpp/)
# Folder with ICE python interfaces
SET( INTERFACES_PYTHON_DIR ${CMAKE_CURRENT_BINARY_DIR}/src/interfaces/python/jderobot ${CMAKE_CURRENT_BINARY_DIR}/src/interfaces/python/)
# Folder with ICE java interfaces
SET( INTERFACES_JAVA_DIR ${CMAKE_CURRENT_BINARY_DIR}/src/interfaces/java/jderobot ${CMAKE_CURRENT_BINARY_DIR}/src/interfaces/java/)
# Folder JdeRobot libraries 
SET( LIBS_DIR ${CMAKE_CURRENT_SOURCE_DIR}/src/libs) 
# Folder ICE interface definitions
SET( SLICE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/src/interfaces/slice)
# Main libraries
SET( LIBS_NEEDED  jderobotutil colorspaces colorspacesmm easyiceconfig parallelIce depthLib geometry logger ns progeo pioneer fuzzylib  )
SET( LIBS_EXTRA     jderobotHandlers jderobotViewer   resourcelocator xmlParser cvblob cvfast imgAnalyze JderobotInterfaces)

# Create directories if necessary
file(MAKE_DIRECTORY ${INTERFACES_PYTHON_DIR})
file(MAKE_DIRECTORY ${INTERFACES_JAVA_DIR})
file(MAKE_DIRECTORY ${INTERFACES_CPP_DIR})

# MACRO to get the list of subdirectories
macro(list_subdirectories retval curdir return_relative)
  file(GLOB sub-dir RELATIVE ${curdir} *)
  set(list_of_dirs "")
  foreach(dir ${sub-dir})
    if(IS_DIRECTORY ${curdir}/${dir})
      if (${return_relative})
        if (NOT ${dir} MATCHES "CMakeFiles" AND NOT ${dir} MATCHES ".svn")
                set(list_of_dirs ${list_of_dirs} ${dir})
        endif()
      else()
        set(list_of_dirs ${list_of_dirs} ${curdir}/${dir})
      endif()
    endif()
  endforeach()
  set(${retval} ${list_of_dirs})
endmacro()



###################
#                 #
#  CHECK SYSTEM   #
#                 #
###################

  # FIND & CHECK PRINCIPAL LIBRARIES

include(FindPkgConfig)

PKG_CHECK_MODULES(gsl REQUIRED gsl)
include_directories(${gsl_INCLUDE_DIRS})
link_directories(${gsl_LIBRARIES_DIRS})

PKG_CHECK_MODULES(eigen REQUIRED eigen3)
include_directories(${eigen_INCLUDE_DIRS})

  # FIND AND CHECK OTHER DEPENDENCES

include(Deps/LoadJderobotDependencies.cmake)

list(APPEND DEPS libgsl2 gsl-bin)
list(APPEND DEPS_DEV git cmake make gcc-5 g++-5 gcc g++ pkg-config libeigen3-dev libgsl-dev libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev)
list(APPEND DEPS_DEV "${DEPS}")

# list(APPEND uses ; separator. We need ,
STRING(REGEX REPLACE ";" ", " DEPS "${DEPS}")
STRING(REGEX REPLACE ";" ", " DEPS_DEV "${DEPS_DEV}")



# START RECURSIVE
add_subdirectory (${CMAKE_CURRENT_SOURCE_DIR}/src)