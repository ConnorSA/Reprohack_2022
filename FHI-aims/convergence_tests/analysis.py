import numpy as np
import matplotlib.pyplot as plt

blist = ['light', 'intermediate', 'tight', 'really_tight']

forces = {}
energies = np.zeros(len(blist))
for i, basis in enumerate(blist):
    forces.update({basis: np.load(f'{basis}/f.npy')})
    energies[i] = np.load(f'{basis}/e.npy')[0]

plt.plot(blist, energies)
plt.ylabel('Energy / eV')
plt.savefig('e_conv.png', dpi=100)
plt.clf()

frms = np.zeros((len(blist), len(forces['light'])))
for i, basis in enumerate(blist):
    for j, f in enumerate(forces[basis]):
        frms[i, j] = np.sqrt(np.mean(f**2))

for j in range(np.shape(frms)[1]):
    plt.plot(blist, frms[:, j], label=f'A{j+1}')

plt.ylabel('RMS Force on Atom / eV/Ang')
plt.legend()
plt.savefig('f_conv.png', dpi=100)

print('Frms (really_tight) - Frms (tight):')
for j in range(np.shape(frms)[1]):
    print(f'A{j+1}: {frms[-1, j] - frms[-2, j]}')