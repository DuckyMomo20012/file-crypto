<div align="center">

  <h1>File Crypto</h1>

  <p>
    A simple file storage console
  </p>

<!-- Badges -->
<p>
  <a href="https://github.com/DuckyMomo20012/file-crypto/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/DuckyMomo20012/file-crypto" alt="contributors" />
  </a>
  <a href="">
    <img src="https://img.shields.io/github/last-commit/DuckyMomo20012/file-crypto" alt="last update" />
  </a>
  <a href="https://github.com/DuckyMomo20012/file-crypto/network/members">
    <img src="https://img.shields.io/github/forks/DuckyMomo20012/file-crypto" alt="forks" />
  </a>
  <a href="https://github.com/DuckyMomo20012/file-crypto/stargazers">
    <img src="https://img.shields.io/github/stars/DuckyMomo20012/file-crypto" alt="stars" />
  </a>
  <a href="https://github.com/DuckyMomo20012/file-crypto/issues/">
    <img src="https://img.shields.io/github/issues/DuckyMomo20012/file-crypto" alt="open issues" />
  </a>
  <a href="https://github.com/DuckyMomo20012/file-crypto/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/DuckyMomo20012/file-crypto.svg" alt="license" />
  </a>
</p>

<h4>
    <a href="https://github.com/DuckyMomo20012/file-crypto/">View Demo</a>
  <span> · </span>
    <a href="https://github.com/DuckyMomo20012/file-crypto">Documentation</a>
  <span> · </span>
    <a href="https://github.com/DuckyMomo20012/file-crypto/issues/">Report Bug</a>
  <span> · </span>
    <a href="https://github.com/DuckyMomo20012/file-crypto/issues/">Request Feature</a>
  </h4>
</div>

<br />

<!-- Table of Contents -->

# :notebook_with_decorative_cover: Table of Contents

