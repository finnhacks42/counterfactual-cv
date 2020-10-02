import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='ccrossval', # Replace with your own username
    version='0.0.1',
    description="cross validation for individual causal effect identification",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'tensorflow',
        'econml',
        'optuna'
    ]
)