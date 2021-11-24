dim=[int(i) for i in input('Enter the dimensions: ').split(' ')]
matr=[]
k=[]
min_of_k=[]
min_of_out=[]
selected_k=[]
k_arr=[]
def functions(mmatr, ii, jj, kk):
    out=mmatr[ii][kk]+mmatr[kk+1][jj]+(dim[ii-1]*dim[kk]*dim[jj])
    return out
    
 
def brackets(matrix, initial, end):
    if initial == end:
        print('A{}'.format(initial), end='')
        return
    k = matrix[initial][end]
    print('(', end='')
    brackets(matrix, initial, k)
    brackets(matrix, k + 1, end)
    print(')', end='')

for i in range(len(dim)):
    a=[]
    for j in range(len(dim)):
       a.append(0) 
    matr.append(a)
    
for i in range(len(dim)):
    a=[]
    for j in range(len(dim)):
       a.append(0) 
    k_arr.append(a)

    
for jj in range(1, len(dim)-1):
    for i in range(1, len(dim)):
        for j in range(1, len(dim)):
            if j-i == jj:
                
                for a in range(i, j):
                    k.append(a)
                for b in k:
                    output=functions(matr, i, j, b)
                    min_of_k.append(b)
                    min_of_out.append(output)
                matr[i][j]=min(min_of_out)
                selected_k.append(min_of_k[min_of_out.index(matr[i][j])])
                k_arr[i][j]=min_of_k[min_of_out.index(matr[i][j])]
            k.clear()
            min_of_out.clear()
            min_of_k.clear()
            
print('\nFinal counting matrix: ')            
for i in matr:
    print(*i)                

print('\nK-value matrix: ')   
for i in k_arr:
    print(*i)

print('The Optimal Paranthsization of matrix chain product will be: ', end='')
brackets(k_arr, 1, len(dim)-1)


