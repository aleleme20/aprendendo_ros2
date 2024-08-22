from setuptools import find_packages, setup

package_name = 'pacote1_alexandre'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch_alexandre/launch_alexandre.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Alexandre Leme',
    maintainer_email='aleamaral.leme@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'no_exemplo_1 = pacote1_alexandre.no_exemplo_1:main',
            'no_exemplo_2 = pacote1_alexandre.no_exemplo_2:main'
        ],
    },
)
