from typing import List, Union, Tuple, Dict

# List of integers
numbers: List[int] = [1,2,3,4]       

#Tuple of a string and an integrer
person : Tuple[str, int] = ("Alice", 30)

# Dictionary with string keys and integer values
scores: Dict[str, int] = {"Alice": 90}

# union type for variables that can hold multiple types
identifier: Union[int, str] = "ID123"
