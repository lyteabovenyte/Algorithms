"""
    implementation for AVL-Tree rotations.
"""

def rotate_right(y):
    x = y.left
    y.left = x.right
    x.right = y
    return x  # New root after rotation
"""
        Y
       /
      X
       \
        B
        
    into
        
       X
       \
        Y
       /
      B
"""

def rotate_left(x):
    y = x.right
    x.right = y.left
    y.left = x
    return y  # New root after rotation

"""
       X
       \
        Y
       /
      B
    
    into
       
        Y
       /
      X
       \
        B
"""