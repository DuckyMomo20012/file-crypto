# A simple file storage console

A safety file storage (basic)

<table>
  <tr>
    <th>Python</th>
  </tr>
  <tr>
    <td>3.10.4</td>
  </tr>
</table>

## 1. Installation:

> NOTE: Requires `poetry` installed. [Guide](https://python-poetry.org/docs/master/#installation)

### 1.1. Install dependencies:

```bash
poetry install
```

### 1.2. Activate virtual environment:

```bash
poetry shell
```

### 1.3. Export PYTHONPATH (Important):

Change directory to project folder:

Windows:

```console
set PYTHONPATH=%cd%
```

Linux:

```bash
export PYTHONPATH=$(pwd)
```

## 2. Start app:

> NOTE: Run in virtual environment

```console
python app.py
```

OR

```console
poe dev
```
