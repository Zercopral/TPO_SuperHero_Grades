import pytest
import filecmp

# def get_list(value):
#     tmp = [[""]*2]*len(value)
#     print(tmp)
#     for index, elem in enumerate(value):
#         #for j in range():
#         tmp[index][index%2] = elem
#         tmp[index+1][1] = elem
#         print(tmp)
#     return tmp

# print(get_list(["File1", "File2"]))
# get_list(["files/SuperHero.json","files/SuoerHero_plus_2.json","files/superhero_plus_2_sorted.json"])

@pytest.mark.parametrize("file1, file2", [("files/SuperHero.json","files/SuoerHero_plus_2.json"),("files/SuoerHero_plus_2.json","files/superhero_plus_2_sorted.json"),("files/superhero_plus_2_sorted.json", "files/SuperHero.json")])
def test_json(file1, file2):
    assert filecmp.cmp(file1, file2) == False