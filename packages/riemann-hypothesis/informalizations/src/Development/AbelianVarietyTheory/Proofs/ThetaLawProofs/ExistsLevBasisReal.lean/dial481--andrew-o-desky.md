---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/ThetaLawProofs/ExistsLevBasisReal.lean",
  "declarations": [
    "GlobalTheory.KeyKa.LevelBasis.exists_levBasis"
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

## A holomorphic family of bases of level theta functions

[Theorem AV.0207](https://andrewodesky.com/rh/lean/GlobalTheory.KeyKa.LevelBasis.exists_levBasis/)

Let $g\ge0$, $l\ge1$, and $a,b\in\{0,\tfrac12\}^g$. There are $l^g$ functions $\Theta_k(P,z)$, for $P\in M_g(\mathbb C)$ with $$\tau(P)=\frac{P+P^t}{2}\in\mathfrak H_g,$$ which are jointly holomorphic in $(P,z)$ and, for every such $P$, form a basis of the entire functions $F:\mathbb C^g\to\mathbb C$ satisfying $$F(z+m+\tau(P)n)=\exp\left(2\pi i\left(a\cdot m-b\cdot n-\frac12n^t\tau(P)n-n\cdot z\right)\right)^lF(z)\qquad(m,n\in\mathbb Z^g).$$ Here $\mathfrak H_g$ consists of symmetric complex matrices with positive definite imaginary part. Every such $F$ has a unique expansion $F(z)=\sum_k c_k\Theta_k(P,z)$ with $c_k\in\mathbb C$.
