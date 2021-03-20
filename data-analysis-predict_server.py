# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import xgboost as xgb

from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sklearn.preprocessing import LabelEncoder

app = FastAPI()

origins = [
    "http://123.56.163.105"
    "http://123.56.163.105:8080"
    "http://47.103.203.133"
    "http://47.103.203.133:8080"
    "http://localhost",
    "http://localhost:8080",
]

# 设置允许跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class BodyIndex(BaseModel):
    creator = ""
    age: int = None
    sex = ""
    nation = ""
    weight = ""
    height = ""
    weightIndex = ""
    obesityWaistline = ""
    waistline = ""
    maxBloodPressure = ""
    minBloodPressure = ""
    goodCholesterol = ""
    batCholesterol = ""
    totalCholesterol = ""
    Dyslipidemia = ""
    pvd = ""
    sportActivities = ""
    education = ""
    marry = ""
    income = ""
    sourceCase = ""
    visionBad = ""
    drink = ""
    highBloodPressure = ""
    familialHighBloodPressure = ""
    diabetes = ""
    familialDiabetes = ""
    hepatitis = ""
    familialHepatitis = ""
    chronicFatigue = ""
    alf = ""

def last_pre(js):
    print(js)
    data = pd.DataFrame(js)
    data.rename(columns={
      'age':'年龄',
      "sex": "性别",
      "nation": "区域",
      "weight": "体重",
      "height": "身高",
      "weightIndex": "体重指数",
      "obesityWaistline": "肥胖腰围",
      "waistline": "腰围",
      "maxBloodPressure": "最高血压",
      "minBloodPressure": "最低血压",
      "goodCholesterol": "好胆固醇",
      "batCholesterol": "坏胆固醇",
      "totalCholesterol": "总胆固醇",
      "Dyslipidemia": "血脂异常",
      "pvd": "PVD",
      "sportActivities": "体育活动",
      "education": "教育",
      "marry": "未婚",
      "income": "收入",
      "sourceCase": "护理来源",
      "visionBad": "视力不佳",
      "drink": "饮酒",
      "highBloodPressure": "高血压",
      "familialHighBloodPressure": "家庭高血压",
      "diabetes": "糖尿病",
      "familialDiabetes": "家族糖尿病",
      "familialHepatitis": "家族肝炎",
      "chronicFatigue": "慢性疲劳",
      "alf":"ALF"}, inplace = True)
    # from sklearn.externals import joblib
    import joblib
    model_new = joblib.load('./model.pkl')
    from sklearn.preprocessing import LabelEncoder
    
    le = LabelEncoder()
    for i in ['性别','区域','护理来源','区域']:
        trans = le.fit(data[i])
        data[i] = trans.transform(data[i])
    data.drop(['教育','未婚','护理来源','视力不佳','家族肝炎','收入','creator',"hepatitis"],axis=1,inplace=True)
    def change_type(df):
        for col in df.columns:
            col_type = df[col].dtype
        
            if col_type == object:
                df[col] = df[col].apply(lambda x : float(x) if str(x) != 'nan' else x)

        return df

    data = change_type(data)
    feats = [f for f in data.columns if f not in ['肝炎']]
    data_p = xgb.DMatrix(data[feats])
    pre = model_new.predict(data_p)
    
    return pre

# js = {
#     "creator": "cosmos1f8a9m5s98gedkslrr0l7t7mzdc5sfq9d39e566",
#     "age": 30,
#     "sex": "M",
#     "nation": "east",
#     "weight": "71.8",
#     "height": "163.3",
#     "weightIndex": "26.92",
#     "obesityWaistline": "0",
#     "waistline": "94.6",
#     "maxBloodPressure": "101",
#     "minBloodPressure": "45",
#     "goodCholesterol": "83",
#     "batCholesterol": "139",
#     "totalCholesterol": "222",
#     "Dyslipidemia": "0",
#     "pvd": "0",
#     "sportActivities": "3",
#     "education": "1",
#     "marry": 0,
#     "income": "",
#     "sourceCase": "Private Hospital",
#     "visionBad": "0",
#     "drink": "0",
#     "highBloodPressure": "1",
#     "familialHighBloodPressure": "1",
#     "diabetes": "0",
#     "familialDiabetes": "1",
#     "hepatitis": "1",
#     "familialHepatitis": "0",
#     "chronicFatigue": "1",
#     "alf":"0"
#   }

# if __name__ == '__main__':
#     print(last_pre(js))

@app.post('/predict')
def predict(request_data: BodyIndex):
    # TODO：预测
    if(request_data.sex == "0"):
        request_data.sex = "F"
    if(request_data.sex == "1"):
        request_data.sex = "M"
    dictBodyIndex = request_data.__dict__
    res = last_pre([dictBodyIndex])
    possibility = str(round(float(res[0]*100))) + "%"
    return {"possibility":possibility}
     
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app=app,
                host="0.0.0.0",
                port=8888,
                workers=1)
















