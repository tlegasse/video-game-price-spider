from setuptools import setup, find_packages

setup(
    name='video_game_price_spider',
    version='0.1.0',
    packages=find_packages(),
    include_package_data= True,
    install_requires=[
        'requests>=2.22',
        'typing>=3',
        'pandas>=1',
        'Click'
    ],
    test_suite="tests",
    entry_points='''
        [console_scripts]
        video_game_price_spider=video_game_price_spider.scripts.cli:cli
    '''
)
