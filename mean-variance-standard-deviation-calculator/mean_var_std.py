import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers !")

    # Convert list to 3 * 3 numpy array
    matrix = np.array(list).reshape(3,3)

    # Compute required statistics
    calculations = {
        'mean':[matrix.mean(axis = 0).tolist(),matrix.mean(axis=1).tolist(),matrix.mean().item()],
        'variance':[matrix.var(axis=0).tolist(),matrix.var(axis=1).tolist(),matrix.var().item()],
        'max': [matrix.max(axis=0).tolist(),matrix.max(axis=1).tolist(),matrix.max().item()],
        'min':[matrix.min(axis=0).tolist(),matrix.min(axis=1).tolist(),matrix.min().item()],
        'sum':[matrix.sum(axis=0).tolist(),matrix.sum(axis=1).tolist(),matrix.sum().item()],
        'standard deviation': [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std().item()],
    }




    return calculations