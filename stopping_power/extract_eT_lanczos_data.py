import numpy as np
import os


class eTLanczosReader:
    def __init__(self, file_name, components=["X", "Y", "Z"]):

        self.file_name = os.path.expanduser(file_name.strip())
        self.components = components

    def _read_component(self, component, units):
        component = component.strip()
        component = component.lstrip()

        n, e_atomic_Re, e_atomic_Im, e_eV_Re, e_eV_Im, f = np.loadtxt(
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

    def generate_component_file(self, file_name, component, units="atomic"):

        if component in component:

            file = open(f"{file_name}_{component}", "w")
            self._write_file_header(file, units)

            e, f = self._read_component(component, units)
            self._write_component_data(file, np.c_[e, f])

            file.close()
        else:
            print(f"Component [{component}] is not defined")

    def generate_file(self, file_name, units="atomic"):

        file = open(file_name, "w")
        self._write_file_header(file, units)

        for component in self.components:
            e, f = self._read_component(component, units)
            self._write_component_data(file, np.c_[e, f])

        file.close()
