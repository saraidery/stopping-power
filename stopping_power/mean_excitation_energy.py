# MIT License
#
# Copyright (c) 2022 Sarai Dery Folkestad
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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
