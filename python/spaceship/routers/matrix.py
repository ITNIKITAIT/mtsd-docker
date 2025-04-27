from fastapi import APIRouter
import numpy as np

router = APIRouter()

@router.get("")
async def multiply_matrices():
    matrix_a = np.random.randint(0, 10, (10, 10)).tolist()
    matrix_b = np.random.randint(0, 10, (10, 10)).tolist()
    product = (np.matmul(matrix_a, matrix_b)).tolist()
    return {
        "matrix_a": matrix_a,
        "matrix_b": matrix_b,
        "product": product
    }
