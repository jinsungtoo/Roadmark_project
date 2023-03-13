# Roadmark_project

기간 : 2023.2.6 - 2023.3.3


## 1. 데이터셋 다운로드
Aihub 데이터 사용 : https://aihub.or.kr/aihubdata/data/view.docurrMenu=116&topMenu=100&aihubDataSe=ty&dataSetSn=654


## 2. 데이터셋 폴더 재구성
총 3차에 걸쳐 진행 
- 라벨 정리 및 삭제
## 3. 데이터 전처리

## 4. Bbox 가이드라인 설정
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


yolov5m 모델 학습하여 1epoch당 5-6분 소요

## 8. 테스트용 인퍼런스 결과 확인

## 9. Confusion matrix 모델별 비교

## 10. tensorrt 적용

## 11. 3차 라벨링 진행 후 학습 진행

## 12. 차선 인식 

## 13. 알림 메시지 서비스 구현
GUI 내 bbox 안에 신호가 감지될 시 텍스트로 띄우도록 구현
