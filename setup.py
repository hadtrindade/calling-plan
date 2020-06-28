from setuptools import setup, find_packages


def read(filename):
    return [requirement.strip() for requirement in open(filename).readlines()]



setup(
    name="military-call",
    version="0.1.0", #major, minor, patch
    description="plano de chamada para militares",
    packeges=find_packages(exclude=['.venv','old-program','tests']),
    include_package_data=True,
    install_requires=read('requirements.txt'),
    extras_require={
            "dev" : read("requirements-dev.txt")
    }

)