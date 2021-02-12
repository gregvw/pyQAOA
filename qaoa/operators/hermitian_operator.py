from qaoa.operators import LinearOperator
from qaoa.util import DocumentationInheritance
import numpy as np

class HermitianOperator(LinearOperator,metaclass=DocumentationInheritance):

    """
    Defines the interface of generic Hermitian operators and provides infrastructure used by 
    derived types

    """

    import abc

    def __str__(self):
        return "HermitianOperator"

    @abc.abstractmethod
    def __deepcopy__(self,memo):
        raise NotImplementedError("{0} does not override __deepcopy__() method".format(str(self)))


    @abc.abstractmethod
    def true_minimum(self):
        """
        Return the minimum eigenvalue of the Hermitian operator

        .. math:: 
            \mu = \min_{v\in\mathbb{R}^m} \\frac{\|Av\|}{\|v\|}

        """
        raise NotImplementedError("{0} does not override true_minimum() method".format(str(self)))

    @abc.abstractmethod
    def true_maximum(self):
        """
        Return the maximum eigenvalue of the Hermitian operator
  
      .. math:: 
            \mu = \max_{v\in\mathbb{R}^m} \\frac{\|Av\|}{\|v\|}
        """        
        raise NotImplementedError("{0} does not override true_maximum() method".format(str(self)))

    @abc.abstractmethod
    def inner_product(self,u,v):
        """
        Compute the inner product of two vectors using the Hermitian operator

        Returns the value that would be computed by the code
 
        >>> u.dot( A.as_matrix().dot(v) )

        Parameters
        ----------
        u : numpy.ndarray
            One-dimensional vector with length equal to len(A)
        v : numpy.ndarray
            One-dimensional vector with length equal to len(A)

        Returns
        -------
        value : scalar (possibly complex)
            Returns a scalar value determined by u.dtype and v.dtype 

        """
        raise NotImplementedError("{0} does not override method inner_product()".format(str(self)))

    @abc.abstractmethod
    def conj_inner_product(self,u,v):
        """
        Compute the complex-conjugated inner product of two vectors using the Hermitian operator

        Returns the value that would be computed by the code

        >>> u.conj().dot( A.as_matrix().dot(v) )

        Parameters
        ----------
        u : numpy.ndarray
            One-dimensional vector with length equal to len(A)
        v : numpy.ndarray
            One-dimensional vector with length equal to len(A)

        Returns
        -------
        value : scalar (possibly complex)
            Returns a scalar value determined by u.dtype and v.dtype 

        """
        raise NotImplementedError("{0} does not override method conj_inner_product()".format(str(self)))

    @abc.abstractmethod
    def expectation(self,v):
        """
        Compute the expectation of this Hermitian operator with the given vector
        
        Returns the value that would be computed by the code

        >>> v.conj().dot( A.as_matrix().dot(v) )

        Parameters
        ----------
        v : numpy.ndarray
            One-dimensional vector with length equal to len(A)

        Returns
        -------
        value : scalar (real)
            Returns a scalar value determined by v.dtype 
             
        """
        return np.real(self.conj_inner_product(v,v))

    @abc.abstractmethod
    def propagator(self,theta=0):
        """
        Return the control-parametrized unitary generated by this operator

        Creates a new object of the form 
  
        .. math:: U_A(\\theta) = \exp(i \\theta A)

        where A is the current operator

        Parameters
        ----------
        theta : scalar (real,optional)
            Initial control angle for the propagator. Default value is zero.
 
        Returns
        -------
        U : qaoa.operators.Propagator
            A control-parameterized unitary operator of Propagator type. Specific derived type is 
            determined by the HermitianOperator type that generates it.
        """
        raise NotImplementedError("{0} foes not override method propagator()".format(str(self)))

    def apply_adjoint(self,v,Hv):
        self.apply(v,Hv)

    def apply_adjoint_inverse(self,v,Hv):
        self.apply_inverse(v,Hv)


