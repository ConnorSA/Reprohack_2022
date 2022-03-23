from multiprocessing.sharedctypes import Value
from ase.io import read, write
from ase.calculators.aims import Aims
import numpy as np
import sys
import os

basis = sys.argv[1]
if basis not in ['light', 'intermediate', 'tight', 'really_tight']:
    raise ValueError('Invalid basis set.')

os.chdir(basis)
mol = read('BeC_tube+wire.xyz', format='extxyz')
mol.set_pbc([False, False, True])

print('Read in structure.')
print('Atomic positions:')
print(mol.get_positions())
print('\nUnit cell:')
print(mol.get_cell())
print('\nPBCs:')
print(mol.get_pbc())
print()
sys.stdout.flush()

calc = Aims(
    command='srun aims.x > aims.out',
    species_dir=f'/sulis/institutions/warwick/easybuild/software/FHI-aims/210716_2-foss-2021b/species_defaults/defaults_2020/{basis}',

    xc='blyp',
    k_grid=[1, 1, 500],
    occupation_type=['gaussian', 0.680],

    spin='none',
    default_initial_moment=0,

    KS_method='parallel',
    RI_method='LVL_fast',
    preconditioner=['kerker', 2.0],

    sc_accuracy_forces=1.0e-4
)

mol.calc = calc

forces = mol.get_forces()
print('Calculated forces:')
print(forces)
energy = mol.get_potential_energy()
print('\nCalculated energy:')
print(energy)

np.save('f.npy', forces)
np.save('e.npy', np.array([energy]))

