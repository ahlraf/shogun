from shogun.Features import RealFeatures
from numpy import array, float64, all

# create dense matrices A,B,C
matrix=array([[1,2,3],[4,0,0],[0,0,0],[0,5,0],[0,0,6],[9,9,9]], dtype=float64)

parameter_list = [[matrix]]

# ... of type LongInt
def features_dense_real_modular(A=matrix):

# ... of type Real, LongInt and Byte
	a=RealFeatures(A)
	a.set_feature_vector(array([1,4,0,0,0,9], dtype=float64), 0)

# get matrix
	a_out = a.get_feature_matrix()

	b = array(a) + a

	print b
	print a_out

	assert(all(a_out==A))
	return a_out

if __name__=='__main__':
	print('dense_real')
	features_dense_real_modular(*parameter_list[0])
