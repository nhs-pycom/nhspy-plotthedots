# nhspy-plotthedots v0.1.0 {alpha}

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![pytest+flake8](https://github.com/nhs-pycom/nhspy-plotthedots/actions/workflows/pytest_flake8.yml/badge.svg)](https://github.com/nhs-pycom/nhspy-plotthedots/actions/workflows/pytest_flake8.yml)
[![codecov](https://codecov.io/gh/nhs-pycom/nhspy-plotthedots/branch/main/graph/badge.svg?token=WJUC4OBRLM)](https://codecov.io/gh/nhs-pycom/nhspy-plotthedots)
[![Contributors][contributors-shield]][contributors-url]
[![Code Lines][code-lines]][code-lines-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/nhs-pycom/nhspy-plotthedots">
    <img src="logo.png" alt="Logo" width="180">
  </a>

  <h3 align="center">nhspy-plotthedots v0.1.0 {alpha}</h3>

  <p align="center">
    NHS Python Community
    <br />
    <a href="https://nhs-pycom.github.io/nhspy-plotthedots/"><strong>Explore the docs »</strong></a>
    <br />
    <a href="https://github.com/nhs-pycom/nhspy-plotthedots/issues">Report Bug</a>
    ·
    <a href="https://github.com/nhs-pycom/nhspy-plotthedots/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <!-- <li><a href="#prerequisites">Prerequisites</a></li> -->
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

### Note: This is an alpha project, not for use in production until v1.0.0

We are working with the NHS-R community to develop a python implementation of 'NHSRplotthedots' SPC package to support NHSE/I 'Making Data Count' programme

Base Code by [Tom Jemmett](https://github.com/tomjemmett)

- [https://gist.github.com/tomjemmett/c167376e5b6464ec1c00975be2d7864e](https://gist.github.com/tomjemmett/c167376e5b6464ec1c00975be2d7864e)

- [Package Template](https://github.com/NHSDigital/rap-package-template) from NHS Digital's [RAP Community of Practice](https://nhsdigital.github.io/rap-community-of-practice/)

_**Note:** No private or patient data are shared in this repository._

### Folder Stucture

| Name                   | Link                                                                                    | Description                                                     |
| ---------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| .github/workflows | [[Link](https://github.com/nhs-pycom/nhspy-plotthedots/tree/main/.github/workflows)] | Azure Data Factory notebooks for running ephemeral job clusters |
| nhspy-plotthedots     | [[Link](https://github.com/nhs-pycom/nhspy-plotthedots/tree/main/nhspy_plotthedots)]               | Project folder                      |
| ~/data    | [[Link](https://github.com/nhs-pycom/nhspy-plotthedots/tree/main/nhspy_plotthedots/data)]               | Example datasets                              |
| ~/dev    | [[Link](https://github.com/nhs-pycom/nhspy-plotthedots/tree/main/nhspy_plotthedots/dev)]               | For testing new code                            |
| ~/utilities        | [[Link](https://github.com/nhs-pycom/nhspy-plotthedots/tree/main/nhspy_plotthedots/utilities)]                   | Helper functions                            |
| tests/unittests        | [[Link](https://github.com/nhs-pycom/nhspy-plotthedots/tree/main/tests/unittests)]                   | Unit testing framework                             |

### Built With

- [Python 3](https://www.python.org/)

<!-- GETTING STARTED -->

## Getting Started

To get up and running follow these simple steps.

### Installation

```bash
pip install --index-url https://test.pypi.org/simple/ --no-deps nhspy-plotthedots-test
```

Note this is the the test version of pypi, not for use in production.
<!-- USAGE EXAMPLES -->

## Usage

Please refer to our [Read the Docs](https://nhs-pycom.github.io/nhspy-plotthedots/) site

<!-- ROADMAP -->

## Roadmap

See the [open issues](https://github.com/nhs-pycom/nhspy-plotthedots/issues) for a list of proposed features (and known issues).

<!-- CONTRIBUTING-->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

_See [CONTRIBUTING.md](https://github.com/nhs-pycom/nhspy-plotthedots/blob/main/CONTRIBUTING.md) for detailed guidance._

<!-- LICENSE -->

## License

Distributed under the MIT License. _See [LICENSE.md](https://github.com/nhs-pycom/nhspy-plotthedots/blob/main/LICENSE) for more information._

<!-- CONTACT -->

## About

Project contact email: [craig.shenton@nhs.net](mailto:craig.shenton@nhs.net)

## Acknowledgements

- [Tom Jemmett](https://github.com/tomjemmett)
- [NHS-R Community](https://nhsrcommunity.com/)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/nhs-pycom/nhspy-plotthedots.svg?color=blue
[contributors-url]: https://github.com/nhs-pycom/nhspy-plotthedots/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/nhs-pycom/nhspy-plotthedots.svg?color=blue
[forks-url]: https://github.com/nhs-pycom/nhspy-plotthedots/network/members
[stars-shield]: https://img.shields.io/github/stars/nhs-pycom/nhspy-plotthedots.svg?color=blue
[stars-url]: https://github.com/nhs-pycom/nhspy-plotthedots/stargazers
[issues-shield]: https://img.shields.io/github/issues/nhs-pycom/nhspy-plotthedots.svg?color=blue
[issues-url]: https://github.com/nhs-pycom/nhspy-plotthedots/issues
[license-shield]: https://img.shields.io/github/license/nhs-pycom/nhspy-plotthedots.svg?color=blue
[license-url]: https://github.com/nhs-pycom/nhspy-plotthedots/blob/main/LICENSE
[code-lines]: https://img.shields.io/tokei/lines/github/nhs-pycom/nhspy-plotthedots?color=blue&label=Code%20Lines
[code-lines-url]: https://github.com/nhs-pycom/nhspy-plotthedots
