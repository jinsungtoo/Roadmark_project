import os
import glob
import json
import xml.etree.ElementTree as ET
from tqdm import tqdm

label_dict = {381: '중앙선', 382: '유턴구역선', 383: '차선', 384: '버스전용차로', 385: '길가장자리구역선', 386: '진로변경제한선506',
              387: '진로변경제한선507', 388: '진로변경제한선508', 389: '주차금지', 390: '정차주차금지516', 391: '정차주차금지5162',
              392: '유도선', 393: '좌회전유도차로', 394: '우회전금지', 395: '좌회전금지', 396: '직진금지', 397: '직진좌회전금지',
              398: '직진우회전금지', 399: '좌우회전금지', 400: '유턴금지', 401: '속도제한', 402: '속도제한어린이보호구역',
              403: '어린이보호구역', 404: '노인보호구역', 405: '장애인보호구역', 406: '유도526', 407: '회전교차로양보선표시',
              408: '유도527', 409: '유도528', 410: '횡단보도예고', 411: '정지선', 412: '횡단보도', 413: '고원식횡단보도',
              414: '자전거횡단보도', 415: '진행방향537', 416: '진행방향538', 417: '진행방향539', 418: '진행방향 및 방면540',
              419: '진행방향 및 방면541', 420: '비보호좌회전', 421: '차로변경', 422: '오르막경사면', 424: '서행519', 425: '서행520',
              426: '자전거전용도로', 427: '자전거우선도로', 428: '안전지대', 429: '일시정지', 430: '양보', 431: '주차',
              432: '정차금지지대', 433: '과속방지턱', 440: '노면색깔유도선'}

new_dict = {394: '우회전금지', 395: '좌회전금지', 396: '직진금지', 397: '직진좌회전금지', 398: '직진우회전금지', 399: '좌우회전금지',
            400: '유턴금지', 401: '속도제한', 402: '속도제한어린이보호구역', 403: '어린이보호구역', 404: '노인보호구역',
            405: '장애인보호구역', 410: '횡단보도예고', 412: '횡단보도', 413: '고원식횡단보도', 414: '자전거횡단보도',
            420: '비보호좌회전', 424: '서행519', 425: '서행520', 429: '일시정지', 430: '양보', 433: '과속방지턱'}

merge_dict = {394: '우회전금지', 395: '좌회전금지', 396: '직진금지', 397: '직진좌회전금지', 398: '직진우회전금지', 399: '좌우회전금지',
              400: '유턴금지', 403: '교통약자보호구역', 410: '횡단보도예고', 412: '횡단보도',
              420: '비보호좌회전', 424: '천천히', 425: '서행', 429: '일시정지', 430: '양보', 433: '과속방지턱',
              30: '속도제한30', 40: '속도제한40', 50: '속도제한50', 60: '속도제한60', 70: '속도제한70', 80: '속도제한80',
              90: '속도제한90'}

paths = glob.glob(os.path.join('A:/load_test4/label/','*.json'))

tree = ET.ElementTree()
root = ET.Element("annotations")

def label_merge(id):
    speed = [401, 402]
    safe_zone = [403, 404, 405]
    cross = [412, 413, 414]
    if id in speed:
        return 40
    elif id in safe_zone:
        return 403
    elif id in cross:
        return 412
    else:
        return id

for path in paths:

    with open(path, 'r', encoding="utf8") as file:
        data = json.load(file)
    image_meta = data['images'][0]
    w = image_meta['width']
    h = image_meta['height']
    image_name = image_meta["filename"]
    id = image_meta['id']
    xml_frame = ET.SubElement(root, "image", id=id, name=image_name,
                                width="%d" % w, height="%d" % h)
    bbox_meta = data['annotations']
    for anno in bbox_meta:
        try:
            x1, y1, w, h = anno['bbox']
            x2, y2 = x1 + w, y1 + h
            xtl = str(round(x1, 3))
            ytl = str(round(y1, 3))
            xbr = str(round(x2, 3))
            ybr = str(round(y2, 3))
            id = anno["category_id"]
            label_id = label_merge(id)
            labels = merge_dict[label_id]
            ET.SubElement(xml_frame, "box", label=labels, occluded="0", source="manual",
                          xtl=xtl, ytl=ytl, xbr=xbr, ybr=ybr, z_order="0")

        except:
            pass


tree._setroot(root)
tree.write(f"A:/load_test4/test4.xml", encoding="utf-8")