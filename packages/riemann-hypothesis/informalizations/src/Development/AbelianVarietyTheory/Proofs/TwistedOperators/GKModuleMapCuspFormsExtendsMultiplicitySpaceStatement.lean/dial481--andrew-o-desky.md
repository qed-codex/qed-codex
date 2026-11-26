---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/TwistedOperators/GKModuleMapCuspFormsExtendsMultiplicitySpaceStatement.lean",
  "declarations": [
    "GlobalTheory.T.gKModuleMapCuspForms_extends_multiplicitySpace"
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

## Extending a cuspidal map from compact-finite vectors

[Theorem REP.0868](https://andrewodesky.com/rh/lean/GlobalTheory.T.gKModuleMapCuspForms_extends_multiplicitySpace/)

Assume the Harish–Chandra-module and Casselman–Wallach packages specified below. Fix the full arithmetic unitary datum, compatible archimedean coordinates, a Hermitian space $V$, and a family of unitary discrete-series models $H_\tau$ for its infinite unitary groups. Let $H_{\tau,K}$ be their compact-finite vectors and $H_\tau^\infty$ the complex span of their smooth vectors. Put $G=U(V)(\mathbb A_F)$. Choose a set $J\subseteq G$, a function $\chi:G\to\mathbb C$, a Haar measure $\mu$, and a fundamental domain $\mathcal F$ for $U(V)(F)\backslash G$.

Let $T_0:\prod_\tau H_{\tau,K}\to\mathbb C^G$ be complex multilinear. Suppose every output is a smooth continuous automorphic cusp function, square integrable on $\mathcal F$, of uniform moderate growth, and satisfies $T_0(u)(gk)=\chi(k)T_0(u)(g)$ for $k\in J$. Suppose $T_0$ intertwines the maximal compact groups and infinitesimal Lie algebra actions in each argument with right translation and differentiation. Then there is a unique complex multilinear extension $$T:\prod_\tau H_\tau^\infty\longrightarrow\mathbb C^G$$ whose outputs are smooth automorphic cusp functions with the same transformation law, which intertwines the full infinite unitary groups in every argument and has the Sobolev continuity property below.
