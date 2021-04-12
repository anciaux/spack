# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install libmultiscale-git
#
# You can edit this file again by typing:
#
#     spack edit libmultiscale-git
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Libmultiscale(CMakePackage):
    """LibMultiScale is a C++/python parallel framework for the multiscale
       coupling methods dedicated to material simulations """

    homepage = "https://libmultiscale.gitlab.io/libmultiscale"
    git = "https://gitlab.com/libmultiscale/libmultiscale.git"

    maintainers = ['anciaux']

    version('lammps_2020', branch='lammps_2020')

    depends_on('akantu@master')
    depends_on('expat')
    depends_on('lapack')
    depends_on('fftw')
    depends_on('gsl')
    depends_on('python@3.5.10:')

    resource(
        name='eigen',
        git='https://gitlab.com/libeigen/eigen.git',
        tag='3.4.0-rc1',
        destination='third-party/'
    )

    resource(
        name='pybind11',
        git='https://github.com/pybind/pybind11.git',
        tag='v2.6.2',
        destination='third-party/'
    )

    resource(
        name='lammps',
        git='https://gitlab.com/libmultiscale/lammps.git',
        tag='new_lammps',
        destination='third-party/'
    )

    def cmake_args(self):
        spec = self.spec
        args = [
            '-DLIBMULTISCALE_AKANTU_PLUGIN:BOOL=ON',
            '-DLIBMULTISCALE_MD1D:BOOL=ON',
            '-DLIBMULTISCALE_MECA1D:BOOL=ON',
            '-DLIBMULTISCALE_LAMMPS_PLUGIN:BOOL=ON'
        ]
        return args

    def cmake(self, spec, prefix):
        try:
            super().cmake(spec, prefix)
            super().cmake(spec, prefix)
        except Exception:
            super(Libmultiscale, self).cmake(spec, prefix)
            super(Libmultiscale, self).cmake(spec, prefix)
