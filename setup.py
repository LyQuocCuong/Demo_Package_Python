from setuptools import setup, find_packages
setup(
    name='MultiPackage',
    # packages=['SinglePackage'],
    packages=find_packages(),  # use for multi packages (MultiPackage)
    version='0.1',
    description='Testing installation of Package',
    url='#',
    author='malhar',
    author_email='mlathkar@gmail.com',
    license='MIT',
    # defines whether the package is installed in compressed mode or regular mode
    zip_safe=False,
    # defines the command use in Terminal, Console
    entry_points={
        'console_scripts': [
            'get_staffId = MultiPackage.statistic.main:get_my_staffid',
            'gte_my_age = MultiPackage.statistic.main:calculate_age'
        ]
    }
)
