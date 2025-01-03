This repository contains my attempts to learn test automation with Playwright, Python, and Pytest.

After dabbling with the absolute basics and finishing the official Playwright tutorial, I found an excellent list of websites designed to practice testing on.: https://github.com/BMayhew/awesome-sites-to-test-on

Currently I am working through https://www.automationexercise.com/.

Tests for every website I tackled will be contained in separate directories.

One can either run all tests in the repository by using the `pytest` command in the root directory, or `pytest directory/` e.g., `pytest /automation_exercise` to run a set of tests limited to a single website.

Please note that automationexercise is the first website I practiced test automation on. The tests initially were all over the place, some tests were using Playwright-library headed boilerplate, some were using Pytest-specific test structure. It has been refactored to make the tests more consistent, but I still left some test cases that use Playwright-library structure, just as an example. A couple of tests are written entirely by hand, but most of the other tests I wrote with the help of the `playwright codegen` tool.

