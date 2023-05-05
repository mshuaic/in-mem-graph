import mmap
import struct
import numpy as np
# import pandas as pd


# import pyarrow as pa

# Open the binary file in read-only mode
# with pa.memory_map("/dev/shm/data.arrow") as mmap:
# loaded_arrays = pa.ipc.open_file(mmap).read_all()
# arr = loaded_arrays[0]
# print(f"{arr[0]} .. {arr[-1]}")
# data = mmap.read(10)
# print(data)

# print(list(zip(loaded_arrays[2], loaded_arrays[3])))
# print(loaded_arrays[3])
# pass

# print(loaded_arrays[2])
# df = loaded_arrays.to_pandas(split_blocks=True, self_destruct=True)
# print(df.head())

# write a simple example file
# with open("hello.txt", "wb") as f:
# f.write(b"Hello Python!\n")

# Student = namedtuple('data', )
# datatype = np.dtype("u4,u2,u8,u8,a16,a16")
# datatype = np.dtype(
# [("a", "u4"), ("b", "u2"), ("c", "u8"), ("d", "u8"), ("e", "a16"), ("f", "a16")]
# )

# datatype = np.dtype("i8")
# datatype = np.dtype([("a", "i8"), ("b", "i8")])
# # # with open("/dev/shm/data.bin", "r+b") as f, mmap.mmap(f.fileno(), 0) as mm:
# data = np.memmap("/dev/shm/edges.bin", dtype=datatype, mode="r", shape=(379120382, 2))
# print(list(data))


# with open("/dev/shm/edges.bin", "r+b") as f, mmap.mmap(f.fileno(), 0) as mm:
#     unpacked_data = struct.unpack("<676920896q", mm)
#     list_of_lists = [list(unpacked_data[i:i+2]) for i in range(0, len(unpacked_data), 2)]
# # #     for data in struct.iter_unpack("<qq", mm):
# # #         print(data)
# #         # pass
# #         # print(data[:3])
# #         # print(int.from_bytes(data[0][4], "little"))
# #         # print(int.from_bytes(data[0][5], "little"))
# #         # print(mm[:4])
# # #     # memory-map the file, size 0 means whole file
# # #     mm = mmap.mmap(f.fileno(), 0)

# print(list_of_lists[:10])

import os
 
with open("/dev/shm/edges.bin", "r+b") as f:
    mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    # x = memoryview(f.read())
    # x = memoryview(mm)
    # data = x.cast('q', shape=[x.nbytes//8//2,2])
    size = os.stat("/dev/shm/edges.bin").st_size // struct.calcsize("<q")
    # data = struct.unpack(f"<{size}q", mm)
    data = struct.iter_unpack('<qq', mm)
from igraph import Graph

# list(data)
G = Graph(n=size//2, edges=data)
G.pagerank()
# mm.close()

# import networkx as nx

# G = nx.from_edgelist(data)

# arr = pa.array(data)
# # # for row in data:
# #     # pass
# #     print(row)
# # data[0][4] - data[0][5]
# df = pd.DataFrame(data, copy=False)

# print(len(data))

# for data in struct.iter_unpack('<IHQQ16s16s', mm):
# pass
# print(data[:3])
# print(int.from_bytes(data[0][4], "little"))
# print(int.from_bytes(data[0][5], "little"))
# print(mm[:4])

# with open("hello.txt", "r+b") as f:
#     # memory-map the file, size 0 means whole file
#     mm = mmap.mmap(f.fileno(), 0)
#     # read content via standard file methods
#     print(mm.readline())  # prints b"Hello Python!\n"
#     # read content via slice notation
#     print(mm[:5])  # prints b"Hello"
#     # update content using slice notation;
#     # note that new content must have same size
#     mm[6:] = b" world!\n"
#     # ... and read again using standard file methods
#     mm.seek(0)
#     print(mm.readline())  # prints b"Hello  world!\n"
#     # close the map
#     mm.close()
