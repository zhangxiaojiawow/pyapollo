# encoding: utf-8
"""
apollo 常用工具包
用于python项目连接携程apollo
For python project to get configuration from ctrip apollo

使用方式 / usage：
client = ApolloClient(app_id='bruce_test', config_server_url='http://106.12.25.204:8080')
client.start()

a = client.get_value('a')

提供自动热更新，可以在初始化ApolloClient时，设置更新的频率，默认5分钟更新
提供本地配置缓存以及服务异常监听
Automatic update is provided. When the Apollo client is initialized, the update frequency can be set. The default is 5 minutes
Provide local configuration cache and service exception monitoring

"""
from setuptools import setup, find_packages
import pyapollo

SHORT = u'a client for apollo'

setup(
    name='apollo-client',
    version=pyapollo.__version__,
    packages=find_packages(),
    install_requires=[
        'requests', 'eventlet'
    ],
    url='',
    author=pyapollo.__author__,
    author_email=pyapollo.__email__,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
    include_package_data=True,
    package_data={'': ['*.py', '*.pyc']},
    zip_safe=False,
    platforms='any',

    description=SHORT,
    long_description=__doc__,
)
