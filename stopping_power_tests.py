import os

from stopping_power import eTLanczosReader
from stopping_power import MeanExcitationEnergy

eT_reader = eTLanczosReader(
    "~/eT_testing/scr/eT.lanczos200", components=['X', 'X', 'Z']
)
eT_reader.generate_file("output")

mean = MeanExcitationEnergy("output")

print(f'S0: {mean.S0}')
print(f'I0: {mean.I0}')
print(f'ln(I0): {mean.ln_I0}')

os.remove("output")

