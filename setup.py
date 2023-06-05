from setuptools import find_packages, setup, Command

setup(
    name='llm_langchain',
    packages=find_packages(include=["llm_langchain", "llm_langchain.*"])
)