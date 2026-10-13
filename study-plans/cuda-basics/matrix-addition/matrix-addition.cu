#include <cuda_runtime.h>

__global__ void matrix_add_kernel(const float* A, const float* B, float* C, int M, int N) {
    // Write the float32 result into C; this kernel returns no value.
    int idx = blockDim.x*blockIdx.x+threadIdx.x;
    int idy = blockDim.y*blockIdx.y+threadIdx.y;
    if (idx < N && idy < M) {
        idx = idy*N+idx;
        C[idx]=A[idx]+B[idx]; }
}

extern "C" void solve(const float* A, const float* B, float* C, int M, int N) {
    dim3 threads(16, 16);
    dim3 blocks((N + 15) / 16, (M + 15) / 16);
    matrix_add_kernel<<<blocks, threads>>>(A, B, C, M, N);
    cudaDeviceSynchronize();
}
