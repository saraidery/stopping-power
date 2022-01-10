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

class eTLanczosReader:
    def __init__(self, file_name, components=["X", "Y", "Z"]):

        self.file_name = os.path.expanduser(file_name.strip())
        self.components = components

    def _read_component(self, component, units):
        component = component.strip()
        component = component.lstrip()

        n, e_eV_Re, e_eV_Im, e_atomic_Re, e_atomic_Im, f = np.loadtxt(
            f"{self.file_name}_{component}", skiprows=1, unpack=True
        )

        if units == "atomic":
            return e_atomic_Re, f
        elif units == "eV":
            return e_eV_Re, f

    def _write_component_data(self, file, data):
        np.savetxt(file, data)

    def _write_file_header(self, file, units):
        file.write(f"Excitation energy [{units}] Oscilator strengths\n")

    def generate_component_file(self, file_name, component, units="eV"):

        if component in component:

            file = open(f"{file_name}_{component}", "w")
            self._write_file_header(file, units)

            e, f = self._read_component(component, units)
            self._write_component_data(file, np.c_[e, f])

            file.close()
        else:
            print(f"Component [{component}] is not defined")

    def generate_file(self, file_name, units="eV"):

        file = open(file_name, "w")
        self._write_file_header(file, units)

        for component in self.components:
            e, f = self._read_component(component, units)
            self._write_component_data(file, np.c_[e, f])

        file.close()
