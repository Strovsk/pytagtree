import re
import os

def getContentModel(testId):
    path = os.path.abspath(f'./helpers/model.txt')
    file = open(path, 'r')
    data = file.read()
    file.close()
    tagstestlist = re.findall(r'\[(.*?)\]', data, re.DOTALL | re.MULTILINE)
    return ({
        "emptyTag": tagstestlist[0],
        "emptyTagSlash": tagstestlist[1],
        "paramTag": tagstestlist[2],
        "paramTagSlash": tagstestlist[3],
        "paramValueTag": tagstestlist[4],
        "paramValueTagSlash": tagstestlist[5],
        "paramsTag": tagstestlist[6],
        "paramsTagSlash": tagstestlist[7],
        "paramsTagId": tagstestlist[8],
        "paramsTagIdSlash": tagstestlist[9],
        "params2TagId": tagstestlist[10],
        "params2TagIdSlash": tagstestlist[11],
        "emptyTagBreak": tagstestlist[12],
        "emptyTagBreakSlash": tagstestlist[13],
        "valueParamTagBreak": tagstestlist[14],
        "valueParamTagBreakSlash": tagstestlist[15],
        "paramsTagBreak": tagstestlist[16],
        "paramsTagBreakSlash": tagstestlist[17],
        "paramsTagBreakId": tagstestlist[18],
        "paramsTagBreakIdSlash": tagstestlist[19],
        "params2TagBreakId": tagstestlist[20],
        "params2TagBreakIdSlash": tagstestlist[21],
        "emptyTagValue": tagstestlist[22],
        "emptyTagBreakValue": tagstestlist[23],
        "paramTagValue": tagstestlist[24],
        "paramTagBreakValue": tagstestlist[25],
        "paramsTagValue": tagstestlist[26],
        "paramsTagBreakValue": tagstestlist[27]
    })[testId]
