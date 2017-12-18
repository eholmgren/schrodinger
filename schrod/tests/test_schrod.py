import schrod
import numpy.polynomial.legendre as L

def test_hamiltonian():
    '''checks if hamiltonian is calculated correctly'''
    ham = schrod.hamiltonian((1,1), 'legendre', 1, 0)
    assert ham == L.Legendre((1,1))

def test_hamiltonian_matrix():
    schrod.hamiltonian_matrix()