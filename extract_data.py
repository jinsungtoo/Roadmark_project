import os
import glob
import random

'''
폴더 구조
park_dataset
    - train (각 라벨당 1033장을 랜덤 추출)
        - image
            - 각 라벨 폴더 >> 나중에 puttext로 불법/정상 표시할때는 따로 조건문 걸어서 표시하는걸로...
        - label
            - 각 라벨별 ann파일
    - valid (각 라벨당 133장을 랜덤 추출)
    - test (각 라벨당 133장을 랜덤 추출)
'''

# 1. A드라이브에 추출 폴더 생성
os.makedirs('A:/load_test4/label/', exist_ok=True)

# 2. 원본 train 데이터에서만 추출, 원본 train root 저장
image_root = 'A:/new_load_data/image/'

# train, valid, test 데이터 추출, 각 라벨별 폴더 생성 및 복사
def extract_img():
    # 폴더 생성
    os.makedirs('A:/load_test4/image/', exist_ok=True)
    # 각 라벨별 폴더 이미지 접근
    img_path = glob.glob(os.path.join(image_root, '*.png'))
    # 중복없이 랜덤으로 1033개 추출
    img_samples = random.sample(img_path, 2000)
    # 이동할 디렉토리
    save_dir = 'A:/load_test4/image/'
    for img in img_samples:
        filename = os.path.basename(img)
        os.rename(img, save_dir+filename)
    print(' Done!!')

def get_filename(path_list):
    filename = []
    for path in path_list:
        file = path.split('\\')[-1]
        file = os.path.splitext(file)[0]
        filename.append(file)
    return filename

def extract_json(imgs_path, anns_path):
    # 각 라벨별 img 파일명 추출
    img_path = glob.glob(os.path.join(imgs_path, '*.png'))
    ann_path = glob.glob(os.path.join(anns_path, '*.json'))
    # 2. 파일명만 추출하여 list로 반환
    img_filename = get_filename(img_path)
    ann_filename = get_filename(ann_path)
    # 3. set타입을 이용해 교집합을 구하고 파일명을 list화
    intersection = list(set(img_filename) & set(ann_filename))
    # json 이동
    # 이동할 디렉토리
    save_dir = 'A:/load_test4/label/'
    for file in intersection:
        filename = file+'.json'
        path = f'{anns_path}{file}.json'
        os.rename(path, save_dir + filename)

def move_file(old, new):
    file_path = glob.glob(os.path.join(old,'*'))
    for path in file_path:
        filename = os.path.basename(path)
        os.rename(path, new+filename)

if __name__=='__main__':
    extract_img()
    extract_json('A:/load_test4/image/','A:/new_load_data/label/')




