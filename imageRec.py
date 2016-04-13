from PIL import Image
from pylab import *
import math
import operator
from sklearn import preprocessing
from functools import reduce
def cal_similar_by_path(img1,img2):
    (Gimage1,Gimage2) = open_regalur_image(img1,img2)
    (Bimage1,Bimage2) = open_regalur_image(img1,img2,'1')
    return image_contrast(Gimage1, Gimage2)* image_contrast(Bimage1, Bimage2)
#图像
def open_regalur_image(img1Path, img2Path,convertType='L'):
	img1 = Image.open(img1Path).convert(convertType)
	img2 = Image.open(img2Path).convert(convertType)
	minWidth = img1.size[0] if img1.size[0]<img2.size[0] else img2.size[0]
	minHeigh = img1.size[1] if img1.size[1]<img2.size[1] else img2.size[1]
	size = (minWidth,minHeigh)
	return img1.resize(size),img2.resize(size)
#矩阵归一化
def transform(data):
	data = array(data).astype(float).tolist()
	min_max_scaler = preprocessing.MinMaxScaler()
	return min_max_scaler.fit_transform(data)

def image_contrast(img1, img2):
    h1 = transform(img1.histogram())
    h2 = transform(img2.histogram())
    d1 = transform(reduce(lambda a,b:a+b,array(img1).tolist()))
    d2 = transform(reduce(lambda a,b:a+b,array(img2).tolist()))
    # 灰度直方图方差
    resultH = math.sqrt(reduce(operator.add,  list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1))
    # 灰度图像矩阵方差
    resultD = math.sqrt(reduce(operator.add,  list(map(lambda a,b: (a-b)**2, d1, d2)))/len(d1))
    resulHMax = resultH*1000
    resultDMax = resultD*100
    print(resulHMax,resultDMax)
    return resulHMax

if __name__ == '__main__':
    img1 = "test1.jpg"  # 指定图片路径
    img2 = "opencv1.jpg"
    result = cal_similar_by_path(img1,img2)
    print(result)
    