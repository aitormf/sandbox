#macro to switch pythonInterp
macro(usePython ver)
  if (${ver} EQUAL 2 AND ${PYTHON2INTERP_FOUND})
    set(PYTHON_EXECUTABLE ${PYTHON2_EXECUTABLE})
    set(PYTHON_VERSION_STRING ${PYTHON2_VERSION_STRING})
    set(PYTHON_VERSION_MAJOR ${PYTHON2_VERSION_MAJOR})
    set(PYTHON_VERSION_MINOR ${PYTHON2_VERSION_MINOR})
    set(PYTHON_VERSION_PATCH ${PYTHON2_VERSION_PATCH})
    set(PYTHON_MODULE_PATH ${PYTHON2_MODULE_PATH})
    set(PYTHONINTERP_FOUND TRUE)
  elseif(${ver} EQUAL 3 AND ${PYTHON3INTERP_FOUND})
    set(PYTHON_EXECUTABLE ${PYTHON3_EXECUTABLE})
    set(PYTHON_VERSION_STRING ${PYTHON3_VERSION_STRING})
    set(PYTHON_VERSION_MAJOR ${PYTHON3_VERSION_MAJOR})
    set(PYTHON_VERSION_MINOR ${PYTHON3_VERSION_MINOR})
    set(PYTHON_VERSION_PATCH ${PYTHON3_VERSION_PATCH})
    set(PYTHON_MODULE_PATH ${PYTHON3_MODULE_PATH})
    set(PYTHONINTERP_FOUND TRUE)
  else(${ver} EQUAL 2 AND ${PYTHON2INTERP_FOUND})
    unset(PYTHON_EXECUTABLE)
    unset(PYTHON_VERSION_STRING)
    unset(PYTHON_VERSION_MAJOR)
    unset(PYTHON_VERSION_MINOR)
    unset(PYTHON_VERSION_PATCH)
    unset(PYTHON_MODULE_PATH)
    set(PYTHONINTERP_FOUND FALSE)
  endif(${ver} EQUAL 2 AND ${PYTHON2INTERP_FOUND})
endmacro()



#macro to switch pythonInterp
macro(configure_file_python input output)

  usePython(2)
  configure_file( ${input} py2/${output} @ONLY)

  usePython(3)
  configure_file( ${input} py3/${output} @ONLY)
  
endmacro()


#macro to switch pythonInterp
macro(configure_module_python module)
  file(GLOB_RECURSE files RELATIVE ${CMAKE_CURRENT_SOURCE_DIR}/${ModuleName}/ *.in)

  foreach(file ${files})
    string(REGEX REPLACE "\\.in$" "" f "${file}")

    configure_file_python(${file} ${f})

  endforeach(file ${files})
  
endmacro()


# MACRO to get the list of subdirectories
macro(copy_to_binary_python target ModuleName)

  if (NOT EXISTS ${CMAKE_CURRENT_BINARY_DIR}/py2/${ModuleName})
    file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/py2/${ModuleName})
  endif()
  if (NOT EXISTS ${CMAKE_CURRENT_BINARY_DIR}/py3/${ModuleName})
    file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/py3/${ModuleName})
  endif()


  file(GLOB_RECURSE files LIST_DIRECTORIES true RELATIVE ${CMAKE_CURRENT_SOURCE_DIR}/${ModuleName} ${ModuleName}/*)



  string(REGEX REPLACE "[^;]+\\.in;?" "" files "${files}")

  foreach(file ${files})
    if(IS_DIRECTORY ${file})
        file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/py2/${file})
        file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/py3/${file})
    else(IS_DIRECTORY ${file})
        add_custom_command(TARGET ${target} 
            COMMAND ${CMAKE_COMMAND} -E copy
            ${CMAKE_CURRENT_SOURCE_DIR}/${ModuleName}/${file} ${CMAKE_CURRENT_BINARY_DIR}/py2/${ModuleName}/${file}
        )
        add_custom_command(TARGET ${target} 
            COMMAND ${CMAKE_COMMAND} -E copy
            ${CMAKE_CURRENT_SOURCE_DIR}/${ModuleName}/${file} ${CMAKE_CURRENT_BINARY_DIR}/py3/${ModuleName}/${file}
        )
    endif(IS_DIRECTORY ${file})
  endforeach(file ${files})
endmacro()


macro (install_python module component)
  install(DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/py2/jderobotComm

    DESTINATION ${PYTHON2_MODULE_PATH}

    COMPONENT core

  )

  install(DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/py3/jderobotComm

    DESTINATION ${PYTHON3_MODULE_PATH}

    COMPONENT core

  )


endmacro()