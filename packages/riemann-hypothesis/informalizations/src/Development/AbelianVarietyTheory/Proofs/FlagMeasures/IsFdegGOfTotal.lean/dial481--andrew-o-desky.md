---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/FlagMeasures/IsFdegGOfTotal.lean",
  "declarations": [
    "GlobalTheory.Dec.SchurTotal.rel_dense",
    "GlobalTheory.Dec.isFdegG_of_total"
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

## Extending an orthogonality identity from a dense set

[Theorem REP.0834](https://andrewodesky.com/rh/lean/GlobalTheory.Dec.SchurTotal.rel_dense/)

Let $(G,\mu)$ be a measure space, $H$ a complex inner-product space, and $\sigma:G\to\mathcal L_{\mathbb C}(H)$ a family of continuous linear operators. Let $d>0$ and $T\subseteq H$ be dense. Assume every coefficient $g\mapsto\langle w,\sigma(g)v\rangle$ is measurable.

Suppose that for every $v,w,v',w'\in T$, the function $$g\longmapsto\langle w,\sigma(g)v\rangle\overline{\langle w',\sigma(g)v'\rangle}$$ is integrable and $$\int_G\langle w,\sigma(g)v\rangle\overline{\langle w',\sigma(g)v'\rangle}\,d\mu(g) =\frac{\langle v',v\rangle\langle w,w'\rangle}{d}.$$ The same integrability and identity hold for all $v,w,v',w'\in H$.

## Extending Schur orthogonality from a dense span

[Theorem REP.0872](https://andrewodesky.com/rh/lean/GlobalTheory.Dec.isFdegG_of_total/)

Let $G$ be a group with a topology and a measurable structure in which open sets are measurable, let $\mu$ be a measure on $G$, and let $H$ be a complex inner product space. Let $\pi:G\to\mathcal L(H)$ be a strongly continuous representation by norm-preserving bounded complex-linear operators. Fix $d>0$ and $S\subseteq H$ with dense complex linear span. Suppose that, whenever $v,w,v',w'\in S$, the function $$g\longmapsto\langle w,\pi(g)v\rangle\overline{\langle w',\pi(g)v'\rangle}$$ is integrable and its integral is $d^{-1}\langle v',v\rangle\langle w,w'\rangle$. Then the same integrability and integral identity hold for all $v,w,v',w'\in H$.
