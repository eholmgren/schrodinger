# Schrodinger 
### Eric Holmgren

This project is used to calculate the lowest energy wave function on a given domain and potential field in terms of a given basis set (either Legendre or Fourier polynomials). The 

To use this program, call the python program schrod.py with your choice in input parameters. This looks like:

```python schrod.py --basis_func='legendre' --basis_size=5 --c=1.0 --v=1.0 --domain=(0,1)```  

The lowest energy state is given by the eigenvector of the Hamiltonian matrix <Ψ|H|Ψ> corresponding with its smallest eigenvalue.

Coverage and test passing can be tested by running:

```python -m pytest```

