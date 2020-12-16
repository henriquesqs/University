# [Thresholding (*Limiarização*)](https://en.wikipedia.org/wiki/Thresholding_(image_processing))
Given a constant (which we defined as *limiar*) T, replace each element (x,y) in the given array with 

![](https://i.imgur.com/42ffqgU.png)

We are using CUDA C programming language with pinned memory which is faster than the conventional allocation (see note 2 and 3)

## Instructions
- Compile by entering `nvcc limiar.cu -o limiar`;
- Run with `./limiar`

## Notes
1. There is a test case (limiar.txt) inside this folder;
2. [How to Optimize Data Transfers in CUDA C/C++](https://developer.nvidia.com/blog/how-optimize-data-transfers-cuda-cc/);
3. [Advantages/Disadvantages of using pinned memory](https://forums.developer.nvidia.com/t/advantages-disadvantages-of-using-pinned-memory/34422);