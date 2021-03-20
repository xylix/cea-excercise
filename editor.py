from typing import Tuple, Literal, Union

Op = Literal["1", "2", "3", "4"]


def append(S: str, W: str):
    S = S + W
    last_op = ("1", W)
    return S, last_op


def delete(S: str, k: int):
    diff = S[0:k]
    # print(f"diff: {diff}")
    S = S[:-k]
    last_op = ("2", diff)
    return S, last_op


Operation = Union[Tuple[Literal["1", "2"], str]]


def undo(S: str, last_op: Operation):
    last_op_type, last_param = last_op
    if last_op_type == "1":
        S, _ = delete(S, len(last_param))
    elif last_op_type == "2":
        S, _ = append(S, last_param)
    return S


Q = int(input())

S: str = ""
op_list = []
for i in range(0, Q):
    operation = input()
    # print(f"Op list: {op_list}")
    if operation == "4":
        S = undo(S, op_list.pop())
    else:
        t, param = operation.split(" ")
        if t == "1":
            S, last_op = append(S, param)
            op_list.append(last_op)
        elif t == "2":
            k = int(param)
            S, last_op = delete(S, k)
            op_list.append(last_op)
        elif t == "3":
            k = int(param) - 1
            # print(f"k: {k}", f"S: {S}")
            print(S[k])
        else:
            raise NotImplementedError()
