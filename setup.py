from setuptools import setup

setup(
    name='snapshotalyzer-30000',
    version='0.1',
    author="Deepa P",
    author_email="writetodeepa.p@gmail.com",
    description="It is a demo project to learn about EC2 Instances",
    license="GPLv3+",
    packages=['shotty'],
    url="https://github.com/gyandeepa/snapshotalyzer-30000",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
        ''',    
)
