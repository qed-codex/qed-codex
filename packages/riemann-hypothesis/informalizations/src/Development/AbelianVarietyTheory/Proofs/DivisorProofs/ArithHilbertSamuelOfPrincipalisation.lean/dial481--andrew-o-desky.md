---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ArithHilbertSamuelOfPrincipalisation.lean",
  "declarations": [
    "GlobalTheory.arithHilbertSamuel_of_principalisation"
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

## Arithmetic Hilbert–Samuel asymptotic

[Theorem ARAK.0040](https://andrewodesky.com/rh/lean/GlobalTheory.arithHilbertSamuel_of_principalisation/)

Let $R$ be an integral ring finite over $\mathbb Z$, not necessarily normal. Let $X$ be an integral projective $R$-scheme, flat over $\mathbb Z$, of dimension $D+1$. Let $\overline L$ and $\overline N$ be Hermitian line bundles on $X$. Assume ([Principalization on a smooth projective variety](https://andrewodesky.com/rh/lean/PositivityTheory.ResPlug.WeightsCompactStabilizer.principalisation_closed/)). Suppose $\overline L$ is nef: its metric is semipositive and its degrees on vertical and horizontal curves are nonnegative. Suppose its top arithmetic self-intersection exists and equals $a$ in the arithmetic-height normalization of ([Mixed arithmetic heights from archimedean integration and reciprocity](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_mixedHeight_of_archimedean_integrals/)).

Write $\widehat H^0(X,\overline L^{\otimes m}\otimes\overline N)$ for the integral sections of $L^{\otimes m}\otimes N$ with supremum norm at most one at every archimedean embedding. These sets are finite for all sufficiently large integers $m$, and $$\log\#\widehat H^0(X,\overline L^{\otimes m}\otimes\overline N)=\frac{a}{(D+1)!}m^{D+1}+o(m^{D+1}).$$
