# LinkedList

This repo is a basic shell for a python project for Blocky code tests.

## Getting started

I assume that you are working on a unix based system such as OS X or Ubuntu and
have installed

- mini conda

You do not need miniconda but as is common when working with python, if you
do not manage your environments, you may get unexpected results.

I recommend setting up an environment with conda and install pip

	conda create --name bky-ll python=3.10 pip

Activate the environment

    conda activate bky-ll

Install all the python dependencies

	pip install -r requirements.txt

Run the tests with

    make test

Make sure your code passes standard python formatting with

	make lint

When you want to clean up

    conda deactivate
    conda remove -n bky-ll --all
	make veryclean


## Acknowledgements

The project setup is loosely based around Martin Heinz's [Ultimate Setup for
Your Next Python
Project](https://towardsdatascience.com/ultimate-setup-for-your-next-python-project-179bda8a7c2c)