- [About the Project](#star2-about-the-project)
  - [Screenshots](#camera-screenshots)
  - [Tech Stack](#space_invader-tech-stack)
  - [Features](#dart-features)
  - [Color Reference](#art-color-reference)
  - [Environment Variables](#key-environment-variables)
- [Getting Started](#toolbox-getting-started)
  - [System Requirements](#goberserk-system-requirements)
  - [Prerequisites](#bangbang-prerequisites)
  - [Installation](#gear-installation)
  - [Run Locally](#running-run-locally)
- [Usage](#eyes-usage)
- [Roadmap](#compass-roadmap)
- [Contributing](#wave-contributing)
  - [Code of Conduct](#scroll-code-of-conduct)
- [FAQ](#grey_question-faq)
- [License](#warning-license)
- [Contact](#handshake-contact)
- [Acknowledgements](#gem-acknowledgements)

<!-- About the Project -->

## :star2: About the Project

<!-- Screenshots -->

### :camera: Screenshots

<!-- How to record: asciinema rec demo.cast -c "poe dev" -i 0.1 -->

<!-- Then compress the gif using this site: https://ezgif.com/optimize -->

<div align="center">
  <img src="https://user-images.githubusercontent.com/64480713/175859655-3aac9d18-fe16-431c-9b65-5e8988c9cd0f.png" alt="screenshot"/>
</div>

<div align="center">
  <img src="https://user-images.githubusercontent.com/64480713/175549661-d0c4f7f7-c82b-4dfa-9fbf-69ef072218eb.gif" alt="screenshot"/>
</div>

<!-- TechStack -->

### :space_invader: Tech Stack

<details>
  <summary>Client</summary>
  <ul>
    <li><a href="https://www.python.org/">Python</a></li>
  </ul>
</details>

<details>
<summary>Database</summary>
  <ul>
    <li><a href="https://www.mongodb.com/">MongoDB</a></li>
  </ul>
</details>

<!-- Features -->

### :dart: Features

- 🔒️ Uploaded files are encrypted
- 🔑 Password protecting for file
- 🔍️ Preview text file in terminal
- ✏️ File editor in the terminal
- 🎨 Syntax highlight for supporting formats
- 🧰 Toolbox:
  - Encrypt file
  - Decrypt file
  - Sign file
  - Verify file signature
- 👀 Preview feature: Preview image in terminal using ANSI codes

<!-- Color Reference -->

### :art: Color Reference

| Color  | Hex                                                             |
| ------ | --------------------------------------------------------------- |
| nord0  | ![#2E3440](http://via.placeholder.com/10/2e3440?text=+) #2E3440 |
| nord1  | ![#3B4252](http://via.placeholder.com/10/3b4252?text=+) #3B4252 |
| nord2  | ![#434C5E](http://via.placeholder.com/10/434c5e?text=+) #434C5E |
| nord3  | ![#4C566A](http://via.placeholder.com/10/4c566a?text=+) #4C566A |
| nord4  | ![#D8DEE9](http://via.placeholder.com/10/d8dee9?text=+) #D8DEE9 |
| nord5  | ![#E5E9F0](http://via.placeholder.com/10/e5e9f0?text=+) #E5E9F0 |
| nord6  | ![#ECEFF4](http://via.placeholder.com/10/eceff4?text=+) #ECEFF4 |
| nord7  | ![#8FBCBB](http://via.placeholder.com/10/8fbcbb?text=+) #8FBCBB |
| nord8  | ![#88C0D0](http://via.placeholder.com/10/88c0d0?text=+) #88C0D0 |
| nord9  | ![#81A1C1](http://via.placeholder.com/10/81a1c1?text=+) #81A1C1 |
| nord10 | ![#5E81AC](http://via.placeholder.com/10/5e81ac?text=+) #5E81AC |
| nord11 | ![#BF616A](http://via.placeholder.com/10/bf616a?text=+) #BF616A |
| nord12 | ![#D08770](http://via.placeholder.com/10/d08770?text=+) #D08770 |
| nord13 | ![#EBCB8B](http://via.placeholder.com/10/ebcb8b?text=+) #EBCB8B |
| nord14 | ![#A3BE8C](http://via.placeholder.com/10/a3be8c?text=+) #A3BE8C |
| nord15 | ![#B48EAD](http://via.placeholder.com/10/b48ead?text=+) #B48EAD |

<!-- Env Variables -->

### :key: Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`MONGODB_HOST`: An URI to connect to your database

E.g: `MONGODB_HOST="mongodb+srv://{username}:{password}@crypto-file.9mziwnd.mongodb.net/test"`

<!-- Getting Started -->

## :toolbox: Getting Started

### :goberserk: System Requirements

> This app only supports Linux and macOS. Currently not supporting Windows.

- Python: `>= 3.9`
- OS: `Linux` and `macOS`

<!-- Prerequisites -->

### :bangbang: Prerequisites

This project uses [Poetry](https://python-poetry.org/) as package manager

Linux, macOS, Windows (WSL)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Read more on [documentation](https://python-poetry.org/docs/master/#installation)

<!-- Installation -->

### :gear: Installation

Install file-crypto with Poetry

```bash
poetry install
cd file-crypto
```

<!-- Run Locally -->

### :running: Run Locally

Clone the project

```bash
git clone https://github.com/DuckyMomo20012/file-crypto.git
```

Go to the project directory

```bash
cd file-crypto
```

Install dependencies

```bash
poetry install
```

Activate virtual environment

```bash
poetry shell
```

Start the program

```bash
poe dev
```

OR

```bash
python3 app.py
```

<!-- Usage -->

## :eyes: Usage

Use this space to tell a little more about your project and how it can be used. Show additional screenshots, code samples, demos or link to other resources.

TODO

<!-- Roadmap -->

## :compass: Roadmap

- [ ] Share images with other users
  - [ ] Download shared images
  - [ ] "Shared with me" tab to view shared files
  - [ ] Permission level. E.g: read-only, write,...
  - [ ] Edit shared files
- [ ] Apply themes for editing mode
- [ ] Trash can to store temporary deleted files
- [x] Preview mode for images

<!-- Contributing -->

## :wave: Contributing

<a href="https://github.com/DuckyMomo20012/file-crypto/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=DuckyMomo20012/file-crypto" />
</a>

Contributions are always welcome!

<!-- Code of Conduct -->

### :scroll: Code of Conduct

Please read the [Code of Conduct](https://github.com/DuckyMomo20012/file-crypto/blob/main/CODE_OF_CONDUCT.md)

<!-- FAQ -->

## :grey_question: FAQ

- Is this project still maintained?

  - Yes, but I will only update UI, docs, or dependencies. New features won't be
    added frequently.

- Is this project ready for production?

  - No, this is a small project for practicing cryptographic systems or schemes.
    This wasn't meant for production.

<!-- License -->

## :warning: License

Distributed under MIT license. See [LICENSE](https://github.com/DuckyMomo20012/file-crypto/blob/main/LICENSE) for more information.

<!-- Contact -->

## :handshake: Contact

Duong Vinh - [@duckymomo20012](https://twitter.com/duckymomo20012) - tienvinh.duong4@gmail.com

Project Link: [https://github.com/DuckyMomo20012/file-crypto](https://github.com/DuckyMomo20012/file-crypto)

<!-- Acknowledgments -->

## :gem: Acknowledgements

Here are useful resources and libraries that I have used in my projects.

- [PyTermGUI](https://ptg.bczsalba.com/pytermgui.html)
- [Pygments](https://pygments.org/)
- [Awesome Readme Template](https://github.com/Louis3797/awesome-readme-template)
