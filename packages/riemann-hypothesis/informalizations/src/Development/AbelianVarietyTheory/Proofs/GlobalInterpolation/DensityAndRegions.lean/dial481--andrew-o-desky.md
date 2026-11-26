---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/DensityAndRegions.lean",
  "declarations": [
    "GlobalTheory.ZerosNearOne.density_and_regions"
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

## Zeros near one and exceptional zeros

[Theorem ANT.1747](https://andrewodesky.com/rh/lean/GlobalTheory.ZerosNearOne.density_and_regions/)

There are absolute constants $C,c>0$ such that, for $Q\ge3$, the zeros of primitive Dirichlet $L$-functions of conductor at most $Q$ in $$\Re\rho\ge399/400,\qquad |\Im\rho|\le Q$$ have total multiplicity at most $CQ^{1/4}$, with multiplicities given by analytic orders. Equivalently, the bound holds for every finite set of character–zero pairs in this region. For each primitive character $\chi$ of conductor $N\ge3$, a zero satisfying $$\Re\rho\ge1-\frac{c}{\log\max(N,N|\Im\rho|)}$$ forces $\chi$ to be real; that zero is real, simple, and the only zero of this character satisfying the same inequality. Every zeta zero with $0<\Re\rho<1$ satisfies $$\Re\rho\le1-\frac{c}{\log(|\Im\rho|+3)}.$$
