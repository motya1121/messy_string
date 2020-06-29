from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# long_description(後述)に、GitHub用のREADME.mdを指定
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="messy_string",  # これがパッケージ名になります～
    packages=['messy_string'],  # moduleが入っているパッケージを選択してください～
    version="0.2.0",
    license='MIT',
    author='motya0414',  # パッケージ作者の名前
    author_email='motya0414@hotmail.co.jp',  # パッケージ作者の連絡先メールアドレス
    url='https://github.com/motya1121/messy_string',
    description='A tool to generate random character strings based on parameters',
    long_description=long_description,  # PyPIに'Project description'として表示されるパッケージの説明文
    long_description_content_type='text/markdown',
    keywords='random string',  # PyPIでの検索用キーワードをスペース区切りで指定
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6'
    ],
    entry_points={
        'console_scripts': ['messy_string = messy_string:main'],
    },
)