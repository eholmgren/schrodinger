import argparse
import numpy as np
import numpy.polynomial.legendre as L
import numpy.linalg as linalg

#basis functions
def fourier(x):
    '''fourier polynomials'''
    return x**2

#defaults
C = 1.0
V = 1.0
BASIS_SIZE = 5
DOMAIN = (-1, 1)
BASIS_FUNC = 'legendre'



def get_arguments(): #pragma: no cover
    '''Get arguments from commandline'''
    parser = argparse.ArgumentParser(description='Schrodinger setup')
    parser.add_argument('--c', type=float, default=C, help='kinetic energy constant')
    parser.add_argument('--v', type=float, default=V, help='potential energy constant')
    parser.add_argument('--basis_size', type=int, default=BASIS_SIZE, help='size of the basis set')
    parser.add_argument('--domain', type=tuple, default=DOMAIN, help='tuple of length 2')
    parser.add_argument('--basis_func', type=str, default=BASIS_FUNC, help='legendre or fourier')
    return parser.parse_args()

def hamiltonian(coefs, func=BASIS_FUNC, V=V, C=C):
    '''hamiltonian operator acting on wavefunction'''
    if func == 'legendre':
        ham = -C*L.legder(L.legder(coefs)) + V*L.Legendre(coefs)
        return ham

def inner_product():
    if BASIS_FUNC == 'legendre':
        pmat = np.zeros((BASIS_SIZE, BASIS_SIZE))
        for i in range(BASIS_SIZE):
            for j in range(BASIS_SIZE):
                coefs_i = [0]*(i) + [1]
                coefs_j = [0]*(j) + [1]
                inside = L.legmul(coefs_i, coefs_j)
                integ = L.legint(inside)
                val = L.legval(DOMAIN[1],integ) - L.legval(DOMAIN[0],integ)
                pmat[i,j] = val
    return pmat



def hamiltonian_matrix(BASIS_SIZE=BASIS_SIZE, BASIS_FUNC=BASIS_FUNC, DOMAIN=DOMAIN, C=C, V=V):
    if BASIS_FUNC == 'legendre':
        hmat = np.zeros((BASIS_SIZE, BASIS_SIZE))
        for i in range(BASIS_SIZE):
            for j in range(BASIS_SIZE):
                coefs_i = [0]*(i) + [1]
                coefs_j = [0]*(j) + [1]
                inside = L.legmul(coefs_i, list(hamiltonian(coefs_j)))
                integ = L.legint(inside)
                val = L.legval(DOMAIN[1],integ) - L.legval(DOMAIN[0],integ)
                hmat[i,j] = val
    return hmat

def first_eigen(mat):
    eigenvalues,eigenvectors = linalg.eig(mat)
    print('VALS',eigenvalues)
    print('VECS',eigenvectors)
    print(min(eigenvalues))
    print(eigenvectors[np.argmin(eigenvalues)])
    return eigenvectors[np.argmin(eigenvalues)]



def run(args):
    print('HAMMY',list(hamiltonian([1])))
    print('IPMAN',inner_product())
    print(hamiltonian_matrix(BASIS_SIZE=5))
    print('asdf',first_eigen(hamiltonian_matrix(BASIS_SIZE=5)))

def main():
    args=get_arguments()
    print(args)
    run(args)

if __name__=='__main__':
    main()


