import toml
import json


class FilterModule(object):
    def filters(self):
        return {"to_toml": self.to_toml}

    def to_toml(self, input):
        return toml.dumps(json.loads(json.dumps(input)))
