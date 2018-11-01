This is a fork of pytorch/accimage for using ipp and libjpeg-turbo installed by anaconda.

```
conda install ipp-devel -c intel
conda install libjpeg-turbo -c conda-forge
# modify anaconda_dir in setup.py
python setup.py install --user
```
