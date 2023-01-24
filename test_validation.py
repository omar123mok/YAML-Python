import yaml
import pytest


# pip install pyyaml

def test_func1():
    with open("data.yaml", 'r') as x:
        data = yaml.safe_load(x)
    for item in data:
        assert 'First Name' in item, f'Missing key: First Name in {item}'
        assert 'Last Name' in item, f'Missing key: Last Name in {item}'
        assert 'Gender' in item, f'Missing key: Gender in {item}'
        assert 'Tags' in item, f'Missing key: Tags in {item}'
        assert item['First Name'], f'Missing value for key: First Name in {item}'
        assert item['Last Name'], f'Missing value for key: Last Name in {item}'
        assert item['Gender'], f'Missing value for key: Gender in {item}'
        assert item['Tags'], f'Missing value for key: Tags in {item}'
