from setuptools import setup, find_namespace_packages
from tethys_apps.app_installation import find_resource_files
import fix_tethys_init_files

# -- Apps Definition -- #
app_package = 'hydroviewer_peru'
release_package = 'tethysapp-' + app_package

# -- Python Dependencies -- #
dependencies = [
    'requests',
    'netCDF4',
    'numpy',
    'scipy',
    'gdal',
]

# -- Get Resource File -- #
resource_files = find_resource_files('tethysapp/' + app_package + '/templates', 'tethysapp/' + app_package)
resource_files += find_resource_files('tethysapp/' + app_package + '/public', 'tethysapp/' + app_package)
resource_files += find_resource_files('tethysapp/' + app_package + '/workspaces', 'tethysapp/' + app_package)

fix_tethys_init_files.fix_tethys_init_files(3)

setup(
    name=release_package,
    version='1',
    description='',
    long_description='',
    keywords='',
    author='',
    author_email='',
    url='',
    license='',
    packages=find_namespace_packages(),
    package_data={'': resource_files},
    include_package_data=True,
    zip_safe=False,
    install_requires=dependencies,
)