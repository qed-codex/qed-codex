---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/ModuliProofs/PrincipalTorusAlgebraic.lean",
  "declarations": [
    "GlobalTheory.principalTorus_algebraic"
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

## Algebraization of a principally polarized complex torus

[Theorem AV.0485](https://andrewodesky.com/rh/lean/GlobalTheory.principalTorus_algebraic/)

Let $\Lambda\subset\mathbb C^g$ be a discrete $\mathbb Z$-submodule spanning $\mathbb C^g$ over $\mathbb R$. Let $H$ be a positive-definite Hermitian matrix and set $h(z,w)=z^tH\overline w$. Let $E:\Lambda\times\Lambda\to\mathbb Z$ be bilinear with $$E(a,b)=\operatorname{Im}h(a,b),$$ and suppose $a\mapsto E(a,\cdot)$ is a bijection $\Lambda\to\operatorname{Hom}_{\mathbb Z}(\Lambda,\mathbb Z)$.

There are a complex abelian variety $A$ of dimension $g$, a rigidified symmetric ample line bundle $L$ with trivial translation kernel, and a surjective holomorphic group map $u:\mathbb C^g\to A(\mathbb C)$ with kernel exactly $\Lambda$. The differential $du_0$ bijectively identifies $\mathbb C^g$ with the tangent vectors of $A$ at the identity. There are $\chi:\Lambda\to\mathbb C$ with $|\chi(a)|=1$ and compatible nowhere-zero holomorphic factors $f_i$ for local frames of $u^*L$ such that $$f_i(z)=\chi(a)\exp\!\left(\pi h(z,a)+\frac\pi2h(a,a)\right)f_i(z+a)$$ whenever $u(z)$ lies in the domain of the frame $i$.
