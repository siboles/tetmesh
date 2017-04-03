# Created by the script cgal_create_CMakeLists
# This is the CMake script for compiling a set of CGAL applications.

project( mesh_polyhedral_domain )
cmake_minimum_required(VERSION 2.8.11)

list(APPEND CMAKE_MODULE_PATH "./findTBB.cmake")

# CGAL and its components
find_package( CGAL QUIET COMPONENTS NO_CMAKE_SYSTEM_PATH)

if ( NOT CGAL_FOUND )

  message(STATUS "This project requires the CGAL library, and will not be compiled.")
  return()  

endif()

# include helper file
include( ${CGAL_USE_FILE} )

find_package( TBB QUIET )

if( TBB_FOUND )
	message(STATUS "Found TBB - Multithreading will be enabled." ${TBB_LIBRARIES})
  include(${TBB_USE_FILE})
  list(APPEND CGAL_3RD_PARTY_LIBRARIES ${TBB_LIBRARIES})
endif()

# Boost and its components
find_package( Boost REQUIRED thread)

if ( NOT Boost_FOUND )

  message(STATUS "This project requires the Boost library, and will not be compiled.")

  return()  

endif()

list(APPEND CGAL_3RD_PARTY_LIBARIES ${Boost_LIBRARIES})
# include for local directory

# include for local package


# Creating entries for target: mesh_polyhedral_domain
# ############################
add_executable( mesh_polyhedral_domain  mesh_polyhedral_domain.cpp )

add_to_cached_list( CGAL_EXECUTABLE_TARGETS mesh_polyhedral_domain )

# Link the executable to CGAL and third-party libraries
target_link_libraries(mesh_polyhedral_domain   ${CGAL_LIBRARIES} ${CGAL_3RD_PARTY_LIBRARIES} )
