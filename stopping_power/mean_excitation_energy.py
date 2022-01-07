import numpy as np
import os


class MeanExcitationEnergy:

    """Reads oscillator strengths and excitation energies,
    and computes all quantities needed to calculate the mean
    excitation energy:

     ln(I0) = (sum_n>0 ln(e_n) f_n) / (sum_n>0 f_n)
            = (sum_n>0 ln(e_n) f_n) / S0

            In exact theory, S0 = N_e
    """

    def __init__(self, file_name):
        self.file_name = os.path.expanduser(file_name.strip())
        self._read_excitation_energies_and_oscillator_strengths()

    def _read_excitation_energies_and_oscillator_strengths(self):
        self.e, self.f = np.loadtxt(self.file_name, skiprows=1, unpack=True)

    @property
    def S0(self):
        return np.sum(self.f)

    def _sum_ln_e_f(self):
        ln_e = np.log(self.e)
        return np.sum(np.multiply(self.f, ln_e))

    @property
    def ln_I0(self):
        return self._sum_ln_e_f() / self.S0

    @property
    def I0(self):
        return np.exp(self.ln_I0)
