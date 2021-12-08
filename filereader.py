import re

# with open('../Downloads/dec2_results.txt') as file:
#     max_acc = -1
#     epoch = -1
#     max_epoch = -1
#     for line in file:
#         l = line.rstrip()
#         if 'RUNNING NOW' in l:
#             print(max_epoch, max_acc) # max_acc
#             max_epoch, epoch, max_acc = -1, -1, -1 # starting new experiment
#             print(l.split('RUNNING NOW',1)[1].rstrip())
#         if 'Iteration' in l:
#             epoch = [int(s) for s in l.split() if s.isdigit()][0]
#         if '| Test Accuracy             |       ' in l:
#             acc = float(re.findall(r"[-+]?\d*\.\d+|\d+", l)[0])
#             if acc > max_acc:
#                 max_acc = acc
#                 max_epoch = epoch
# 
#     print(max_epoch, max_acc) # max_acc
# 
# with open('../Downloads/dec2_reults_distilBERT.txt') as file:
#     max_acc = -1
#     epoch = -1
#     max_epoch = -1
#     for line in file:
#         l = line.rstrip()
#         if 'RUNNING NOW' in l:
#             print(max_epoch, max_acc) # max_acc
#             max_epoch, epoch, max_acc = -1, -1, -1 # starting new experiment
#             print(l.split('RUNNING NOW',1)[1].rstrip())
#         if 'Iteration' in l:
#             epoch = [int(s) for s in l.split() if s.isdigit()][0]
#         if '| Test Accuracy             |       ' in l:
#             acc = float(re.findall(r"[-+]?\d*\.\d+|\d+", l)[0])
#             if acc > max_acc:
#                 max_acc = acc
#                 max_epoch = epoch
# 
#     print(max_epoch, max_acc) # max_acc


with open('../Downloads/listops.txt') as file:
    max_acc = -1
    epoch = -1
    max_epoch = -1
    for line in file:
        l = line.rstrip()
        if 'RUNNING NOW' in l:
            print(max_epoch, max_acc) # max_acc
            max_epoch, epoch, max_acc = -1, -1, -1 # starting new experiment
            print(l.split('RUNNING NOW',1)[1].rstrip())
        if 'Iteration' in l:
            epoch = [int(s) for s in l.split() if s.isdigit()][0]
        if '| Test Accuracy             |       ' in l:
            acc = float(re.findall(r"[-+]?\d*\.\d+|\d+", l)[0])
            if acc > max_acc:
                max_acc = acc
                max_epoch = epoch

    print(max_epoch, max_acc) # max_acc
