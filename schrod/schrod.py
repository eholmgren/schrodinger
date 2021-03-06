import argparse
import numpy as np
import numpy.polynomial.legendre as L
import numpy.linalg as linalg

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
    elif func == 'fourier':
        ham = [V] + [(i**2)*C*coefs[i] for i in range(1,len(coefs))]
        return ham

def inner_product(): #do I even need this?
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



def hamiltonian_matrix(BASIS_SIZE=BASIS_SIZE, BASIS_FUNC=BASIS_FUNC, DOMAIN=DOMAIN, C=C, V=V):
    '''Calculates the hamiltonian matrix <psi|H|psi>'''
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
    if BASIS_FUNC == 'fourier':
        a = DOMAIN[1] #restrict the domain to be symmetric about origin for simplicity
        hmat = np.zeros((BASIS_SIZE,BASIS_SIZE))
        for i in range(BASIS_SIZE):
            for j in range(BASIS_SIZE):
                p1 = 2*V*np.sin(a*j)/j #cos V0 term
                p2 = 0 #cos cos term cancels due to parity if i != j
                if i==j:
                    p2 = C*(j**2)*(a + np.sin(2*a*j)/(2*j))
                hmat[i,j] = p1+p2
    return hmat

def first_eigen(mat):
    '''Calculates the lowest energy state (eigenvector corresponding to lowest eigenvalue)'''
    eigenvalues,eigenvectors = linalg.eig(mat)
    print('VALS',eigenvalues)
    print('VECS',eigenvectors)
    return eigenvectors[np.argmin(eigenvalues)]



def run(args):
    print('HAMMY',list(hamiltonian([1])))
    print('HAMIL',hamiltonian((1,2,3), 'fourier', 1.5, 3))
    print(hamiltonian_matrix(BASIS_SIZE=5))
    print(hamiltonian_matrix(5,'fourier',(-1,1),1,2))
    print('asdf',first_eigen(hamiltonian_matrix(BASIS_SIZE=5)))


    answer = first_eigen(hamiltonian_matrix())
    print('The coefficients of the basis set are ', answer)

def main():
    args=get_arguments()
    print(args)
    run(args)

if __name__=='__main__':
    main()


