import sympy as sp

# Let \mathbf{B} = B*(a,b,c) where (a,b,c) is a normalized vector (\hat B)
a, b, c, B = sp.symbols('a b c B', real=True)
# Force B -> B'\hat z'
pi2_phi = sp.atan2(b, a)
theta = sp.acos(c / sp.sqrt(a**2 + b**2 + c**2))

R_z = sp.Matrix([
    [sp.sin(pi2_phi), -sp.cos(pi2_phi), 0],
    [sp.cos(pi2_phi), sp.sin(pi2_phi), 0],
    [0, 0, 1]
])

R_x = sp.Matrix([
    [1, 0, 0],
    [0, sp.cos(theta), -sp.sin(theta)],
    [0, sp.sin(theta), sp.cos(theta)]
])

R_zx = R_x * R_z

# plug in sqrt(a^2 + b^2 + c^2) = 1

R_zx = R_zx.subs(sp.sqrt(a**2 + b**2 + c**2), 1)

R_zx = sp.simplify(R_zx)

# print(sp.latex(R_zx))

test_B = B * sp.Matrix([a, b, c])

# print(sp.latex(sp.simplify(((R_x * R_z) * test_B)
#                            ).subs(sp.sqrt(a**2 + b**2 + c**2), 1)))

text_x = sp.Matrix([1, 0, 0])
text_y = sp.Matrix([0, 1, 0])
text_z = sp.Matrix([0, 0, 1])

print(sp.latex(sp.simplify(sp.simplify(((R_x * R_z) * text_x)
                                       ).subs(sp.sqrt(a**2 + b**2 + c**2), 1))))
