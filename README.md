# Light-the-Spire

crwal_test.py : spirelogs.com의 데이터를 크롤링

data setup1.py : 크롤링해 얻은 데이터(20190201003826_1548999484.run.json)의 데이터를 전처리해 저장. 저장된 파일의 예시는 1.json과 같음

data setup2.py : 전처리된 데이터(1.json)의 파일을 불러와 학습에 쓰일 데이터(Jaw Worm_0.csv)로 저장

training_test.py : 학습 데이터를 불러와 AI를 학습. 학습한 뒤 모델을 저장하고, 불러오고, 체력 손실값을 예측할 수 있음
