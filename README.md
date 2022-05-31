# LinkedList

This repo is a basic shell for a python project for Blocky code tests.

## Getting started

I assume that you are working on a unix based system such as OS X or Ubuntu and
have installed

- python3
- pip

Personally, I recommend also using miniconda (or some other environment
management tool). If you do not manage environments, you may get unexpected
results.

I setup as follows:

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

## Your task

Create a function that takes as input a link list _L_ and returns linked list in
which the data entries of _L_ occur in the reverse order.  The input linked list
should not be modified.  Once you have successfully created this function, issue
a PR.

Your goal is to not only to get your code working, but do so in a way that it is
not painful for other developers to work with your code going forward

If you have any questions or run into any problems, feel free to reach out to
us via email.

Good luck!!

## Acknowledgements

The project setup is loosely based around Martin Heinz's [Ultimate Setup for
Your Next Python
Project](https://towardsdatascience.com/ultimate-setup-for-your-next-python-project-179bda8a7c2c)
