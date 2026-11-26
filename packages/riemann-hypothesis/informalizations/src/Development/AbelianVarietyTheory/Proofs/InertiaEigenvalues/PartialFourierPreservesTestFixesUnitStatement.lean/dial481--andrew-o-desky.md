---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/PartialFourierPreservesTestFixesUnitStatement.lean",
  "declarations": [
    "GlobalTheory.T.partialFourier_preserves_test_fixes_unit"
  ],
  "author": "dial481",
  "writer": "Andrew O'Desky",
  "origin": "other-author",
  "source": "https://andrewodesky.com/rh/",
  "source_commit": "40e56bab026552e089d7afcfeff08d2defb9c005",
  "license": "with-permission"
}
---

As published on 26 November 2026.

## Partial Fourier transforms preserve test functions and the integral unit

[Theorem ANT.0217](https://andrewodesky.com/rh/lean/GlobalTheory.T.partialFourier_preserves_test_fixes_unit/)

Let $F\subseteq E$ be nontrivially normed fields with a compatible normed algebra structure. Suppose both are ultrametric and locally compact, $F$ has characteristic zero, $[E:F]=2$, and $E$ has an involution fixing the scalar field, preserving the norm and nontrivial on $E$. Assume every norm of an element of $E$ also occurs as the norm of an element of $F$. Fix the measure and character normalizations below, and let $r\ge0$.

For functions on $M_r(F)\times F^r\times F^r\times F$ and on $\operatorname{Herm}_r(E)\times E^r\times F$, respectively, put $$\widehat f(A,b,c,d)=\int_{F^r}\int_{F^r}f(A,b',c',d)\,\psi(c'\cdot b+c\cdot b')\,db'\,dc',$$ $$\widehat h(A,b,d)=\int_{E^r}h(A,c,d)\,\psi\!\left(\operatorname{Tr}_{E/F}(\overline c\cdot b)\right)\,dc.$$ Each transform carries locally constant compactly supported functions to functions of the same kind. The characteristic functions of the respective sets where every matrix, vector and scalar coordinate has norm at most one are themselves test functions and are fixed by their respective transforms.
