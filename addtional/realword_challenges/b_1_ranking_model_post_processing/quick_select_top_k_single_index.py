"""
quick select for top k
single index partitioning
"""

from typing import Union


def quick_select_top_k(items: list, low: int,
                       high: int, top_k: int) -> Union[list, None]:
    #     """
    #     >>> quick_select([2, 4, 5, 7, 899, 54, 32], 5)
    #     [899, 54, 32, 7, 5]
    #     >>> quick_select([2, 4, 5, 7, 899, 54, 32], 1)
    #     [899]
    #     >>> quick_select([5, 4, 3, 2], 2)
    #     [5, 4]
    #     >>> quick_select([3, 5, 7, 10, 2, 12], 3)
    #     [12, 10, 7]
    #     """
    # invalid input
    if top_k >= len(items) or top_k < 0:
        return None
    pivot_idx = _partition(items, low, high)
    curr_top_count = len(items) - pivot_idx

    if curr_top_count == top_k:
        return items[pivot_idx:]
    # must select in the greater part
    elif curr_top_count > top_k:
        return quick_select_top_k(items,
                                  pivot_idx + 1, high,
                                  top_k
                                  )
    # must select remind element in the less part
    else:
        still_pick_count = top_k - curr_top_count
        return quick_select_top_k(items,
                                  low, pivot_idx - 1,
                                  still_pick_count)


def _partition(data: list, low: int, high: int) -> int:
    '''
    in place partitioning
    '''
    pivot = data[low]
    pass


print(quick_select_top_k(items=[2, 4, 5, 7, 899, 54, 32],
                         low=0, high=6,
                         top_k=5))
print(quick_select_top_k(items=[3, 5, 7, 10, 2, 12],
                         low=0, high=5,
                         top_k=6))
