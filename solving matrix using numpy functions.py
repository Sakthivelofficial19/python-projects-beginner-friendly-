#matrix operations using numpy functions
import numpy as np
#lets have the linear quations in matrix form with three unknowns x,y,z
#equation 1
a=np.array([[2,3,1],
            [4,1,2],
            [3,2,3]])
#column matrix equation 2
b=np.array([[1,2,3]]).reshape(3,1)
no_unknowns=len(a)
homogeneity=False
invertibility = False
solution_status=False
if np.array_equal(np.zeros(b.shape),b):#equality check
    homogeneity=True
#to check whether it is invertible
if np.linalg.det(a)!=0:
    invertibility=True
    inverse_a=np.linalg.inv(a)
    x=np.dot(inverse_a,b)
    solution=np.round(x,2)
    solution_status=True
else:
    solution_status=False
# to check rank of the matrix in gaussian form
augmented_matrix=np.hstack((a,b))
augmented_rank=np.linalg.matrix_rank(augmented_matrix)
coefficient_rank=np.linalg.matrix_rank(a)
if augmented_rank==coefficient_rank:
    consistency=True
else:
    consistency=False
#check for unique or infinite no of solutions
    #if it is consistent then atleast have one solution
if consistency:
    value=-1*(augmented_rank-no_unknowns)
    if not value==0:
        no_solutions="infinite no of solutions"
    else:
        no_solutions="unique solutions"
print(f"""Homogeneity:{"homogeneous" if homogeneity else "non homogeneous"},
no_unknowns:{len(a)}
invertibility:{"invertible" if invertibility else "non invertible"},
solution:{solution if solution_status else "no solution"},
rank:{augmented_rank if consistency else "different rank(inconsistent)"},
consistency:{"consistent" if consistency else "inconsistent"},
no_solutions:{no_solutions if consistency else "zero solution"}

""")
        
            
    
    

            
        
        


