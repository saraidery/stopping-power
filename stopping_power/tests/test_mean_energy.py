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

import pytest
import os

import numpy as np


from stopping_power import eTLanczosReader
from stopping_power import MeanExcitationEnergy


class TesteTReader:
    def test_mean_excitation_energy(self):

        reference = np.array([42.280374221168536, 3.7443230119838824, 2.0038666367310003])

        file_path = os.path.dirname(__file__)
        file_name = os.path.join(file_path, "He_20")
        eT_reader = eTLanczosReader(file_name)

        file_name_out = os.path.join(file_path, "output")
        eT_reader.generate_file(file_name_out)

        mean = MeanExcitationEnergy(file_name_out)

        computed = np.array([mean.I0, mean.ln_I0, mean.S0])
        assert np.allclose(reference, computed)

        os.remove(file_name_out)

    def test_mean_excitation_energy_symmetry(self):

        reference = np.array([42.280374221168536, 3.7443230119838824, 2.0038666367310003])

        file_path = os.path.dirname(__file__)
        file_name = os.path.join(file_path, "He_20")
        eT_reader = eTLanczosReader(file_name, components=["X", "X", "X"])

        file_name_out = os.path.join(file_path, "output")
        eT_reader.generate_file(file_name_out)

        mean = MeanExcitationEnergy(file_name_out)

        computed = np.array([mean.I0, mean.ln_I0, mean.S0])
        assert np.allclose(reference, computed)

        os.remove(file_name_out)

    def test_mean_excitation_energy_units(self):

        reference = np.array([1.5537751068646541, 0.44068752259535465, 2.0038666367310003])

        file_path = os.path.dirname(__file__)
        file_name = os.path.join(file_path, "./He_20")
        eT_reader = eTLanczosReader(file_name)

        file_name_out = os.path.join(file_path, "output")
        eT_reader.generate_file(file_name_out, units="atomic")

        mean = MeanExcitationEnergy(file_name_out)

        computed = np.array([mean.I0, mean.ln_I0, mean.S0])
        assert np.allclose(reference, computed)

        os.remove(file_name_out)


    def test_mean_excitation_energy_X_2(self):

        reference = np.array([16.56409506030352, 2.807237404637121])

        file_path = os.path.dirname(__file__)
        file_name = os.path.join(file_path, "./H2_20")
        eT_reader = eTLanczosReader(file_name, components=["Z"])

        file_name_out = os.path.join(file_path, "output")
        eT_reader.generate_file(file_name_out)

        mean = MeanExcitationEnergy(file_name_out)

        computed = np.array([mean.I0, mean.ln_I0])
        assert np.allclose(reference, computed)

        os.remove(file_name_out)


