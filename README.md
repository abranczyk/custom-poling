# The custom_poling module

This repo contains artefacts related to the custom_poling module. 

## Structure of this repo:
- `custom_poling`
  - contains the module source code
- Tutorial notebooks are in the root directory

## The module
The custom_poling module can be used to design the domain configuration of a nonlinear crystal to approximate a desired phase-matching function. 

## For users

### How to use this code

#### Installation instructions
0. Make sure you have [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [pip](https://pip.pypa.io/en/stable/installation/) (and optionally [Miniconda](https://docs.conda.io/en/latest/miniconda.html)) installed.
1. Open terminal.

    1.5 (Optional) It can be useful to create a new environment (here called `my_env`) and install Python 3.8 (recommended). Within terminal:
    ```
    conda create -n my_env python=3.8 
    ```
    then
    ```
    conda activate my_env
    ```
2. Within terminal,  clone repository:
```bash
git clone https://github.com/abranczyk/custom-poling.git
```
3. Change directory to the freshly cloned custom-poling module:
```bash
cd custom-poling
```
4. Install the package (this step gives you access to the module _outside_ of the cloned directory):
```bash
pip install -e .
```
5. You can now use the package. 

#### How to use installed the package

Now that you have the package installed, you can follow examples within the tutorial notebooks
or see the simple example below (copy the code into a file `example.py` and execute within terminal using `python example.py`):

```python
import numpy as np
import matplotlib.pyplot as plt

from custom_poling.core.target import Target
from custom_poling.core.custom_crystal import CustomCrystal

# Crystal properties
domain_width = 10.0e-6
number_domains = 1000
L = number_domains * domain_width
k0 = np.pi / domain_width

# Numerical integration parameters
k_range = 100/L
dk = k_range/401
k_array = np.arange(k0-k_range/2,k0+k_range/2,dk)

# Create a custom crystal object
custom_crystal_gauss = CustomCrystal(domain_width,number_domains)
domain_middles_gauss = custom_crystal_gauss.domain_middles

#Define and plot the target function
std = 10/L
height = 0.00025
target_pmf_gauss = lambda k:1j*height*np.exp(-(k-k0)**2/(2*std**2))*np.exp(1j * L/2 * k)
# target_pmf_gauss =lambda k:-(1j*2/(np.pi**2)) * np.sin((k-k0) * L/2)*np.exp(1j * L/2 * (k-k0))/(k-k0)
target_gauss = Target(target_pmf_gauss,k_array)
target_gauss.plot_pmf()

# Compute and plot the target amplitude
target_amplitude_gauss = target_gauss.compute_amplitude(k0,domain_middles_gauss)
target_gauss.plot_amplitude()

# Compute and plot the custom domains
custom_domains_gauss = custom_crystal_gauss.compute_domains(target_amplitude_gauss,k0)
custom_crystal_gauss.plot_domains()

# Compute and plot the PMF for the cystomized crystal

custom_crystal_gauss.compute_pmf(k_array)
custom_crystal_gauss.plot_pmf()
```

## For contributers

### Initial set-up and installing dependencies
0. Make sure you have [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [pip](https://pip.pypa.io/en/stable/installation/) (and optionally [Miniconda](https://docs.conda.io/en/latest/miniconda.html)) installed.
1. Open terminal.

    1.5 (Optional) It can be useful to create a new environment (here called `my_env`) and install Python 3.8 (recommended). Within terminal:
    ```
    conda create -n my_env python=3.8 
    ```
    then
    ```
    conda activate my_env
    ```
2. Within terminal, clone repository:
```bash
git clone https://github.com/abranczyk/custom-poling.git
```
3. Change directory to the freshly cloned custom-poling module:
```bash
cd custom-poling
```
4. Install the dependencies needed:
```
pip install -r requirements.txt
```
5. To make a contribution, first set up a remote branch (here called `my-contribution`) that is tracked:
```
git checkout master
git pull
git checkout -b my-contribution
```
... make your contribution now (edit some code, add some files) ...
```
git add .
git commit -m 'initial working version of my contribution'
git push -u origin my-contribution
```
6. Before making a Pull Request always get the latest changes from master:
```
git checkout master
git pull
git checkout my-contribution
git merge master
```
... fix any merge conflicts here ...
```
git add .
git commit -m 'merged updates from master'
git push
```
7. Go back to the `/custom-poling` repo on _GitHub_, switch to your contribution branch (same name: `my-contribution`), and click "Pull Request". Write a clear explanation of the feature.
8. Under Reviewer, select Agata Branczyk.
9. Click "Create Pull Request".
10. Your Pull Request will be reviewed and, if everything is ok, it will be merged. 

## Resources

This module is based on the theory described in the following paper:

Francesco Graffitti, Dmytro Kundys, Derryck T Reid, Agata M Brańczyk and Alessandro Fedrizzi, *Pure down-conversion photons through sub-coherence-length domain engineering*, https://iopscience.iop.org/article/10.1088/2058-9565/aa78d4

