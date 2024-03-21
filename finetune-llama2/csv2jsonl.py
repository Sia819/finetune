# !pip install jsonlines
import json

def csv2json(csv_file_path, json_file_path):
    # CSV파일을 DataFrame으로 읽기
    # JSON 파일로 저장
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        # 각 행을 JSON으로 변환하여 바로 파일에 쓰기
        for index, row in df.iterrows():
            data = {'inputs': row['inputs'], 'response':row['response']}
            json.dump(data, json_file, ensure_ascii=False, indent=4)
            json_file.write('\n')
            
# CSV 파일 경로와 JSON 파일 경로 설정
csv_file_path = dataPath + datasetName
json_file_path = dataPath = jsonFileName

# 함수 호출
csv2json(csv_file_path, json_file_path)