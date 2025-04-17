from setuptools import setup, find_packages

setup(
    name="autoeda",
    version="1.0.0",
    author="Dhruv Sanghvi",
    author_email="sanghvidhruv20@gmail.com",
    description="An automated exploratory data analysis (EDA) tool including visualisation",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    # Replace with your GitHub repo URL
    url="https://github.com/yourusername/autoeda",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "seaborn",
        "matplotlib",
        "ydata-profiling",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
