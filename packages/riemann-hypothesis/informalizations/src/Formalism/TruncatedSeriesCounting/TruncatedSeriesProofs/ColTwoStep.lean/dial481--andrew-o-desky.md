---
{
  "module": "src/Formalism/TruncatedSeriesCounting/TruncatedSeriesProofs/ColTwoStep.lean",
  "declarations": [
    "Formalism.TruncatedSeriesCounting.TruncatedSeriesCountingBounds.length_quotient_le_of_two_step"
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

## A quotient-length bound from two generating stages

[Theorem ALG.1039](https://andrewodesky.com/rh/lean/Formalism.TruncatedSeriesCounting.TruncatedSeriesCountingBounds.length_quotient_le_of_two_step/)

Let $O$ be a commutative ring, $M$ an $O$-module, $I\subseteq Z\subseteq M$ submodules, and $\ell,g,g_0,e,e'\ge0$ integers. Suppose there are finite sets $S\subset M$, $S_0\subset Z$, with $|S|\le g$, $|S_0|\le g_0$, such that $$\langle S\rangle_O+I=Z,\qquad \ell^eZ\subseteq\langle S_0\rangle_O+I,\qquad \ell^{e'}\langle S_0\rangle_O\subseteq I.$$ Then, with module lengths in $\mathbb N\cup\{\infty\}$, $$\operatorname{length}_O(Z/I)\le(ge+g_0e')\operatorname{length}_O(O/\ell O).$$
