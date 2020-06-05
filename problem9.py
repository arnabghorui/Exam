import numpy as np
np.set_printoptions(precision=2)
np.set_printoptions(suppress=True)

A1 = np.array([ [2, 1],
				[1, 0],
				[0, 1] ])

A2 = np.array([ [1, 1, 0],
				[1, 0, 1],
				[0, 1, 1] ])
u1, s1, vh1 = np.linalg.svd(A1, full_matrices=True)
u2, s2, vh2 = np.linalg.svd(A2, full_matrices=True)

print("Singular values for first matrix are: ", s1[0],", ", s1[1] )
print("Singular values for second matrix are: ", s2[0],", ",s2[1],", ", s2[2])
