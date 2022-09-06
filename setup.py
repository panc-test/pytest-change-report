"""
pip install 模块名 :在线安装，会安装该包的相关依赖包；
python setup.py install :下载源码包然后在本地安装，不会安装该包的相关依赖包.
setup.py 描述安装包相关的信息

"""
from setuptools import setup

setup(
    name='pytest-change-report',
    url='https://github.com/panc-test/pytest-change-report',
    version='1.0',
    author="panc-test",
    author_email='123456@qq.com',
    description='turn . into √，turn F into x',
    long_description='print result on terminal turn . into √，turn F into x using hook',
    classifiers=[
        'Framework :: Pytest',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 3.6',
    ],
    license='proprietary',
    py_modules=['pytest_change_report'],
    keywords=[
        'pytest', 'py.test', 'pytest-change-report',
    ],

    install_requires=[
        'pytest'
    ],
    entry_points={
        'pytest11': [
            'change-report = pytest_change_report',
        ]
    }
)
