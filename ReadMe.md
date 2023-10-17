AptSourcesList.py [![Unlicensed work](https://raw.githubusercontent.com/unlicense/unlicense.org/master/static/favicon.png)](https://unlicense.org/)
===============
~~![GitLab Build Status](https://gitlab.com/KOLANICH/AptSourcesList.py/badges/master/pipeline.svg)~~
~~[wheel (GHA via `nightly.link`)](https://nightly.link/KOLANICH-libs/AptSourcesList.py/workflows/CI/master/AptSourcesList-0.CI-py3-none-any.whl)~~
~~[![GitHub Actions](https://github.com/KOLANICH-libs/AptSourcesList.py/workflows/CI/badge.svg)](https://github.com/KOLANICH-libs/AptSourcesList.py/actions/)~~
~~![GitLab Coverage](https://gitlab.com/KOLANICH/AptSourcesList.py/badges/master/coverage.svg)~~
[![Libraries.io Status](https://img.shields.io/librariesio/github/KOLANICH-libs/AptSourcesList.py.svg)](https://libraries.io/github/KOLANICH-libs/AptSourcesList.py)
[![Code style: antiflash](https://img.shields.io/badge/code%20style-antiflash-FFF.svg)](https://codeberg.org/KOLANICH-tools/antiflash.py)

**We have moved to https://codeberg.org/KFmts/AptSourcesList.py (the namespace has changed to `KFmts`, which groups packages related to parsing or serialization), grab new versions there.**

Under the disguise of "better security" Micro$oft-owned GitHub has [discriminated users of 1FA passwords](https://github.blog/2023-03-09-raising-the-bar-for-software-security-github-2fa-begins-march-13/) while having commercial interest in success and wide adoption of [FIDO 1FA specifications](https://fidoalliance.org/specifications/download/) and [Windows Hello implementation](https://support.microsoft.com/en-us/windows/passkeys-in-windows-301c8944-5ea2-452b-9886-97e4d2ef4422) which [it promotes as a replacement for passwords](https://github.blog/2023-07-12-introducing-passwordless-authentication-on-github-com/). It will result in dire consequencies and is competely inacceptable, [read why](https://codeberg.org/KOLANICH/Fuck-GuanTEEnomo).

If you don't want to participate in harming yourself, it is recommended to follow the lead and migrate somewhere away of GitHub and Micro$oft. Here is [the list of alternatives and rationales to do it](https://github.com/orgs/community/discussions/49869). If they delete the discussion, there are certain well-known places where you can get a copy of it. [Read why you should also leave GitHub](https://codeberg.org/KOLANICH/Fuck-GuanTEEnomo).

---

This is the library to parse APT `sources.list` and serialize the modified version back.

Requirements
------------
* [`UniGrammarRuntime`](https://codeberg.org/UniGrammar/UniGrammarRuntime.py)
* Any of the parser libs:
  * [`parglare`](https://github.com/igordejanovic/parglare) ![Licence](https://img.shields.io/github/license/igordejanovic/parglare.svg) [![PyPi Status](https://img.shields.io/pypi/v/parglare.svg)](https://pypi.python.org/pypi/parglare) [![Libraries.io Status](https://img.shields.io/librariesio/github/igordejanovic/parglare.svg)](https://libraries.io/github/igordejanovic/parglare)
