import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fcm_notifier", # Replace with your own username
    version="0.0.1",
    author="Bryan Lincoln M. de Oliveira",
    author_email="bryanufg@gmail.com",
    description="A python module to notify about ML model training statuses with Firebase Cloud Messaging.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bryanlincoln/ml-notifier",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)