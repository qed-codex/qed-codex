---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/FoundationProofs/ExistsCmIdempotentsSelectConjugatePrimes.lean",
  "declarations": [
    "GlobalTheory.SelectIdem.exists_select_idem"
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

## Compatible idempotents selected by conjugate primes

[Theorem ANT.1162](https://andrewodesky.com/rh/lean/GlobalTheory.SelectIdem.exists_select_idem/)

Assume ([Identifications for arithmetic family members](https://andrewodesky.com/rh/lean/Formalism.MainNotions.N.LocTie/)), with CM field $E$ and conjugation $c$. For a rational prime $q$, let $I(q)$ mean that every nonzero prime ideal of $\mathcal O_E$ above $q$ is fixed by $c$. There exists a sequence $e_N\in\mathcal O_E$, indexed by $N\ge0$, such that, for $N,m\ge1$, $$e_{Nm}\equiv e_N\pmod N,\qquad e_N^2\equiv e_N\pmod N,\qquad e_Nc(e_N)\equiv0\pmod N.$$ For every rational prime $q$ and $k\ge0$, $$e_{q^k}+c(e_{q^k})\equiv\begin{cases}0&I(q),\\1&\neg I(q)\end{cases}\pmod{q^k}.$$
