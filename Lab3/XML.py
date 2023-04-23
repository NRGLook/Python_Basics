import re


class XMLSerializer:
    @staticmethod
    def dump(obj, fp):
        with open(fp, "w") as f:
            f.write(XMLSerializer.dumps(obj))

    @staticmethod
    def dumps(obj):
        if isinstance(obj, (int, float, bool)):
            return str(obj).lower()
        elif isinstance(obj, str):
            return f"<str>{obj}</str>"
        elif isinstance(obj, (list, tuple)):
            return f"<list>{''.join([XMLSerializer.dumps(item) for item in obj])}</list>"
        elif isinstance(obj, dict):
            return f"<dict>{''.join([f'<{k}>{XMLSerializer.dumps(v)}</{k}>' for k,v in obj.items()])}</dict>"
        elif obj is None:
            return "<null/>"
        else:
            raise TypeError(f"Object of type '{obj.class.name}' is not XML serializable")

    @staticmethod
    def load(fp):
        with open(fp, "r") as f:
            return XMLSerializer.loads(f.read())

    @staticmethod
    def loads(s):
        return eval(re.sub(r"<(.*?)>(.*?)</\1>", r'{"\1":"\2"}', s))