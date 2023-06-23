import schemaser
import json
import enum

Vector = tuple[float, float, float]

class Choose(enum.Enum):
    FIRST_ITEM='first_item'
    SECOND_ITEM='second_item'
    THIRD_ITEM='third_item'

class ResourcePath:
    def __init__(self, module_type:str, node_name:str):
        """
        Describes a resrouce path used for annotations.

        Arguments
        ---
        `module_type` - The node type that it should except.

        `node_name` - The node name that is should except.

        Methods
        ---
        exists
        """
        self.module_type = module_type
        self.node_name = node_name

    # TODO
    def exists(self) -> bool:
        """
        Checks if this resource path exists
        """
        raise NotImplementedError()
    

class cls:
    """cls desc"""
    def __init__(self, string:str=None, integer:int=None, float:float=None):
        pass

    # Create custom schemas for classes by using the __schema__ magic method.
    # def __schema__(self):
    #     return {}

def func2(value:str, **kw:cls):
    """func2 desc"""
    pass

# **kw "additionalProperties": true
def func1(enum: Choose, path:ResourcePath, bytes:bytes, string:str, integer:int, float:float, vec:Vector, tuple:list[str,int], array:list[str|int], both:str|cls, object:cls, func:func2):
    pass

dat = schemaser.to_schema(func1)
print(dat)

with open('schema.json', 'w') as w:
    w.write(json.dumps(dat, indent=4))