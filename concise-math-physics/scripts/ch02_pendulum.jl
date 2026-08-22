#!/usr/bin/env julia
using DifferentialEquations

function pendulum!(du, u, p, t)
    θ, ω = u
    du[1] = ω
    du[2] = -(9.8 / 1.0) * sin(θ)
end

u0 = [0.1, 0.0]
prob = ODEProblem(pendulum!, u0, (0.0, 10.0))
sol = solve(prob, Tsit5())
println("Pendulum: θ(10) = ", sol.u[end][1])
