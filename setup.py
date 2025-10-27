from setuptools import setup, find_packages

setup(
    name="TEXT_LOOM",
    version="0.0.1",
    author="Israel Lallouz",
    author_email="israellallouz30@gmail.com",
    description="A terminal-based node editor for text manipulation",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/LLallouz/text-editing-network-llm",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "textual>=0.52.1",
        "fastapi>=0.104.0",
        "uvicorn[standard]>=0.24.0",
        "requests>=2.31.0",
        "pydantic>=2.0.0",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires=">=3.8",
    include_package_data=True,
    package_data={
        "TUI": ["themes/*"],
    },
)