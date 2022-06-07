

from matplotlib import image
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

testimg =image.imread('media/test/1654582290.952967.jpg')
print(testimg)
plt.imshow(testimg)
plt.show()
