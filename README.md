![](https://zambeel.lums.edu.pk/ps/images/zmlogo.png)

# Zambeel Sniper

Snipe Courses on Zambeel.

The script monitors the first course in the shopping list and automatically enrolls as soon as it opens.

## Installation

### Clone Repository

```
git clone https://github.com/millionhz/zambeel-sniper.git
```

### Install Requirements

```
pip install -r requirements.txt
```

## Usage

```
usage: snipe.py [-h] roll password

Snipe courses on zambeel.

positional arguments:
  roll        zambeel roll number
  password    zambeel password

options:
  -h, --help  show this help message and exit
```

### Example

```
python snipe.py '24100999' 'my_password'
```

