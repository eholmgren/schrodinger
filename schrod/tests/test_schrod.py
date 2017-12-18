import schrod
import numpy as np
import numpy.polynomial.legendre as L

def test_hamiltonian():
    '''checks if hamiltonian is calculated correctly'''
    ham = schrod.hamiltonian((1,1), 'legendre', 1, 0)
    assert ham == L.Legendre((1,1))

def test_hamiltonian_matrix(): #have this actually test something
    schrod.hamiltonian_matrix()

def test_first_eigen():
    '''can first_eigen calculate eigenvectors'''
    vec = schrod.first_eigen([[1,2],[2,6]])
    assert(np.allclose(vec,[-0.94362832, -0.33100694]))

def test_run():
    '''does the entire program run'''
    schrod.run({})