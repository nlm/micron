from setuptools import setup,find_packages

setup(
    name = "micron",
    version = "1.0",
    packages = find_packages(),
    author = "Nicolas Limage",
    author_email = 'github@xephon.org',
    description = "minimal cron alternative for container",
    license = "MIT",
    keywords = "crontab container",
    url = "https://github.com/nlm/micron",
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
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
