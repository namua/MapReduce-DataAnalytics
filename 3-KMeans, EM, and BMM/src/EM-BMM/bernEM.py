'''
BernEM.py

This is an implementation of EM algorithm on binary dataset
with Bernoulli likelihood. 
'''

import numpy as np
from scipy import stats

SEED = 483982
PRNG = np.random.RandomState(SEED)

## NUMBER OF CLUSTERS ##
K = 10
N = 60000
D = 784
####

observations = np.zeros((N,D))

fname = 'bin_train.txt'

def generateSample(N, D, pi, mu):
	'''
	sample = np.ndarray([N, D])
	for ii in range(0, N):
		zn = np.random.multinomial(1, pi, size=1)[0]
		ind = _indices(zn, lambda x: x==1)[0]
		sample[ii, :] = np.random.binomial(1, mu[ind])	
	return sample
	'''
	

def _indices(a, func):
	return [i for (i, val) in enumerate(a) if func(val)]

def em(observations, cont_tol, iterations):
	[N, D] = observations.shape
	iteration = 1
	delta_change = 9999

	# Init Model
	pi = np.random.rand(K)
	#mu = [[.5, .5, .5, .5], [.9, .1, .1, .9]]
	mu = np.random.rand(K, D)
	r = np.zeros([N, K]) # soft assignment
	weight = np.zeros(K)

	# Main loop
	while iteration <= iterations:
		# E step
		print('Iter:',iteration)
		which_e = 0
		for ii in range(0, N):
			observation = observations[ii]
			for kk in range(0, K):
				weight[kk] = pi[kk]
				for jj in range(0, D):
					weight[kk] *= mu[kk][jj]**int(observation[jj]) * (1-mu[kk][jj])**(1-int(observation[jj]))
					which_e +=1
					if(which_e % 78600000 == 0):
						print('E Step:'+ str(int(which_e /78600000)) +'/6')
			if(sum(weight) != 0):
				r[ii, :] = weight / sum(weight)

		# M step
		nk = [sum(r[:, ii]) for ii in range(K)]

		new_mu = np.zeros([K, D])
		which_m = 0
		for kk in range(0, K):
			mean = np.zeros(D)
			for ii in range(0, N):
				mean += r[ii, kk]*int(observations[ii])
				which_m +=1
				if(which_m % 78600000 == 0):
						print('E Step:'+ str(int(which_m /78600000)) +'/6')
			new_mu[kk] = mean / nk[kk]
		pi = nk / sum(nk) 

		delta_change = sum(sum(abs(new_mu-mu)))
		print('Error:',delta_change)
		if delta_change < cont_tol:
			break
		else:
			mu = new_mu
			iteration += 1

	return [mu, pi, iteration]


def main():
	num_feat = 784
	num_sample = 600000
	cont_tol = 1e-4
	max_iter = 100

	# GLOBAL PARAMS
	pi = [.2, .8] # probablity of each cluster
	mu = [[.5, .5, .5, .5], [.9, .9, .1, .1]] # probabilities of 1 for each cluster

	# Generate observations
	# observations = generateSample(num_sample, num_feat, pi, mu)
	which_line = 0
	with open(fname) as f:
		lines = [line.rstrip('\n') for line in open(fname)]
		for line in lines:
			line = line.strip()
			header, line = line.split(':')
			header, digit = header.split()
			pixels = line.split()
			observations[int(digit)] = pixels
			which_line += 1
			if(which_line % 1000 == 0):
				print(which_line)

	# Run EM
	[mu_est, pi_est, iterations] = em(observations, cont_tol, max_iter)

	# dataset = MNIST()
	# dataset.load_training()
	# train = dataset.train_images
	# train_labels = dataset.train_labels
	# train = train[0:100]
	# train_labels = train_labels[0:100]
	
	# train = np.array(train)
	# for ii in range(len(train)):
	# 	train[ii] = dataset.conv2binary(train[ii])

	# [mu_est, pi_est, iterations] = em(train, cont_tol, max_iter)

	print 'mu', mu_est
	print 'pi', pi_est
	print 'iter', iterations


if __name__ == '__main__':
	import time
	start_time = time.time()
	main()
	end_time = time.time()
	print("Elapsed time was %g seconds" % (end_time - start_time))





