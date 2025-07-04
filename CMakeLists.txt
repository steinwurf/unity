cmake_minimum_required(VERSION 3.12)
project(unity)

find_package(Python COMPONENTS Interpreter)

# Include common CMake settings
include("${STEINWURF_RESOLVE}/toolchains/common_settings.cmake")

# Use waf to resolve dependencies
if(NOT DEFINED STEINWURF_RESOLVE)
  message(STATUS "Resolving dependencies...")
  execute_process(
    COMMAND ${Python_EXECUTABLE} waf resolve ${STEINWURF_RESOLVE_OPTIONS}
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    RESULT_VARIABLE STATUS)

  if(STATUS AND NOT STATUS EQUAL 0)
    message(FATAL_ERROR "Failed: ${STATUS}")
  endif()

  set(STEINWURF_RESOLVE "${CMAKE_CURRENT_SOURCE_DIR}/resolve_symlinks")
endif()

add_subdirectory("${STEINWURF_RESOLVE}/unity-source" unity EXCLUDE_FROM_ALL)

add_library(steinwurf::unity ALIAS unity)

# Is top level project?
if(${CMAKE_PROJECT_NAME} STREQUAL ${PROJECT_NAME})
  enable_testing()

  # Build test executable
  file(GLOB_RECURSE unity_test_sources ./test/*.c)
  add_executable(unity_test ${unity_test_sources})
  target_link_libraries(unity_test steinwurf::unity)

  add_test(unity_test unity_test)
endif()
