# Contribution guidelines

These guidelines instruct how to submit issues and contribute. Please read the following [submission guidelines].

  [submission guidelines]: #submission-guidelines

## Code contributions

If you would like to fixed a bug or implemented an enhancement, you can contribute your changes via [Pull Request].
This is not restricted to code, on the contrary, fixes and enhancements alone are also very valuable.

  [Pull Request]: #pull-request

## Submission guidelines

### Reporting bugs

If you found a bug, you can help us by submitting an issue to the [issue tracker].
Even better, you can submit a [Pull Request] with a fix.

  [issue tracker]: https://github.com/little-scripts/scanvulnpy/issues/new/choose

Before you submit an issue, please search the issue tracker, maybe an issue for
your problem already exists, and the discussion might inform you of workarounds
readily available.

We want to fix all the issues as soon as possible, but before fixing a bug, we
need to reproduce and confirm it. In order to reproduce bugs, we will
systematically ask you to provide a minimal reproduction scenario using the
[Bug report template](.github/ISSUE_TEMPLATE/bug_report.md). Please stick to the issue template.

Notice that all information in the issue tracker is public. Do not include
any confidential information there.

Unfortunately, we are not able to investigate / fix bugs without a minimal
reproduction scenario, so if we don't hear back from you, we may close the issue.

### Enhancement requests

If you would like to implement a new feature, please submit an issue using
[Feature request template](.github/ISSUE_TEMPLATE/feature_request.md) with a proposal for your work first to be sure that it is of use to everyone.
Describe the new feature and use cases for it in as much detail as possible and
be prepared to contribute the code in the form of a [Pull Request].

### Pull Request

On GitHub pull requests are the main mechanism to contribute code.
GitHub has good articles explaining how to [set up Git], [fork a repository] and [use pull requests]
and we do not go through them in more detail. We do, however, recommend to
create dedicated topic branches for pull requests instead of creating
them based on the master branch. This is especially important if you plan to
work on multiple pull requests at the same time.

  [set up Git]: https://help.github.com/articles/set-up-git/
  [fork a repository]: https://help.github.com/articles/fork-a-repo/
  [use pull requests]: https://help.github.com/articles/using-pull-requests

1.  **Fork the repository**: Make your changes in a separate git branch and add descriptive messages to
    your commits.

2.  **Create a pull requests**: After, push your branch, send a PR to [dev].

    [dev]: https://github.com/little-scripts/scanvulnpy/pulls
