
import glob
from pythonforandroid.toolchain import (
    CythonRecipe,
    Recipe,
    current_directory,
    info,
    shprint,
)
from os.path import join
import sh


class TwistedRecipe(CythonRecipe):
    version = '16.1.1'
    url = 'https://pypi.python.org/packages/source/T/Twisted/Twisted-{version}.tar.bz2'

    depends = ['setuptools', 'zope_interface']

    call_hostpython_via_targetpython = False
    install_in_hostpython = True

    def prebuild_arch(self, arch):
        super(TwistedRecipe, self).prebuild_arch(arch)
        # TODO Need to whitelist tty.pyo and termios.so here
        print('Should remove twisted tests etc. here, but skipping for now')

    def get_recipe_env(self, arch):
        env = super(TwistedRecipe, self).get_recipe_env(arch)
        # We add BUILDLIB_PATH to PYTHONPATH so twisted can find _io.so
        env['PYTHONPATH'] = ':'.join([
            self.ctx.get_site_packages_dir(),
            env['BUILDLIB_PATH'],
        ])
        return env

recipe = TwistedRecipe()
