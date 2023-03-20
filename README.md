# Roadmark_project

기간 : 2023.2.6 - 2023.3.3


## 1. 데이터셋 다운로드
Aihub "감성 대화 말뭉치" 데이터 사용


https://aihub.or.kr/aihubdata/data/view.docurrMenu=116&topMenu=100&aihubDataSe=ty&dataSetSn=654

## 2. 목적
아직까지도 도로 위 사건사고는 끊임없이 발생하고 있다. 이를 조금이라도 방지하고자 본 프로젝트에서는 주행 영상 데이터를 이용하여 로드마크를 인식하고 문제가 발생했을 시 경고나 알림음을 활용하여 운전에 대한 경각심을 일으킨다. 이 프로젝트를 통해서 운전 규칙을 준수하고 더 나은 교통관리에 도움이 되도록 한다

## 3. 데이터셋 폴더 재구성
총 3차에 걸쳐 진행 
- 라벨 정리 및 삭제
![image](https://user-images.githubusercontent.com/115756142/226233612-e329f11e-d029-4284-b05b-867028f49e2b.png)


## 4. Bbox 가이드라인 설정
![image](https://user-images.githubusercontent.com/115756142/226249749-6f4f536d-f28d-4fcc-a2ef-b57b39e8ad42.png)
![image](https://user-images.githubusercontent.com/115756142/226249870-1c6bf9c0-c173-4b2f-b8ed-832279713be3.png)

1. 비보호 좌회전은 비보호만 바운딩 박스
2. 어린이/노인/장애인 보호구역은 보호구역만 바운딩 박스
3. 횡단보도, 과속방지턱은 각 차선마다 따로 바운딩 박스
4. 운전자와 같은 방향의 도로 표시만 라벨링. (역주행 차선 x)
5. 바운딩 박스로 표시하기 어려운 차선류 제외
6. 라벨링 편의성을 위하여 금지 화살표, 비보호 제외한 모든 화살표는 제외
7. 운전자 차선과 같은 방향의 차선의 도로 표시만 라벨링
8. 속도제한은 20부터 10 간격으로 100까지 구분

## 5. 이미지 cvat 검수
참고 사이트 : https://www.cvat.ai/


가이드라인을 바탕으로 일일이 bbox 설정

## 6. 1차, 2차 라벨링 진행
1차 라벨링 결과 : 다른 라벨에 비해 데이터 개수가 현저히 적은 라벨 삭제


2차 라벨링 결과 : 라벨별 편차가 큰 것을 확인

## 7. Yolov5 모델 학습
오피셜 yolov5 github 참고



yolov5m 모델 학습하여 1epoch당 5-6분 소요(총 100 epoch)


## 8. 테스트용 인퍼런스 결과 확인

학습 모델 : yolov5m
이미지 사이즈 : 640
옵티마이저 : Adam
배치 사이즈 : 45
사용 메모리 : 15.5G


## 9. Confusion matrix 모델별 비교
[yolo5s]
![image](https://user-images.githubusercontent.com/115756142/226250378-dcb5a455-80c1-4e5a-a4c8-74a8e9bf7242.png)


[yolov5m]
![image](https://user-images.githubusercontent.com/115756142/226250501-349447a6-71c2-4d5c-b4b8-62b764a66d56.png)


[yolov5l]
![image](https://user-images.githubusercontent.com/115756142/226250556-94d34b52-d681-44e9-b013-424948799dcd.png)


[yolov5x]
![image](https://user-images.githubusercontent.com/115756142/226250612-02de8bd5-c686-4006-bdd0-6f6f5f2114de.png)
## 10. tensorrt 적용

## 11. 3차 라벨링 진행 후 학습 진행
1) 서행, 속도제한20 등 이미지 수가 적은 라벨은 아예 삭제. (21종류 라벨 -> 18종류 라벨)


2) 전체적으로 모든 라벨 이미지 수를 늘려 좀 더 많은 양을 학습할 수 있도록 함


## 12. 차선 인식 
차선 인식 대신, bbox를 설정하여 그 안에 신호가 들어오게 되면 서비스 하는 방식으로 결정
![image](https://user-images.githubusercontent.com/115756142/226253852-b2f0b377-5fc4-4e1e-aa2c-ba8654fa0917.png)

## 13. 알림 메시지 서비스 구현
GUI 내 bbox 안에 신호가 감지될 시 텍스트로 띄우도록 구현
![test](https://user-images.githubusercontent.com/115756142/226246444-bb467a0d-c9ae-4393-918f-9d4126bd1a99.gif)



## 14. 진행 중 이슈사항
1) CVAT 작업 시 이미지 업로드 양이 많고 사이즈가 커서 한번에 안올라가는 오류가 발생-> task를 여러개로 나눠 진행


2) CVAT 사이트 자체가 느리고 무거워 한번씩 팅기는 현상이 발생


3) GUI pt 파일 재생 시 멈추는 현상 발생


4) GUI에서 프레임이 너무 낮게 나와서 속도 체크를 우선 진행 -> 파이토치 버전을 업그레이드 하여 프레임 속도 해결 (15 FPS -> 30 FPS)


5) GUI 프레임을 더 높이기 위해 tensorrt를 알아보는 중
