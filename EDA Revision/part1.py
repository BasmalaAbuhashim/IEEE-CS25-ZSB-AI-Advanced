import numpy as np
def calculate(list):
    if(len(list) != 9):
        raise ValueError("List must contain nine numbers.")
    else:
        mtrx = np.array(list).reshape(3,3)
        calculations = {
            'mean' : [np.mean(mtrx,axis = 0).tolist(),np.mean(mtrx,axis = 1).tolist(),mtrx.mean()],
            'variance': [np.var(mtrx,axis = 0).tolist(), np.var(mtrx,axis = 1).tolist(),np.var(mtrx)],
            'Std': [np.std(mtrx,axis = 0).tolist(), np.std(mtrx,axis = 1).tolist(),np.std(mtrx)],
            'min': [np.min(mtrx,axis = 0).tolist(), np.min(mtrx,axis = 1).tolist(),np.min(mtrx)],
            'max': [np.max(mtrx,axis = 0).tolist(), np.max(mtrx,axis = 1).tolist(),np.max(mtrx)],
            'sum': [np.sum(mtrx,axis = 0).tolist(), np.sum(mtrx,axis = 1).tolist(),np.sum(mtrx)],
        }

    return calculations

print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))

