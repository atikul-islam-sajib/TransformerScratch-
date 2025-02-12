from setuptools import setup, find_packages


def requirements():
    with open("./requirements.txt", "r") as file:
        return file.read().splitlines()


setup(
    name="TransformerScratch",
    version="0.0.1",
    description="A deep learning project that is build for NLP based task using Transformer",
    author="Atikul Islam Sajib",
    author_email="atikul.sajib@ptb.de",
    url="https://github.com/atikul-islam-sajib/TransformerScratch.git",  # Update with your project's GitHub repository URL
    packages=find_packages(),
    install_requires=requirements(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="TransformerScratch : machine-learning",
    project_urls={
        "Bug Tracker": "https://github.com/atikul-islam-sajib/TransformerScratch.git/issues",
        "Documentation": "https://github.com/atikul-islam-sajib/TransformerScratch.git",
        "Source Code": "https://github.com/atikul-islam-sajib/TransformerScratch.git",
    },
)
