---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/AdelicLatticeProofs/MovedOfSplitPl.lean",
  "declarations": [
    "GlobalTheory.UnRep.FullReps.exists_nat_bd"
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

## Clearing adelic matrix denominators away from prescribed primes

[Theorem ANT.0616](https://andrewodesky.com/rh/lean/GlobalTheory.UnRep.FullReps.exists_nat_bd/)

Let $F\subseteq E$ be number fields and put $R=\mathbb A_{F,f}\otimes_FE$. Let $L\subseteq E^n$ be a finitely generated $\mathcal O_E$-submodule spanning $E^n$. Let $N\ge0$, $e\in\mathbb A_{F,f}$, and $M\in M_n(R)$ satisfy $$e_v=0\quad\text{if }N\in\mathfrak p_v,\qquad (e\otimes1)(M-1)=M-1.$$ There exists an integer $t\ge0$, coprime to $N$, such that $$(1\otimes t)M\widehat L\subseteq\widehat L.$$
