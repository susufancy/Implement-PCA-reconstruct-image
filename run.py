import numpy
from PIL import Image
reconMat = numpy.load('./data/mat/reconMat.npy')

reimg_1 = numpy.vsplit(reconMat,5)[0]
reimg_2 = numpy.vsplit(reconMat,5)[1]
reimg_3 = numpy.vsplit(reconMat,5)[2]
reimg_4 = numpy.vsplit(reconMat,5)[3]
reimg_5 = numpy.vsplit(reconMat,5)[4]



trans_img1 = numpy.reshape(reimg_1,(32,32,3))
reimg_1 = Image.fromarray((trans_img1 * 255).astype(numpy.uint8))
reimg_1.save('./data/img/recodifferent/01.png')

trans_img2 = numpy.reshape(reimg_2,(32,32,3))
reimg_2 = Image.fromarray((trans_img2 * 255).astype(numpy.uint8))
reimg_2.save('./data/img/recodifferent/02.png')

trans_img3 = numpy.reshape(reimg_3,(32,32,3))
reimg_3 = Image.fromarray((trans_img3 * 255).astype(numpy.uint8))
reimg_3.save('./data/img/recodifferent/03.png')

trans_img4 = numpy.reshape(reimg_4,(32,32,3))
reimg_4 = Image.fromarray((trans_img4 * 255).astype(numpy.uint8))
reimg_4.save('./data/img/recodifferent/04.png')

trans_img5 = numpy.reshape(reimg_5,(32,32,3))
reimg_5 = Image.fromarray((trans_img5 * 255).astype(numpy.uint8))
reimg_5.save('./data/img/recodifferent/05.png')
