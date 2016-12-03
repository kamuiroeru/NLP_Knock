#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json


class JsonAdapter(object):
    # jsonからシリアライズ
    def serialize(self, arg_json_data):

        json_data = arg_json_data
        if isinstance(arg_json_data, str):
            json_data = json.loads(arg_json_data)

        for key in self.__dict__.keys():
            if isinstance(getattr(self, key), JsonAdapter) or not getattr(self, key):
                val_class = getattr(self, key)
                if not val_class:
                    val_class = getattr(sys.modules["Classes.DataPDO"], key)()

                val_class.serialize(json_data[key])
                setattr(self, key, val_class)

            elif isinstance(getattr(self, key), int):
                setattr(self, key, int(json_data[key]))
            else:
                setattr(self, key, json_data[key])

    # Jsonを出力
    def to_json(self):
        json_dict = self.to_dictionary()
        json_string = json.dumps(json_dict, ensure_ascii=False)
        return json_string

    # Mapを作成
    def to_dictionary(self):
        json_dict = {}
        for key in self.__dict__.keys():
            if isinstance(getattr(self, key), JsonAdapter):
                json_dict.update({key: getattr(self, key).to_dictionary()})
            else:
                json_dict.update({key: getattr(self, key)})
        return json_dict
