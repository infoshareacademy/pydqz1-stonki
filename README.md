# rapdator (Random Personal Data Generator)

This is a sipmle Python random personal data generator. It can deliver a fake, but realistic looking data from it's own database, such as: name, last name, adress, nickname, e-mail adress or whole personal data package, male and female versions. You can use those data in need to fill some form fields, when testing, for example. Data can be saved to a file. For now, you can have data only in Polish.

## Usage

```python
from rapdator import Rapdator 

r = Rapdator()

r.name_female()
"Olga"

r.last_name()
"Ptak"

r.email()
"ptak@wp.pl"

r.nick()
"pbnsth76"

r.adress()
"Wiejska 15" 
"80-509" 
"Gdańsk"

r.person_female()
"Olga" 
"Ptak"
"ptak@wp.pl"
"pbnsth76"
"Wiejska" 
"15" 
"80-509" 
"Gdańsk"
```

OR
```python
r.name_male()
"Olgierd"

r.last_name()
"Stępień"

r.email()
"stepien@wp.pl"

r.nick()
"pedhrl94"

r.adress()
"Morska"
"22/5"
"80-412" 
"Gdańsk"

r.person_male()
"Olgierd"
"Stępień"
"stepien@wp.pl"
"pedhrl94"
"Morska" 
"22/5"
"80-412" 
"Gdańsk"
```
OR
```python
from rapdator import Rapdator
r = Rapdator()
for i in range(2):
        r.person_female()

"Olga" 
"Ptak"
"ptak@wp.pl"
"pbnsth76"
"Wiejska" 
"15" 
"80-509" 
"Gdańsk"
"Barbara" 
"Kos"
"kos@wp.pl"
"plenst52"
"Niska"
"4A" 
"80-509" 
"Gdańsk"
```

## Installation

pip:

pip install rapdator
source:

git clone git@github.com:infoshareacademy/pydqz1-stonki.git
cd rapdator
python setup.py install


## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/....) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We don't use any versioning, yet ;) 

## Authors

* **Magda Borkowska** - [magdaborkowska](https://github.com/magdaborkowska)
* **Paweł Sobieraj** - 
* **Konrad Linka** -

See also the list of [contributors](https://github.com/infoshareacademy/pydqz1-stonki/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Thanks to iSA trainers for help during development


