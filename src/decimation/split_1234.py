def split_array(array):
    """
    Downsample an even square array into combinations of even/odd indicies
    Example of 2D array split, grouped by number
     ___ ___ ___ ___
    |_0_|_1_|_0_|_1_|
    |_2_|_3_|_2_|_3_| 
    |_0_|_1_|_0_|_1_|
    |_2_|_3_|_2_|_3_|
  
    """

    shape = array.shape
    
    even = slice(None, None, 2)
    odd = slice(1, None, 2)
    
    pairs = [[even, odd] for dimension in range(len(shape))]
    
    split_idx = list(product(*pairs))
    
    split = np.array([array[idx] for idx in split_idx])
    
    return split
