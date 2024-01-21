import numpy as np
import os
import pytest

from custom_poling.core.custom_crystal import Crystal

def test_crystal_attributes() -> None:
    domain_width = 1
    number_domains = 10
    z0 = 0
    crystal = Crystal(domain_width, number_domains, z0)
    assert crystal.domain_width == domain_width
    assert crystal.number_domains == number_domains
    assert crystal.z0 == z0
    assert crystal.length == domain_width * number_domains
    assert np.array_equal(crystal.domain_walls, np.arange(z0, z0 + (number_domains + 1) * domain_width, domain_width))
    assert np.array_equal(crystal.domain_middles, (crystal.domain_walls + domain_width/2)[0:-1])
  
def test_crystal_compute_pmf_array_length() -> None:
    domain_width = 1
    number_domains = 10
    z0 = 0
    crystal = Crystal(domain_width, number_domains, z0)
    domain_configuration = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]
    k_array = np.linspace(-1, 1, 100)
    crystal_pmf = crystal.compute_pmf(domain_configuration, k_array)
    assert len(crystal_pmf) == len(k_array)

def test_crystal_compute_pmf_array_values() -> None:
    domain_width = 1
    number_domains = 10
    z0 = 0
    crystal = Crystal(domain_width, number_domains, z0)
    domain_configuration = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]
    k_array = np.linspace(-1, 1, 6)
    crystal_pmf = crystal.compute_pmf(domain_configuration, k_array)
    expected_crystal_pmf=np.array([1.00468936-0.29720009j, 0.02053462-0.14405557j,
       0.71044314+0.4561703j , 0.71044314-0.4561703j ,
       0.02053462+0.14405557j, 1.00468936+0.29720009j])
    assert np.allclose(crystal_pmf,expected_crystal_pmf,rtol=1e-07)
    
def test_crystal_compute_pmf_invalid_karray() -> None:
    with pytest.raises(ValueError):
        domain_width = 1
        number_domains = 10
        z0 = 0
        crystal = Crystal(domain_width, number_domains, z0)
        domain_configuration = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]
        k_array = np.linspace(-1, 1, 5)
        crystal.compute_pmf(domain_configuration, k_array)

def test_crystal_plot_domains_and_save() -> None:
    domain_width = 1
    number_domains = 10
    z0 = 0
    crystal = Crystal(domain_width, number_domains, z0)
    domain_configuration = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]
    crystal.plot_domains(domain_configuration, n_max=5, show=False, save_as='test_crystal.png', fix_ticks=True)
    assert os.path.isfile('test_crystal.png')
    os.remove('test_crystal.png')

# def test_crystal_plot_domains_and_show() -> None:
#     domain_width = 1
#     number_domains = 10
#     z0 = 0
#     crystal = Crystal(domain_width, number_domains, z0)
#     domain_configuration = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]
#     crystal.plot_domains(domain_configuration, n_max=5, show=True, save_as='test_crystal.png', fix_ticks=True)
#     # TBD
