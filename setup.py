from setuptools import setup, find_packages

setup(
    name='gpthistory',
    version='0.3',
    description='A tool for searching through your chatgpt conversation history',
    author='Kaustubh Srivastava',
    author_email='kaustubh282.s@gmail.com',
    url='https://github.com/kaustubh-28/gpt-history',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'python-dotenv',
        'openai',
        'pandas',
        'numpy'
    ],
    entry_points='''
        [console_scripts]
        gpthistory=gpthistory.gpthistory:main
    ''',
)
