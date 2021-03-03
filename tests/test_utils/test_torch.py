"""
    PyTorch utility methods tests
"""

import torch

from quantum_computing.utils import torch as torch_utils


def test_kronecker():
    a_real = torch.Tensor([[1.0, 2.0], [3.0, 4.0]])
    a_imag = torch.Tensor([[1.0, 2.0], [3.0, 4.0]])
    a = torch.complex(a_real, a_imag)
    output = torch_utils.kronecker(a, a)

    excepted_real = torch.Tensor(
        [[0., 0., 0., 0.],
         [0., 0., 0., 0.],
         [0., 0., 0., 0.],
         [0., 0., 0., 0.]]
    )
    excepted_imag = torch.Tensor(
        [[2., 4., 4., 8.],
         [6., 8., 12., 16.],
         [6., 12., 8., 16.],
         [18., 24., 24., 32.]]
    )
    excepted = torch.complex(excepted_real, excepted_imag)

    assert torch.equal(output, excepted)
