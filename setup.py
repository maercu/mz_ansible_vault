import setuptools

setuptools.setup(
    name="mz_ansible_vault", # Replace with your own username
    version="0.9",
    author="Marcel Zehnder",
    author_email="dev@maercu.ch",
    description="ansible-vault helpter",
    url="https://github.com/maercu/mz_ansible_vault.git",
    packages=setuptools.find_packages(),
    install_requires=['ansible'],
)