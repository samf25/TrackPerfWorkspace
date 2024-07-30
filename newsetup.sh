# mkdir build
# cd build
# cmake .. -DCMAKE_INSTALL_PREFIX=../install
# cmake --build . -j $(nproc) -t install 
# cd ../install

export PATH=$PWD/install/bin:$PATH
export LD_LIBRARY_PATH=$PWD/install/lib:$PWD/install/lib64:$LD_LIBRARY_PATH
export ROOT_INCLUDE_PATH=$PWD/install/include:$ROOT_INCLUDE_PATH
export PYTHONPATH=$PWD/install/python:$PYTHONPATH
export CMAKE_PREFIX_PATH=$PWD/install:$CMAKE_PREFIX_PATH

export LD_LIBRARY_PATH=/opt/spack/opt/spack/x86_64-almalinux9-gcc11.4.1-opt/acts/32.1.0-bptf4c/lib64/:$LD_LIBRARY_PATH
