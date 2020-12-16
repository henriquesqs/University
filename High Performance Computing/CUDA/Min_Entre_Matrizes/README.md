# Min between 2d-arrays
Given two 2d-arrays A and B, find the minimum element in A and B.

We are using **CUDA C programming language** here with two Cuda Streams, where the first stream computes the min element on A and the second stream finds the min element on B. To do so, we needed to use pinned memory (check notes 2 and 3).

## Instructions
- Compile by entering `nvcc min.cu -o min`;
- Run with `./min`

## Notes
1. There is a test case (min.txt) inside this folder;
2. [How to Optimize Data Transfers in CUDA C/C++](https://developer.nvidia.com/blog/how-optimize-data-transfers-cuda-cc/);
3. [Advantages/Disadvantages of using pinned memory](https://forums.developer.nvidia.com/t/advantages-disadvantages-of-using-pinned-memory/34422);