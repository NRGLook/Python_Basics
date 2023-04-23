import argparse
import os

from SerializeFactory import SerializerFactory


# Press the green button in the gutter to run the script.
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
        return eval(re.sub(r"<(.*?)>(.*?)</\1>", r'{"\\1":"\\2"}', s))


class SerializerFactory:
    @staticmethod
    def create_serializer(format_type):
        if format_type == "json":
            return JSONSerializer
        elif format_type == "xml":
            return XMLSerializer
        else:
            raise ValueError(f"Unsupported serializer format '{format_type}'")


if name == "main":
    parser = argparse.ArgumentParser(description="Serialize and deserialize Python objects in different formats")
    parser.add_argument("obj", type=str, help="The object to be serialized and deserialized")
    parser.add_argument("--format", type=str, default="json", help="The format to use for serialization")
    parser.add_argument("--outfile", type=str, help="The file to write the serialized object to")
    args = parser.parse_args()

    serializer_cls = SerializerFactory.create_serializer(args.format)
    obj = eval(args.obj)

    if args.outfile:
        serializer_cls.dump(obj, args.outfile)
        print(f"Object serialized to {os.path.abspath(args.outfile)}")
    else:
        serialized_obj = serializer_cls.dumps(obj)
        print(serialized_obj

