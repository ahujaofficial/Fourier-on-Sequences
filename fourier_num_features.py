from scipy.fftpack import fft,ifft,fftshift,ifftshift
import numpy as np
import pandas
import matplotlib.pyplot as plt

array_size = 187
df = pandas.read_csv('mock_kaggle_edit_validate.csv')
arr_sales = np.zeros(array_size)
for i in range(array_size):
	arr_sales[i] = df['sales'][i]

def reconstruct(arr,vals =1):
	fft1=fft(arr)
	fft1_s = fftshift(fft1)
	fft1_s[:vals]=0
	fft1_s[-vals:]=0
	ifft1 = ifft(ifftshift(fft1_s))
	return ifft1.real


l2_distances = []
for window in range(5,array_size):
	l2_dis = 0
	for i in range(array_size-window+1):
		reconstructed_array = reconstruct(arr_sales[i:i+window])
		l2_dis += np.linalg.norm(reconstructed_array - arr_sales[i:i+window])
	l2_distances.append(l2_dis/((array_size-window+1)*window))
	if window%100 ==0:
		print(window+1 , " windows done")
		
x = np.arange(5,array_size)
#print(len(l2_distances),l2_distances[:10],l2_distances[-10:])
plt.plot(x,l2_distances)#,'bo',markersize=1)
plt.show()
