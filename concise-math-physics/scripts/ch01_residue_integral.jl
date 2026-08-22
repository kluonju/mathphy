#!/usr/bin/env julia
using QuadGK

for a in [0.3, 0.5, 0.9]
    I, _ = quadgk(θ -> 1 / (1 + a * cos(θ)), 0, 2π)
    exact = 2π / sqrt(1 - a^2)
    println("a=$a: numeric=$I, exact=$exact, err=$(abs(I - exact))")
end
