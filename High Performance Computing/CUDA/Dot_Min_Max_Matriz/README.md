# Sum of dot product, min and max values between two matrices.
Given two NxN 2D-arrays A and B, find the sum of the dot product of A and B, the min and max values between these two given 2d-arrays using **CUDA C programming**. 

This program reads the two given arrays in row major order and uses three cuda Streams to find the results. To do it, we needed to use pinned memory (check notes 2 and 3).

## Instructions
- Compile by entering `nvcc cuda.cu -o cuda`
- Run this program with `./cuda`

## Notes
1. There is a test case (entrada.txt) inside this folder.
2. [How to Optimize Data Transfers in CUDA C/C++](https://developer.nvidia.com/blog/how-optimize-data-transfers-cuda-cc/);
3. [Advantages/Disadvantages of using pinned memory](https://forums.developer.nvidia.com/t/advantages-disadvantages-of-using-pinned-memory/34422).