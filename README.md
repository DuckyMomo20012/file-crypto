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
  - [Prerequisites](#bangbang-prerequisites)
  - [Run Locally](#running-run-locally)
- [Usage](#eyes-usage)
- [Settings](#wrench-settings)
- [Application Styles](#peach-application-styles)
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
  <img src="https://user-images.githubusercontent.com/64480713/175859655-3aac9d18-fe16-431c-9b65-5e8988c9cd0f.png" alt="screenshot" width="1024"/>
</div>

_Last updated: Jun 27, 2022_

<div align="center">
  <img src="https://user-images.githubusercontent.com/64480713/175549661-d0c4f7f7-c82b-4dfa-9fbf-69ef072218eb.gif" alt="screenshot" width="1024"/>
</div>

_Last updated: Jun 24, 2022_

<!-- TechStack -->

### :space_invader: Tech Stack

<details>
  <summary>Client</summary>
  <ul>
    <li><a href="https://www.python.org/">Python</a></li>
    <li><a href="https://ptg.bczsalba.com/pytermgui.html">PyTermGUI</a></li>
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
- 🔑 Password protection for file
- 🔍️ Preview text file in terminal
- ✏️ File editor in the terminal
- 🎨 Syntax highlight for supporting formats
- 🧰 Toolbox:
  - Sign file
  - Verify file signature
  - Encrypt file
  - Decrypt file
- 👀 (Preview feature) Preview image in terminal using ANSI codes

<!-- Color Reference -->

### :art: Color Reference

This color palette is based on [Nord](https://www.nordtheme.com/) theme.

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

To run this project, you will need to add the following environment variables to
your .env file.

`MONGODB_HOST`: An URI to connect to your database

E.g:

```
MONGODB_HOST="mongodb+srv://{username}:{password}@crypto-file.9mziwnd.mongodb.net/test"
```

You can also checkout file `.env.example` to see all required environment variables.

<!-- Getting Started -->

## :toolbox: Getting Started

<!-- Prerequisites -->

### :bangbang: Prerequisites

- Python: `>= 3.9`.

- Operating system: `Linux` and `macOS`.

  > **NOTE**: This app only supports `Linux` and `macOS`. Currently not supporting `Windows`.

- This project uses [Poetry](https://python-poetry.org/) as package manager:

  Linux, macOS, Windows (WSL)

  ```bash
  curl -sSL https://install.python-poetry.org | python3 -
  ```

  Read more about installation on
  [Poetry documentation](https://python-poetry.org/docs/master/#installation).

<!-- Run Locally -->

### :running: Run Locally

Clone the project:

```bash
git clone https://github.com/DuckyMomo20012/file-crypto.git
```

Go to the project directory:

```bash
cd file-crypto
```

Install dependencies:

```bash
poetry install
```

OR:

Export Poetry dependencies to file `requirements.txt`:

```bash
poetry export -f requirements.txt --output requirements.txt
```

> NOTE: You can add option: `--dev` to include development dependencies.

Then install dependencies with `pip`:

```bash
pip install -r requirements.txt
```

---

Activate virtual environment:

```bash
poetry shell
```

Start the program:

```bash
poe dev
```

OR

```bash
python3 app.py
```

<!-- Usage -->

## :eyes: Usage

First, you have to log in to your account on the **Login** page:

<details>
<summary>Screenshot</summary>

![login page](https://user-images.githubusercontent.com/64480713/175862816-cf2deeab-6c8b-4147-9da1-1992c9652334.png)

</details>

OR, you can create your new account on the **Register** page:

<details>
<summary>Screenshot</summary>

![register page](https://user-images.githubusercontent.com/64480713/175869157-6b3d5a96-21c8-4641-a7fc-69f3a5ab3c1f.png)

</details>

> **NOTE**: The email field must have a valid email format.

After login, you will see the **Dashboard** page:

![dashboard page](https://user-images.githubusercontent.com/64480713/175863076-068a2be8-d892-423f-9a19-736c6fc712ae.png)

- Your files will be grouped into dates.

- **Settings**: You can see and edit your account information or change your
  password here.

  <details>
  <summary>Screenshot</summary>

  ![settings page](https://user-images.githubusercontent.com/64480713/175869328-43ed970e-0f93-4c39-92c7-c32d55e396f9.png)

  </details>

  - **Your information**: This page will show you brief information about your
    account.

    <details>
    <summary>Screenshot</summary>

    ![your information page](https://user-images.githubusercontent.com/64480713/175869525-52fbfdc6-5cd4-4adc-a6d3-f1dfd8d7fe46.png)

    </details>

  - **Edit your information** page: You can edit your information here.

    <details>
    <summary>Screenshot</summary>

    ![edit your information page](https://user-images.githubusercontent.com/64480713/175869992-bac292ae-209c-467a-b6be-ad420cb7ebdc.png)

    </details>

    > **NOTE**: To edit your date of birth, your new value has to follow this format:
    > `YYYY-MM-DD`. E.g: 2022-01-01.

  - **Change password** page:

    <details>
    <summary>Screenshot</summary>

    ![change password page](https://user-images.githubusercontent.com/64480713/175870196-2a19e74e-075a-4713-9dc4-f1e1e6e371d7.png)

    </details>

  - **Logout**: This will log you out and redirect you to the **Login** page.

- **Tools**: This consists of multiple helpful tools:

  <details>
  <summary>Screenshot</summary>

  ![tools](https://user-images.githubusercontent.com/64480713/175871157-c16080ec-05cc-4d22-a3fb-ad21dcf25213.png)

  </details>

  - **Sign file**: This tool will create a file with the `.sig` extension in
    your save folder path, which is your file's signature. Later, another user
    can use the `Verify signed file` tool to check who has signed that file.

    <details>
    <summary>Screenshot</summary>

    ![sign file page](https://user-images.githubusercontent.com/64480713/175870557-db8c9a59-8042-4b83-99ed-4f985c4f3f60.png)

    </details>

  - **Verify signed file**: This tool will check all available users to verify
    that file was signed by a valid user.

    <details>
    <summary>Screenshot</summary>

    ![verify signed file page](https://user-images.githubusercontent.com/64480713/175870750-2128f1a2-3f3e-4491-be6e-74dc5143e03e.png)

    </details>

  - **Encrypt file**: This tool will create a file with `.bin` extension in your
    save folder path. The only targeted receiver can decrypt that file using the
    `Decrypt file` tool.

    > **NOTE**: You can target yourself as the receiver.

    <details>
    <summary>Screenshot</summary>

    ![encrypt file page](https://user-images.githubusercontent.com/64480713/175870830-ef7b1171-7a56-48a4-8848-7f710d63e266.png)

    </details>

  - **Decrypt file**: This tool will try to decrypt your encrypted and encode it
    if possible and save it to your save folder path.

    <details>
    <summary>Screenshot</summary>

    ![decrypt file page](https://user-images.githubusercontent.com/64480713/175870887-a2d6ff23-73c6-4e3e-bf5b-fc2a955cd7d5.png)

    </details>

    > **NOTE**: Encrypted file name **MUST** have `.bin` extension.

> **NOTE**: The file path and folder path can be an absolute path or relative
> path.
> E.g:
>
> ```
> ./src/pages/
> ./
> ../
> ./../
> /home/alice/Desktop/file-crypto
> /home/alice/Desktop/file-crypto/
> ```

> **NOTE**: Other fields without `(optional)` is required.

- **Upload**: You can upload your file here. After uploading, your file will be
  encrypted.

  <details>
  <summary>Screenshot</summary>

  ![upload file page](https://user-images.githubusercontent.com/64480713/175871068-3a874b63-070b-43a4-98b9-61dcb36566dc.png)

  </details>

  > **NOTE**: If you upload a file with the same name, the new file name will be
  > appended with a timestamp. E.g: `app_20220626221134.py`.

- **File preview**: After you type your password to unlock the file, the file
  will be opened in a window, **in preview mode**, and **using the `dracula`
  theme by default** (only available for text files).

  ![file preview page](https://user-images.githubusercontent.com/64480713/175871319-e8cd5fca-bc42-4c33-831f-73630bdcbede.png)

  > **NOTE**: **Preview mode** supports **text files** and **images files**.
  > **Edit mode** only supports **text files**.

  - In **Preview mode**, you can change many themes if the file extension is
    supported since we use [Pygments](https://pygments.org/) to enable syntax
    highlighting.

    <details>
    <summary>Screenshot</summary>

    ![theme picker page](https://user-images.githubusercontent.com/64480713/175872466-ac7558e1-82e9-48f4-aeac-df3472e68b04.png)

    </details>

    - You can turn off syntax highlighting by choosing `no theme` in the theme
      picker.

    - All supported file types: https://pygments.org/docs/lexers/

    > **NOTE**: If your file type is not supported, you should change to the `no theme` theme.

    - All available themes: https://pygments.org/styles/

    > **NOTE**: Some themes will be removed due to incompatible: `borland`,
    > `lilypond`, `trac`, `bw`, `algol`, `algol_nu`.

  - You can optionally switch to **Edit mode** with the `Edit mode` button:

    ![edit mode page](https://user-images.githubusercontent.com/64480713/175871596-612e8420-de73-4226-914e-3e0d3ec23917.png)

    > **NOTE**: Any changes with "newlines" `("\n")`, "tabs" `("\t")` or
    > "whitespace" `(" ")` will be consider as **"no changes"**, and won't be
    > saved.

  - You can also can **Download** this file to your computer or **Delete** this
    file.

    > NOTE: Delete will **completely delete** the file from the server.

  - **File information**: You can see brief information about your file.

    <details>
    <summary>Screenshot</summary>

    ![file information page](https://user-images.githubusercontent.com/64480713/175871882-0524d9b3-b803-4228-a1d8-d888b1fd71ff.png)

    </details>

  - **Edit file information**: You can edit your file name here.

    <details>
    <summary>Screenshot</summary>

    ![edit file information page](https://user-images.githubusercontent.com/64480713/175872134-241423fc-ca75-4428-951f-69f166ce07f6.png)

    </details>

  - **(Preview feature) Preview image file**: Using
    [CLImage](https://github.com/pnappa/CLImage) to display beautiful pictures
    using ANSI codes.

    ![image preview page](https://user-images.githubusercontent.com/64480713/175874258-5b9f63cd-5bfc-4d1a-8182-f85c07956337.png)

    > **NOTE**: This is a preview feature. This feature may reduce your computer
    > performance.

<!-- Settings -->

## :wrench: Settings

You can override default behaviors by configuring the `settings.json` file.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Description</th>
            <th>Default</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>workbench.preview.defaultColorTheme</code></td>
            <td>
                Default theme for file preview mode
            </td>
            <td>
                <code>'dracula'</code>
            </td>
        </tr>
        <tr>
            <td><code>workbench.preview.imageWidth</code></td>
            <td>
                Default image width for image preview mode
            </td>
            <td>
                <code>60</code>
            </td>
        </tr>
        <tr>
            <td><code>workbench.preview.defaultMode</code></td>
            <td>
                Default mode for preview page. Options: <code>preview</code>, <code>edit</code>
            </td>
            <td>
                <code>preview</code>
            </td>
        </tr>
        <tr>
            <td><code>workbench.animation</code></td>
            <td>
                Controls if animation is played when adding or remove windows
            </td>
            <td>
                <code>true</code>
            </td>
        </tr>
        <tr>
            <td><code>workbench.styles</code></td>
            <td>
                Load default styles to the application
            </td>
            <td>
                <code>[object Object]</code>
            </td>
        </tr>
    </tbody>
</table>

> NOTE: `workbench.animation` setting not apply to **modals** (error,
> success, warning) or **toast** messages.

> NOTE: `workbench.styles` will simply dump JSON to YAML and load them to the
> application. The default value for this setting is loaded from file
> `styles.yaml`.

<!-- Styles -->

## :peach: Application Styles

You can customize your application looks (text colors, border chars,...) by
changing default styles in file `styles.yaml`.

Read more about customizing on
[PyTermGUI documentation](https://ptg.bczsalba.com/pytermgui.html#how-to-configure-your-application-using-yaml).

<!-- Roadmap -->

## :compass: Roadmap

- [ ] Share files with other users
  - [ ] Download shared files
  - [ ] "Shared with me" tab to view shared files
  - [ ] File permission level. E.g: read-only, write,...
  - [ ] Edit shared files
- [ ] Apply themes for editing mode
- [ ] Trash can to store temporary deleted files
- [x] Preview mode for images
- [ ] Image size automatically resize on window resize in preview mode
- [x] Config default theme in user settings
- [ ] Config testing
<!-- Contributing -->

## :wave: Contributing

<a href="https://github.com/DuckyMomo20012/file-crypto/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=DuckyMomo20012/file-crypto" />
</a>

Contributions are always welcome!

<!-- Code of Conduct -->

### :scroll: Code of Conduct

Please read the [Code of Conduct](https://github.com/DuckyMomo20012/file-crypto/blob/main/CODE_OF_CONDUCT.md).

<!-- FAQ -->

## :grey_question: FAQ

- Is this project still maintained?

  - Yes, but we will only update UI, docs, or dependencies. New features won't
    be added frequently.

- Is this project ready for production?

  - No, this is a small project for practicing cryptographic systems or schemes.
    This wasn't meant for production.

- Are you planning to support Windows OS in the future?

  - No, we are not adding support for Windows any time soon (and most likely
    never).

- Error: `IndexError: list index out of range`:

  - Please update PyTermGUI to version 7.0.0 or higher to resolve this issue.

- Error: `assert self._drag_start is not None`:

  - Please update PyTermGUI to version 7.0.0 or higher to resolve this issue.

- Error: `ValueError: list.remove(x): x not in list`:

  - You are **clicking the button too fast** before the modal or window is fully
    closed. You should click the button **once** and wait for the modal or
    window is fully closed.

- In image preview mode, my image is broken:

  - That is because your **terminal width size is too small**. Image has a
    default width size is `60` block. Then terminal should be larger than that
    size (the nav bar wasn't counted).

- I can't decrypt my file using the `Decrypt file` tool:

  - Maybe the encrypted file is broken. You should ask the owner to resend
    the file.

- In preview mode for large text files, the app becomes very laggy:

  - Then you should change to the `no theme` theme.

- I have accidentally deleted the file, how can I restore it?

  - No, you can't. If the file is deleted, it will be **completely deleted**
    from our database and **can't be restored**.

- I can't load settings using the `settings.json` file:

  - Ensure your JSON format is correct. Notice that comment is not allowed in
    JSON files.

  - For application styles, make sure those styles are supported.

<!-- License -->

## :warning: License

Distributed under MIT license. See
[LICENSE](https://github.com/DuckyMomo20012/file-crypto/blob/main/LICENSE) for
more information.

<!-- Contact -->

## :handshake: Contact

Duong Vinh - [@duckymomo20012](https://twitter.com/duckymomo20012) - tienvinh.duong4@gmail.com

Project Link: [https://github.com/DuckyMomo20012/file-crypto](https://github.com/DuckyMomo20012/file-crypto).

<!-- Acknowledgments -->

## :gem: Acknowledgements

Here are useful resources and libraries that we have used in our projects:

- [PyTermGUI](https://ptg.bczsalba.com/pytermgui.html): A wonderful and fully
  documented TUI framework to make your terminal rocks.
- [Pygments](https://pygments.org/): A useful utility to add your favorite theme
  to your code.
- [CLImage](https://github.com/pnappa/CLImage): Print out magnificent pictures
  in your terminal using ANSI codes.
- [Awesome Readme Template](https://github.com/Louis3797/awesome-readme-template):
  A detailed template to bootstrap your README file quickly.
