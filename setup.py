from setuptools import setup

extra_requirements = {"tests": ["pytest", "coverage", "pytest-cov"]}

setup(
    name="stopping-power",
    author="Sarai D. Folkestad",
    description="Computes average excitation energies and stopping power",
    install_requires=["numpy"],
    extras_require=extra_requirements,
)
