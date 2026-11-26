---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/InertCharpoly/CharPolOfInert.lean",
  "declarations": [
    "UpperTheory.Gal.Int.Row.plainTor_of_tor"
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

## Local support tests for zero-monodromy parameters

[Theorem REP.0160](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Int.Row.plainTor_of_tor/)

Let $E$ be a number field, $v$ a finite place, and $k=E_v$. Fix an algebraic closure and a place above $v$, so that the local Weil group $W_k$ and inertia $I_k$ are specified. Let $\operatorname{rec}$ be a local correspondence satisfying the reciprocity conditions used in ([Galois representations of polarized cusp forms](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Int.galoisLocalGlobalStrong_recParameter/)), including its good-supercuspidal and depth-zero conditions.

First, let $x$ be a generic smooth irreducible representation of $\mathrm{GL}_n(k)$ and put $y=\operatorname{rec}(x)$. Suppose $N_y=0$ and $$\det(T-y([g,h]))=(T-1)^{\dim y}\qquad(g,h\in W_k).$$ Then $x$ has supercuspidal support consisting of characters $\xi_1,\ldots,\xi_n$ of $k^\times$, with no two support constituents related by the twist $\nu$ defined below.

Second, assume $E$ is CM, $a\ge1$, and $\sigma$ is a finite local component at $v$ of a cuspidal automorphic representation of $\mathrm{GL}_a(\mathbb A_E)$. Put $y=\operatorname{rec}(\sigma|\det|^{(1-a)/2})$. Suppose $k$ is continuously isomorphic to $\mathbb Q_p$ for a prime $p$, $N_y=0$, and the characteristic polynomial of every wild-inertia element is $(T-1)^a$. Suppose also that for every inertia element generating $I_k$ modulo wild inertia topologically, each characteristic root $z$ of multiplicity at least two satisfies $z^{q_v-1}=1$. Then $$\sigma^{K_1}\ne0,\qquad K_1=\ker(\mathrm{GL}_a(\mathcal O_k)\longrightarrow\mathrm{GL}_a(k_v)).$$ In every supercuspidal support multiset of $\sigma|\det|^{(1-a)/2}$, the constituents of rank at least two are pairwise inequivalent up to unramified character twist, counting occurrences in the multiset.
