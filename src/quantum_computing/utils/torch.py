"""
    PyTorch utility methods and classes
"""

import torch


def kronecker(t1: torch.Tensor, t2: torch.Tensor) -> torch.Tensor:
    """
        Computes the Kronecker product between two tensors.
        See https://en.wikipedia.org/wiki/Kronecker_product

        :param t1: first tensor
        :param t2: second tensor
        :returns: Tensor obtained from Kronecker product between t1 and t2
    """
    t1_height, t1_width = t1.size()
    t2_height, t2_width = t2.size()
    out_height = t1_height * t2_height
    out_width = t1_width * t2_width

    tiled_t2 = t2.repeat(t1_height, t1_width)
    expanded_t1 = (
        t1.unsqueeze(2)
            .unsqueeze(3)
            .repeat(1, t2_height, t2_width, 1)
            .view(out_height, out_width)
    )

    return expanded_t1 * tiled_t2
