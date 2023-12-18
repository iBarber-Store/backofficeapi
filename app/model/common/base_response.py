from typing import Any

class BaseResponse:
    code: int
    msg: str
    data: Any

    def __init__(self, code: int, msg: str, data: Any = None) -> None:
        self.code = code
        self.msg = msg
        self.data = data

    @staticmethod
    def from_dict(obj: Any) -> 'BaseResponse':
        assert isinstance(obj, dict)
        code = int(obj.get("code"))
        msg = str(obj.get("msg"))
        data = obj.get("data")
        return BaseResponse(code, msg, data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["code"] = int(self.code)
        result["msg"] = str(self.msg)
        result["data"] = self.data
        return result
