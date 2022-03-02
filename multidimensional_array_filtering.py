# %% [markdown]
# ### Initial Part
# We have defined a 3D, 3x2x4 numpy array named `array_3D`.

# %%
import numpy as np
array_3B = np.arange(0, 24).reshape(3, 2, 4)
print("Our array: ", array_3B)
print("Dimensions of our array: ", array_3B.shape)
print("Our array has a size of ", array_3B.ndim, " pieces.")

# %% [markdown]
# Let's consider the first axis (dimension) of this array as "floors", the second axis as "apartments", and the third axis as "rooms". It has three floors ([0],[1], [2]) and two apartments(left[0], right[1]) on each floor. Each apartment has four rooms (living room[0], bedroom[1], kitchen[2], bathroom[3]). There are 3x2x4 = 24 rooms in total, and the values we give are the number of tables in each room.

# %%
print("Number of 'floors' on the first axis: ", array_3B.shape[0])
print("Number of 'apartments' on the second axis: ", array_3B.shape[1])
print("Number of 'rooms' on the third axis: ", array_3B.shape[2])

# %% [markdown]
# Let's get, in one row, the number of tables (_or fridge magnet_) in the kitchens of each right apartment on each floor.

# %%
print("The number of magnets in the kitchen of the right apartments on each floor : ",
      array_3B[0:3, 1, 2])

# %% [markdown]
# Let's list the apartments with more than 3 magnets in their kitchens.

# %%
array_3B_filter = array_3B[array_3B[:, :, 2] > 3]
# Just to get the apartment numbers:
array_3B_apartments = np.delete(array_3B_filter, [0, 2, 3], 1)
print("Apartments with more than 3 magnets in their kitchens",
      array_3B_apartments.tolist())

# %% [markdown]
# **Bonus**: Let's define the values of a 3-dimensional array as the sum of the indices of each respective cell. For example: array_3B will be [0,1,2] --> 3.

# %%
array_3B = np.empty([3, 2, 4])
for first_axis in np.arange(array_3B.shape[0]):
    for second_axis in np.arange(array_3B.shape[1]):
        for third_axis in np.arange(array_3B.shape[2]):
            array_3B[first_axis, second_axis,
                     third_axis] = first_axis + second_axis + third_axis
print("Our array :", array_3B)

# %% [markdown]
# ### Second Part
# Let's have an _ugly_ array like `a = np.array([ 1,  7, 10, 12,  0,  9,  2,  0,  0,  8, 10, 14,  5, 14,  5, 4, 14, 5,  1,  5,  9,  4, 12])` Let's discard those less than 5 and those greater than 10 from this array.

# %%
a = np.array([1,  7, 10, 12,  0,  9,  2,  0,  0,  8, 10,
             14,  5, 14,  5, 4, 14, 5,  1,  5,  9,  4, 12])
a_filter = list(s for s in a if s > 5 and s < 10)
print("greater than 5 and less than 10 : ", a_filter)
