from setuptools import find_packages,setup

setup(
    name='mcqgenrator',
    version='0.0.1',
    author='harshit aggarwal',
    author_email='aggarwalharshit99@gmmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2","ctransformers"],
    packages=find_packages()
)