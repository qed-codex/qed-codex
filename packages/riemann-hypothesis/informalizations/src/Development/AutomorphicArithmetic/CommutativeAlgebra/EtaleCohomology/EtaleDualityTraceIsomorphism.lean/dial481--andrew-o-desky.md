---
{
  "module": "src/Development/AutomorphicArithmetic/CommutativeAlgebra/EtaleCohomology/EtaleDualityTraceIsomorphism.lean",
  "declarations": [
    "UpperTheory.Et.etale_duality_trace_isomorphism"
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

## Additive characteristic classes in etale cohomology

[Theorem AG.0041](https://andrewodesky.com/rh/lean/UpperTheory.Et.etale_duality_trace_isomorphism/)

For every integer $q>0$ and $k>0$, there is an assignment $$V\longmapsto s_k(V)\in H^{2k}_{\mathrm{et}}(E,\mathbb Z/q\mathbb Z(k))$$ for every simplicial presheaf $E$ on schemes and every rank-$N$ bundle datum $V:E\to B\mathrm{GL}_N$, for every $N\ge0$. Say $q$ is invertible on $E$ if it is a unit in the global functions of every scheme carrying a zero-simplex of $E$. The assignment satisfies $$f^*s_k(V)=s_k(f^*V)\quad(f:E\to E',\ q\text{ invertible on }E'),$$ $$s_k(V\oplus W)=s_k(V)+s_k(W)\quad(q\text{ invertible on }E),$$ $$s_k(L)=c_1(L)^k\quad(q\text{ invertible on }E,\ L\text{ a line bundle datum}).$$ Here the cohomology and $B\mathrm{GL}_N$ use the source's etale simplicial-presheaf construction.
