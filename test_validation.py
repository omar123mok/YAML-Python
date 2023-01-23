import yaml
import pytest


# pip install pyyaml
def func1(data):
    ''' Tests for the format of code'''
    for item in data:
        print(item)
        assert 'kkkk Name' in item, f'Missing key: First Name in {item}'
        assert 'Last Name' in item, f'Missing key: Last Name in {item}'
        assert 'Gender' in item, f'Missing key: Gender in {item}'
        assert 'Tags' in item, f'Missing key: Tags in {item}'
        assert item['First Name'], f'Missing value for key: First Name in {item}'
        assert item['Last Name'], f'Missing value for key: Last Name in {item}'
        assert item['Gender'], f'Missing value for key: Gender in {item}'
        assert item['Tags'], f'Missing value for key: Tags in {item}'


def test_01():
    ''' Reads the data.yaml file'''
    with open("data.yaml", 'r') as x:
        data = x
    with pytest.raises(Exception) as exc:
        data = yaml.safe_load(x)

    with pytest.raises(Exception) as exc:
        func1(data)
    print(str(exc.value))
    # assert (str(exc.value)) == "Value Error at func1"
    
test_01()
