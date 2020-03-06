from setuptools import setup,find_packages

with open("README.md", "r") as fd:
    long_description = fd.read()

setup(
    name = "micron",
    version = "1.0.post1",
    packages = find_packages(),
    author = "Nicolas Limage",
    author_email = 'github@xephon.org',
    description = "minimal cron alternative for containers",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    license = "MIT",
    keywords = "crontab container",
    url = "https://github.com/nlm/micron",
    python_requires = '>=3.6',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
    install_requires = [
        'crontab',
    ],
    entry_points = {
        'console_scripts': [
            'micron = micron:main',
        ],
    },
)
