#!/usr/bin/python3
""" 14-main """
from models.base import Base
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    dictionary = r1.to_dictionary()
    #json_dictionary = Base.to_json_string([dictionary])
    j = Base.to_json_string([{'y': 3, 'id': 1, 'x': 53, 'height': 39, 'width': 89}, {'size': 13, 'id': 2, 'x': 99, 'y': 19}, {'y': 99, 'id': 2, 'x': 99, 'height': 71, 'width': 17}, {'size': 13, 'id': 3, 'x': 81, 'y': 27}, {'y': 39, 'id': 3, 'x': 67, 'height': 17, 'width': 27}, {'size': 41, 'id': 4, 'x': 77, 'y': 83}, {'y': 21, 'id': 4, 'x': 49, 'height': 19, 'width': 39}, {'size': 19, 'id': 5, 'x': 61, 'y': 71}, {'y': 25, 'id': 5, 'x': 15, 'height': 93, 'width': 1}, {'size': 97, 'id': 6, 'x': 19, 'y': 43}, {'id': 20, 'name': '2454fee4-3a3f-4b4d-923d-a6ff745c36b4'}, {'id': 21, 'name': 'e262513a-b537-440a-ac08-4600ea4df5e6'}, {'id': 22, 'name': 'a4245a05-526e-4b18-8d8c-cda29a512414'}, {'id': 23, 'name': '6f5bb2fd-fc61-478e-a739-94bed72edd76'}, {'id': 24, 'name': '5c554f55-57f7-42e3-b00a-bbbe5b4215f5'}])
    print(dictionary)
    print(type(dictionary))
    print(j)
    print(type(j))
