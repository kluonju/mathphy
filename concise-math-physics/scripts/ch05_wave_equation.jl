#!/usr/bin/env julia
# 1D wave equation explicit scheme
L, c, nx, nt = 1.0, 1.0, 100, 200
dx = L / (nx - 1)
dt = 0.5 * dx / c
x = range(0, L, length=nx)
u = sin.(π * x)
u_prev = copy(u)
for _ in 1:nt
    u_next = similar(u)
    u_next[1] = u_next[end] = 0.0
    for i in 2:nx-1
        u_next[i] = 2u[i] - u_prev[i] + (c * dt / dx)^2 * (u[i+1] - 2u[i] + u[i-1])
    end
    u_prev, u = u, u_next
end
println("Wave simulation done, u(mid) = ", u[nx÷2])
