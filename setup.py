from setuptools import setup

extras = {
    'xls': ['openpyxl','xlrd'],
    'parquet': ['pyarrow'],
    'psql': ['psycopg2-binary'],
    'mysql': ['mysql-connector'],
}

setup(
    name='d6tstackmod',
    version='1',
    packages=['d6tstackmod'],
    url='https://github.com/valeriozhang/d6tstack/archive/1.tar.gz',
    license='MIT',
    author='DataBolt Team',
    author_email='valeriozhang14@gmail.com',
    description='d6tstackmod: Quickly ingest CSV and XLS files. Export to pandas, SQL, parquet',
    long_description='Quickly ingest raw files. Works for XLS, CSV, TXT which can be exported to CSV, Parquet, SQL and Pandas. d6tstack solves many performance and schema problems typically encountered when ingesting raw files.',
    install_requires=[
        'numpy','pandas>=0.22.0','sqlalchemy','scipy','d6tcollect'
    ],
    extras_require=extras,
    include_package_data=True,
    python_requires='>=3.5',
    keywords=['d6tstackmod', 'ingest csv'],
    classifiers=[]
)
