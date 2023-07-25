import uuid
import json
from pytest import Item
from inspect import getsource


class TestItem:
    def __init__(self, item: Item):
        self.uid = uuid.uuid4()
        self.id: int = None
        self.title = _clear_param_brackets(item.name)
        self.file_name = item.path.name
        self.abs_path = str(item.path)
        self.file_path = item.location[0]
        self.module = item.module.__name__
        self.source_code: str = None
        # straitforward way, does not work with test packages
        # self.source_code = getsource(item.function)
        self.class_name = item.cls.__name__ if item.cls else None

    def to_dict(self) -> dict:
        result = dict()
        result['uid'] = str(self.uid)
        result['id'] = self.id
        result['title'] = self.title
        result['fileName'] = self.file_name
        result['absolutePath'] = self.abs_path
        result['filePath'] = self.file_path
        result['module'] = self.module
        result['className'] = self.class_name
        result['sourceCode'] = self.source_code
        return result

    def json(self) -> str:
        return json.dumps(self.to_dict(), indent=4)


def _clear_param_brackets(name: str) -> str:
    point = name.find('[')
    if point > -1:
        return name[0:point]
    return name
