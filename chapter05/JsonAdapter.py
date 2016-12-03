#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json


class JsonAdapter(object):
    # jsonからシリアライズ
    def Serialize(self, argJsonData) :

        jsonData = argJsonData
        if isinstance(argJsonData, basestring ) :
            jsonData = json.loads(argJsonData)

        for key in self.__dict__.keys():
            if isinstance(getattr(self,key), JsonAdapter ) or getattr(self,key) == None :
                valclass = getattr(self,key)
                if valclass == None :
                    valclass = getattr(sys.modules["Classes.DataPDO"],key)()

                valclass.Serialize(jsonData[key])
                setattr(self,key, valclass)

            elif isinstance(getattr(self,key), int ) :
                setattr(self,key, int(jsonData[key]))
            else :
                setattr(self,key, jsonData[key])

    # Jsonを出力
    def ToJson(self):
        jsonDict = self.__ToDictionary()
        jsonstring = json.dumps(jsonDict, ensure_ascii=False)
        return jsonstring

    #Mapを作成
    def __ToDictionary(self):
        jsonDict = {}
        for key in self.__dict__.keys():
            if isinstance(getattr(self,key), JsonAdapter ) :
                jsonDict.update({key : getattr(self,key).__ToDictionary()})
            else :
                jsonDict.update({key : getattr(self,key)})
        return jsonDict

