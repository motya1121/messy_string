import setuptools

setuptools.setup(
    name="random_string",  # これがパッケージ名になります～
    version="0.0.1",
    packages=['random_string'],  # moduleが入っているパッケージを選択してください～
    entry_points={
        'console_scripts': ['random_string = random_string:main'],
    },
)