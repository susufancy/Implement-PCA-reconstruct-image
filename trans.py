from PIL import Image
from pca import *
import numpy
# 加载图片
I_1 = Image.open('./data/img/different/01.png')
I_2 = Image.open('./data/img/different/02.png')
I_3 = Image.open('./data/img/different/03.png')
I_4 = Image.open('./data/img/different/04.png')
I_5 = Image.open('./data/img/different/05.png')


# 转换成numpy矩阵
img_1 = numpy.array(I_1).reshape(1,numpy.product(numpy.array(I_1).shape))
img_2 = numpy.array(I_2).reshape(1,numpy.product(numpy.array(I_2).shape))
img_3 = numpy.array(I_3).reshape(1,numpy.product(numpy.array(I_3).shape))
img_4 = numpy.array(I_4).reshape(1,numpy.product(numpy.array(I_4).shape))
img_5 = numpy.array(I_5).reshape(1,numpy.product(numpy.array(I_5).shape))


# print(img_1.shape)
# print(img_2.shape)
# print(img_3.shape)
# print(img_4.shape)
# print(img_5.shape)

cat_dataset = numpy.vstack((img_1,img_2,img_3,img_4,img_5))
# print(cat_dataset.shape)

#print(dataMat)
lowDDataMat, reconMat = pca(cat_dataset, 500)
numpy.save(file="./data/mat/lowDDataMat.npy", arr=lowDDataMat)
numpy.save(file="./data/mat/reconMat.npy", arr=reconMat)
print(lowDDataMat.shape)
print(reconMat.shape)



# reimg_1 = numpy.vsplit(reconMat,5)[0]
# print(reimg_1.shape)


# trans_img1 = numpy.reshape(reimg_1,numpy.array(I_1).shape)
# print(trans_img1.shape)
# reimg_1 = Image.fromarray(trans_img1).convert('RGB')
# reimg_1.save('./data/reconimg/01.png')