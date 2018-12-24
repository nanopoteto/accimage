This is a fork of pytorch/accimage for using ipp and libjpeg-turbo installed by anaconda.

```
conda install ipp-devel -c intel
conda install libjpeg-turbo -c conda-forge
# modify anaconda_dir in setup.py
python setup.py install --user
```

time: load 1000 grey scale images

-- 512x512 --
acc time:  2.597926616668701
cv time:  3.9754631519317627
pil time:  3.622662305831909
-- 256x256 --
acc time:  0.5734424591064453
cv time:  0.9428215026855469
pil time:  1.6239163875579834