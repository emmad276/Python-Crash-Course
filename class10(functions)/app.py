from typing import Tuple,Dict
def my_function(a:int, b:int, *abc:Tuple[int, ...], **xyz:Dict[str, int]):
    print(a,b,abc,xyz)

my_function(2,3,2,5,6,7,3,5,6,3,a1=23,b1=30,c1=46)