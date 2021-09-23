def func_to_matrix(lambda_func,list1,list2):
    A =[]
    for idx1 in list1:
        A_row = []
        for idx2 in list2:
            A_row += [lambda_func(idx1,idx2)]
        A += [A_row]
    return A