
twcs2PersonaChat 🐦2🤖
======================
[![Issues](	https://img.shields.io/github/issues/gonmelo/leek)](https://github.com/gonmelo/leek/issues)
[![Forks](https://img.shields.io/github/forks/gonmelo/leek)](https://github.com/gonmelo/leek)
[![License](https://img.shields.io/github/license/gonmelo/leek)](https://packagist.org/packages/aimeos/aimeos-typo3)

This project allows to take the [Twitter Customer Support](https://www.kaggle.com/thoughtvector/customer-support-on-twitter) and format it in the [Persona Chat](https://arxiv.org/pdf/1801.07243.pdf) format. This is helpful to adapt the model described in this [paper](https://arxiv.org/abs/1901.08149) into an task oriented version.


### Table of content

- [Getting Started](#getting_started)
- [Usage](#usage)
- [Contribute](#contribute)
    - [Contributors](#contributors)
- [Show you Support](#support)
- [License](#license)



<a name="getting_started"> 

## 🚀 Getting Started

</a>

#### 0 - Download the project

Click [here](https://github.com/HLT-MAIA/twcs2PersonaChat/archive/main.zip) and extract the zip to your preferred dirctory.

#### 1 - Install pipenv

The first step is to install pipenv. Go to the project directory and run:
On mac:
You can use homebrew:
```
brew install pipenv
```
or pip:
```
pip install pipenv
```
On Linux:
```
sudo apt install software-properties-common python-software-properties
sudo add-apt-repository ppa:pypa/ppa
sudo apt update
sudo apt install pipenv
```

#### 2 - Install project requirements

On the project directory run:
```
pip install -r requirements.txt
```

#### 3 - Run the project
To run the project:
```
python cli.py [module_name] [options]
```

<a name="usage"> 

## 👩‍💻 Usage

</a>
This project includes 3 modules: **getMetadata**, **preprocess**, and **personify**.

#### getMetadata
This module allows you to retrieve some metadata about the [Twitter Customer Support](https://www.kaggle.com/thoughtvector/customer-support-on-twitter) to use it run:

```
python cli.py getMetadata
```

#### preprocess

This module allows you to preprocess the [Twitter Customer Support](https://www.kaggle.com/thoughtvector/customer-support-on-twitter). Here are the options you can use:

- --emojis: Boolean, if True, removes all emojis from the dataset (default: True)
- --emoticons: Boolean, if True, removes all emoticons from the dataset (default: True)
- --urls: Boolean, if True, tags urls as '(URL)' from the dataset (default: True)
- --html_tags: Boolean, if True, removes all html tags (default: True)
- --acronyms: Boolean, if True, converts acronyms to their meaning. E.g.: SMH -> So much Hate (default: True)
- --spelling: Boolean, if True, spellchecks the dataset (default: False)
- --usernames: Boolean, if True, tags usernames (default: False)

To run:

```
python cli.py preprocess [options]
```

#### personify

This modules allows you to format the (preprocessed or not) dataset. The options are:

- --brand: String, represents the name of a brand, only uses the interactions with a specific brand. If none, uses the whole dataset (default: None)
- --limit: Integer, only uses a limited amount of conversations. If -1 uses the whole dataset (default: -1)


<a name="contribute"> 

## 🤝 Contribute 

</a>

If you have any ideas, just open an [issue](https://github.com/gonmelo/leek/issues) and tell us what you think!

If you'd like to contribute, please fork the repository and make changes as you'd like. Pull requests are warmly welcome.


<a name="contributors"> 
  
## Contributors

</a>

<a href="https://github.com/gonmelo">
	<img src="https://github.com/gonmelo.png" width="80" style="border-radius:50%">
</a>


<a name="support"> 
  
## Show your support 

</a>
:star: Star us on GitHub — it helps!

<a name="license"> 
  
## License

</a>


This project is [MIT](https://github.com/gonmelo/leek/blob/master/LICENSE) licensed.
