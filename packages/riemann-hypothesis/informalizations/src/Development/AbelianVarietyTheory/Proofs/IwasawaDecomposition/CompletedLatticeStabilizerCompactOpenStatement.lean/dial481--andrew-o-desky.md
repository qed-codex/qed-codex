---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/CompletedLatticeStabilizerCompactOpenStatement.lean",
  "declarations": [
    "GlobalTheory.T.completedLattice_stabilizer_compact_open"
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

## Compact open stabilizer of a completed lattice

[Theorem ANT.1460](https://andrewodesky.com/rh/lean/GlobalTheory.T.completedLattice_stabilizer_compact_open/)

Let $E/F$ be an extension of number fields, $\sigma:E\to E$ an $F$-algebra homomorphism, $M\ge0$, and $J\in M_M(E)$. Let $L\subset E^M$ be a finitely generated $\mathcal O_E$-submodule spanning $E^M$. Put $$H=\{g\in\operatorname{GL}_M(\mathbb A_{F,f}\otimes_FE):\sigma(g)^T Jg=J\},$$ where $\sigma$ acts on the second tensor factor, and let $\widehat L$ be the completed lattice defined in ([Rational unitary approximation with an adelic lattice congruence](https://andrewodesky.com/rh/lean/GlobalTheory.T.unitaryGroup_weak_approximation_at_primes/)). There is a compact open subgroup $K\subseteq H$ satisfying $$g\in K\quad\Longleftrightarrow\quad (y\in\widehat L\ \Longleftrightarrow\ gy\in\widehat L\text{ for every }y).$$
