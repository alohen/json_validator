import json
import json_data.dict as jdict
import json_data.string as jstring
import json_data.lists as jlist


def abvalidator(text):
    if text not in ["a", "b"]:
        raise ValueError("string not '{}' valid 'a' or 'b'".format(text))


schema = jdict.create_json_dict_parser(
    {
        "text": {
            "allowEmpty": True,
            "parser": jstring.create_json_string_parser(abvalidator)
        },
        "list": {
            "allowEmpty": False,
            "parser": jlist.create_json_list_parser(
                jstring.create_json_string_parser(abvalidator)
            )
        },
        "dict": {
            "allowEmpty": True,
            "parser": jdict.create_json_dict_parser(
                {
                    "a": {
                        "allowEmpty": True,
                        "parser": jstring.create_json_string_parser(abvalidator),
                    },
                    "b": {
                        "allowEmpty": True,
                        "parser": jstring.create_json_string_parser(abvalidator),
                    }
                }
            )
        }
    }
)
a = '{"text":"a", "list":["a","b"], "dict": {"a":"a","b":"b"}}'

unmarshalled = json.loads(a)

schema(unmarshalled)
