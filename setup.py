import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "End-to-end-Machine-Learning-Project-with-MLflow"
AUTHOR_USER_NAME = "EmmaculateC"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "chelangatemmaculate77@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small Python package for ML app",
    long_description=long_description,
    long_description_content_type="text/markdown",  # Fixed the argument name
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},  # Maps package root to the "src/" folder
    packages=setuptools.find_packages(where="src"),  # Finds all packages in "src/"
    install_requires=[],  # Add dependencies here, e.g., ["numpy", "pandas"]
    include_package_data=True,  # Include files specified in MANIFEST.in
    python_requires=">=3.7",  # Minimum Python version required
)
