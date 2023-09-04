
<!-- omit in toc -->
# Contributing to twAuto🦆

First off, thanks for taking the time to contribute! ❤️

All types of contributions are encouraged and valued. See the [Table of Contents](#table-of-contents) for different ways to help and details about how this project handles them. Please make sure to read the relevant section before making your contribution. It will make it a lot easier for us maintainers and smooth out the experience for all involved. The community looks forward to your contributions. 🎉

> And if you like the project, but just don't have time to contribute, that's fine. There are other easy ways to support the project and show your appreciation, which we would also be very happy about:
> - Star the project
> - Refer this project in your project's readme


<!-- omit in toc -->
## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [I Have a Question](#i-have-a-question)
  - [I Want To Contribute](#i-want-to-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Enhancements](#suggesting-enhancements)
  - [Improving The Documentation](#improving-the-documentation)


## Code of Conduct

This project and everyone participating in it is governed by the
[twAuto Code of Conduct](https://github.com/EKOzkan/twAuto/blob//CODE_OF_CONDUCT.md).
By participating, you are expected to uphold this code. Please report unacceptable behaviour
to <ekinkagan@gmail.com>.


## I Have a Question

> If you want to ask a question, we assume that you have read the available [Documentation]().

Before you ask a question, it is best to search for existing [Issues](https://github.com/EKOzkan/twAuto/issues) that might help you. In case you have found a suitable issue and still need clarification, you can write your question in this issue. It is also advisable to search the internet for answers first.

If you then still feel the need to ask a question and need clarification, we recommend the following:

- Open an [Issue](https://github.com/EKOzkan/twAuto/issues/new).
- Provide as much context as you can about what you're running into.
- Provide project, selenium and driver versions.

We will then take care of the issue as soon as possible.



## I Want To Contribute

> ### Legal Notice <!-- omit in toc -->
> When contributing to this project, you must agree that you have authored 100% of the content, that you have the necessary rights to the content and that the content you contribute may be provided under the project licence.

### How to Contribute
1.  Fork the repository to your own GitHub account.
    
2.  Clone the forked repository to your local machine.
    
    
    `git clone https://github.com/EKOzkan/twAuto.git` 
    
3.  Create a new branch for your contribution.

    `git checkout -b feature/your-feature-name` 
    
5.  Make your changes or additions to the codebase.
    
6.  Test your changes thoroughly to ensure they work as expected.
    
7.  Commit your changes with a clear and descriptive commit message.
    
    
    `git commit -m "Add feature: your-feature-name"` 
    
8.  Push your changes to your GitHub fork.
    
    
    `git push origin feature/your-feature-name` 
    
9.  Open a pull request (PR) to the original repository.

### Pull Request Guidelines
When submitting a pull request, please make sure to:

-   Provide a clear and concise title for your PR.
-   Describe the purpose of your changes in the PR description.
-   Reference any related issues or discussions in your PR description.
-   Be open to feedback and be prepared to make additional changes if needed.


### Notes for Contributors
-   Please try to use `testId` in the testId mode and `xPath` in the xPath mode. I know that not every element has a `testId`, so at some point you may be forced to use `xPaths`, but please try to avoid it as much as possible for writing the code for the testId mode.
-   If you want to add a new feature to the project, please implement it for both modes (xPath and testId). If you cant, no problem, I will check if it possible to do after your pull request.
-   Try to avoid functions that affect the user's system, such as copy and paste functions, etc.


#### Before Submitting a Bug Report

A good bug report shouldn't leave others needing to chase you up for more information. Therefore, we ask you to investigate carefully, collect information and describe the issue in detail in your report. Please complete the following steps in advance to help us fix any potential bug as fast as possible.

- Make sure that you are using the latest version.
- Determine if your bug is really a bug and not an error on your side e.g. using incompatible environment components/versions (Make sure that you have read the [documentation](). If you are looking for support, you might want to check [this section](#i-have-a-question)).
- To see if other users have experienced (and potentially already solved) the same issue you are having, check if there is not already a bug report existing for your bug or error in the [bug tracker](https://github.com/EKOzkan/twAuto/issues?q=label%3Abug).
- Also make sure to search the internet (including Stack Overflow) to see if users outside of the GitHub community have discussed the issue.

- Collect information about the bug:
  - Stack trace (Traceback)
  - OS, Platform and Version (Windows, Linux, macOS, x86, ARM)
  - Version of the interpreter, compiler, SDK, runtime environment, package manager, depending on what seems relevant.
  - Possibly your input and the output
  - Can you reliably reproduce the issue? And can you also reproduce it with older versions?

#### How Do I Submit a Good Bug Report?

> You must never report security related issues, vulnerabilities or bugs including sensitive information to the issue tracker, or elsewhere in public. Instead sensitive bugs must be sent by email to <ekinkagan@gmail.com>.


We use GitHub issues to track bugs and errors. If you run into an issue with the project:

- Open an [Issue](https://github.com/EKOzkan/twAuto/issues/new). (Since we can't be sure at this point whether it is a bug or not, we ask you not to talk about a bug yet and not to label the issue.)
- Explain the behaviour you would expect and the actual behaviour.
- Please provide as much context as possible and describe the *reproduction steps* that someone else can follow to recreate the issue on their own. This usually includes your code. For good bug reports you should isolate the problem and create a reduced test case.
- Please provide your code, <u>**DONT FORGET TO DELETE YOUR LOGIN INFO!**
- Try our [Debug Mode](https://github.com/EKOzkan/twAuto#:~:text=debugMode%3D%20True/False%20%23Really%20poorly%20implemented%20debug%20mode%2C%20this%20is%20for%20reading%20occured%20errors.%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23It%20is%20not%20reliable%20right%20now%20but%20you%20can%20give%20it%20a%20try%20if%20you%20want%20to.) to provide as much as info you can.
- Provide the information you collected in the previous section.




### Suggesting Enhancements

This section guides you through submitting an enhancement suggestion for twAuto, **including completely new features and minor improvements to existing functionality**. Following these guidelines will help maintainers and the community to understand your suggestion and find related suggestions.

#### Before Submitting an Enhancement

- Make sure that you are using the latest version.
- Read the [documentation]() carefully and find out if the functionality is already covered, maybe by an individual configuration.
- Perform a [search](https://github.com/EKOzkan/twAuto/issues) to see if the enhancement has already been suggested. If it has, add a comment to the existing issue instead of opening a new one.
- Find out whether your idea fits with the scope and aims of the project. It's up to you to make a strong case to convince the project's developers of the merits of this feature. Keep in mind that we want features that will be useful to the majority of our users and not just a small subset. If you're just targeting a minority of users, consider writing an add-on/plugin library.

#### How Do I Submit a Good Enhancement Suggestion?

Enhancement suggestions are tracked as [GitHub issues](https://github.com/EKOzkan/twAuto/issues).

- Use a **clear and descriptive title** for the issue to identify the suggestion.
- Provide a **step-by-step description of the suggested enhancement** in as many details as possible.
- **Describe the current behaviour** and **explain which behaviour you expected to see instead** and why. At this point you can also tell which alternatives do not work for you.
- **Explain why this enhancement would be useful** to most twAuto users. You may also want to point out the other projects that solved it better and which could serve as inspiration.


