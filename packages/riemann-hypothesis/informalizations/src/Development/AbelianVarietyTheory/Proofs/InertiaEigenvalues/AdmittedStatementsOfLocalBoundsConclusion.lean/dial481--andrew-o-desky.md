---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/AdmittedStatementsOfLocalBoundsConclusion.lean",
  "declarations": [
    "GlobalTheory.NLink.admittedStatements_of_localBoundsConclusion"
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

## Uniform construction of local congruence tables

[Theorem GC.0020](https://andrewodesky.com/rh/lean/GlobalTheory.NLinkClose.main_alt_alt/)

Let $0<\varepsilon<1/52$ and assume ([Arithmetic families with local and theta data](https://andrewodesky.com/rh/s/family-arithmetic-data.html)). Assume ([Integral twisting conditions for arithmetic families](https://andrewodesky.com/rh/lean/Formalism.MainNotions.TwIn/)), the local cohomology hypothesis and the normalized Galois, integral congruence matrix and paired-character hypotheses below, with constants $C\ge0$ and $C_T\in\mathbb Z_{\ge0}$. Assume also the uniform bound at residue primes $2,3$ below.

There exist $C_a\ge0$ and $x_a\in\mathbb R$ such that for every $x\ge x_a$ above the family's original threshold, every member of $\mathcal F$ at $x$, and the hypothesis that $\operatorname{length}_{\mathbb Z_\ell}\mathcal K_{\ell,a}$ is finite for every prime $\ell$ and $1\le a<t$, with $\mathcal K_{\ell,a}$ defined in ([Local congruence tables](https://andrewodesky.com/rh/lean/Formalism.MainNotions.TwistedPlaces.AdmT/)), there is a table satisfying all the conditions of ([Local congruence tables](https://andrewodesky.com/rh/lean/Formalism.MainNotions.TwistedPlaces.AdmT/)) with constant $C_a$. The constant and threshold are chosen before the member and before the finiteness hypothesis.
