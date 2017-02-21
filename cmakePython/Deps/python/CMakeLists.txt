find_package(Python3Interp)
find_package(Python2Interp)

usePython(3)

execute_process(
  COMMAND ${PYTHON_EXECUTABLE} -c "import os;print(os.path.dirname(os.__file__))"
  RESULT_VARIABLE _RESULT
  OUTPUT_VARIABLE PYTHON3_MODULE_PATH
  OUTPUT_STRIP_TRAILING_WHITESPACE
)

if(_RESULT)
  message(FATAL_ERROR "Failed to determine python information")
endif(_RESULT)
unset(_RESULT)

message(${PYTHON3_MODULE_PATH})


usePython(2)

execute_process(
  COMMAND ${PYTHON_EXECUTABLE} -c "import os;print(os.path.dirname(os.__file__))"
  RESULT_VARIABLE _RESULT
  OUTPUT_VARIABLE PYTHON2_MODULE_PATH
  OUTPUT_STRIP_TRAILING_WHITESPACE
)

if(_RESULT)
  message(FATAL_ERROR "Failed to determine python information")
endif(_RESULT)
unset(_RESULT)

message(${PYTHON2_MODULE_PATH})
