#!/usr/bin/env julia
using Printf

x = range(-π, π, length=500)
f = sign.(sin.(x))
for N in [1, 3, 5, 21]
    s = sum((4 / (n * π)) * sin.(n * x) for n in 1:2:N)
    err = maximum(abs.(f .- s))
    @printf("N=%d: max error = %.4f\n", N, err)
end
