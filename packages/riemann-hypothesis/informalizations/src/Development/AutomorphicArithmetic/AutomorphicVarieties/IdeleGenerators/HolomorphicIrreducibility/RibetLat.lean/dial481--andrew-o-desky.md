---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/IdeleGenerators/HolomorphicIrreducibility/RibetLat.lean",
  "declarations": [
    "UpperTheory.V.Sd.ribetLat"
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

## A basis with a nontrivial upper triangular residual extension

[Theorem AGR.0404](https://andrewodesky.com/rh/lean/UpperTheory.V.Sd.ribetLat/)

Let $\ell$ be prime and $\Gamma$ a compact Hausdorff topological group. Let $\rho:\Gamma\to\mathrm{GL}_2(\overline{\mathbb Q}_\ell)$ be continuous and irreducible, and let $a,b:\Gamma\to\overline{\mathbb Q}_\ell^\times$ be characters with $|a(g)|_\ell=|b(g)|_\ell=1$. Assume that every coefficient of $$\det(T-\rho(g))-(T-a(g))(T-b(g))$$ has absolute value less than one, for every $g$. If $g_0\in\Gamma$ satisfies $|a(g_0)-b(g_0)|_\ell\ge1$, there is an isomorphic representation $\rho'$ with $\rho'(g_0)$ diagonal and, for all $g$, $$|\rho'_{00}(g)-a(g)|_\ell<1,\quad |\rho'_{11}(g)-b(g)|_\ell<1,$$ $$|\rho'_{10}(g)|_\ell<1,\qquad |\rho'_{01}(g)|_\ell\le1.$$ Moreover $|\rho'_{01}(g)|_\ell=1$ for at least one $g$.
