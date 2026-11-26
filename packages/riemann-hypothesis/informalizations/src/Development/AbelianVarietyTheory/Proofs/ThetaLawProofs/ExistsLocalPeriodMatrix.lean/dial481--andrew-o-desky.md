---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/ThetaLawProofs/ExistsLocalPeriodMatrix.lean",
  "declarations": [
    "GlobalTheory.PeriodLift.exists_local_period_matrix"
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

## A local holomorphic family of normalized period matrices

[Theorem AV.0813](https://andrewodesky.com/rh/lean/GlobalTheory.PeriodLift.exists_local_period_matrix/)

Assume the polarized abelian-scheme laws in the conventions and ([Theta functions for a principally polarized complex abelian variety](https://andrewodesky.com/rh/lean/GlobalTheory.thetaUnifAV_closed/)). Let $K$ be a field, $\sigma:K\hookrightarrow\mathbb C$, $s:X\to\operatorname{Spec}K$ locally of finite type, and $(A,L)$ a polarized abelian scheme on $X$ in these packages. Fix $k>0$ and sections $l(a)\in A(X)$, indexed by $a\in\mathbb Z^{2g}$, with $kl(a)=0$.

Let $B\subset\mathbb C^m$ be open, $b_0\in B$, and $y:B\to X(\mathbb C)$ holomorphic over $\sigma$. Suppose the fibre at $y(b_0)$ is identified as a polarized abelian variety with $\mathbb C^g/(\tau_0\mathbb Z^g+\mathbb Z^g)$, where $\tau_0$ is symmetric with positive-definite imaginary part, and $l(a)$ at that fibre is represented by $(\tau_0a_1+a_2)/k$ for $a=(a_1,a_2)$. Require the Weil-pairing normalization below.

There are an open neighborhood $b_0\in B'\subseteq B$ and a holomorphic matrix function $\tau:B'\to M_g(\mathbb C)$ with $\tau(b_0)=\tau_0$ such that, for every $b\in B'$, the polarized fibre at $y(b)$ has such a uniformization with period matrix $\tau(b)$, and its sections $l(a)$ are represented by $(\tau(b)a_1+a_2)/k$.
