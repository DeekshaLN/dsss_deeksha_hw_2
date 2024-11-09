from setuptools import setup, find_packages

setup(
    name="my_repository",           # Name of your package
    version="0.1.0",                # Initial version of your package
    author="Your Name",             # Your name or organization
    author_email="your_email@example.com",  # Your email
    description="A brief description of your package",
    long_description=open("README.md").read(),  # Read the content of the README file
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my_repository",  # Your project URL
    packages=find_packages(),  # Automatically discover all packages in the repository
    classifiers=[  # Classifiers help people discover your package
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Choose your license
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Minimum Python version required
    install_requires=[         # List of dependencies your package requires
        # "dependency1",
        # "dependency2",
    ],
)
