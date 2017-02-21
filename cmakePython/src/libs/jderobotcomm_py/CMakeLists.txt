cmake_minimum_required(VERSION 2.8)

configure_module_python(jderobotComm)

add_custom_target(jderobotcomm_py ALL)
copy_to_binary_python(jderobotcomm_py jderobotComm)


### Install

install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/jderobotComm

    DESTINATION ${PYTHON_MODULE_PATH}

    COMPONENT core

)