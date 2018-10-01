'''
this code computes minimum edit distance between 2 strings and
prints sequence of insertion/deletion/substitution operations required to convert source string to target string
'''

__author__ = 'nishant'

def edit_distance(source, target):
    matrix = []

    source = '\0'+source
    target = '\0' + target

    for i in range(len(target)):
        if i == 0:
            matrix.append(range(len(source)))
        else:
            matrix.append([i]+[0]*(len(source)-1))

    for i in range(1,len(target)):
        for j in range(1, len(source)):
            if target[i] == source[j]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                matrix[i][j] = min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1])+1

    movement = backtrace(matrix, target, source)

    return matrix[len(target)-1][len(source)-1], movement

def backtrace(matrix, target, source):

    movement = []
    target_index, source_index = len(target)-1, len(source) - 1

    while target_index >= 1 and source_index >= 1:
        if target[target_index] == source[source_index]:  # if corresponding chars are same, we move to upper left diagnol cell
            target_index -= 1
            source_index -= 1
        else:
            diag_val = matrix[target_index-1][source_index-1]
            up_val = matrix[target_index-1][source_index]
            left_val = matrix[target_index][source_index-1]

            min_val = min(diag_val, up_val, left_val)

    # assigning the kind of operation - s - substitution, i - insertion, d - deletion
            if min_val == diag_val:
                operation = 's'
                movement.append([source[source_index], operation,target[target_index]])
                target_index -= 1
                source_index -= 1
            elif min_val == up_val:
                operation = 'i'
                movement.append([target[target_index], operation])
                target_index -= 1
            else:
                operation = 'd'
                movement.append([source[source_index], operation])
                source_index -= 1

    return movement[::-1]

if __name__=="__main__":

    print edit_distance("leda","deal")  # 3
    print edit_distance("drive","brief")  # 3
    print edit_distance("drive","divers")  # 3