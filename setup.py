from setuptools import setup, find_packages

setup(
    name="commit-ai",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "click",
        "google-generativeai",
        "python-dotenv",
    ],
    entry_points={
        "console_scripts": [
            "commit-ai=commit_ai.cli:main",
        ],
    },
    python_requires=">=3.7",
)