from setuptools import find_packages, setup

package_name = 'meu_primeiro_pacote'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Alexandre Leme',
    maintainer_email='aleamaral.leme@gmail.com',
    description='Meu primeiro pacote em ROS2',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'meu_primeiro_no = meu_primeiro_pacote.meu_primeiro_no:main'
        ],
    },
)
