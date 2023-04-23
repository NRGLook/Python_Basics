import re


class JSONSerializer:
    @staticmethod
    def dump(obj, fp):
        with open(fp, "w") as f:
            f.write(JSONSerializer.dumps(obj))

    @staticmethod
    def dumps(obj):
        if isinstance(obj, (int, float, bool)):
            return str(obj).lower()
        elif isinstance(obj, str):
            return f'"{obj}"'
        elif isinstance(obj, (list, tuple)):
            return f"[{','.join(map(JSONSerializer.dumps, obj))}]"
        elif isinstance(obj, dict):
            return f"{{{','.join([f'\"{k}\":{JSONSerializer.dumps(v)}' for k,v in obj.items()])}}}"
        elif obj is None:
            return "null"
        else:
            raise TypeError(f"Object of type '{obj.class.name}' is not JSON serializable")

    @staticmethod
    def load(fp):
        with open(fp, "r") as f:
            return JSONSerializer.loads(f.read())

    @staticmethod
    def loads(s):
        return eval(re.sub(r'"(.*?)":', r'\\\"\1\\\":', s))