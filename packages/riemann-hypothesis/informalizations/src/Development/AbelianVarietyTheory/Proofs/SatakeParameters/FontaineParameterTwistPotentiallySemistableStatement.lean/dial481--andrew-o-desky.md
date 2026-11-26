---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/FontaineParameterTwistPotentiallySemistableStatement.lean",
  "declarations": [
    "GlobalTheory.T.fontaineParameter_twist_potentiallySemistable"
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

## Character twists of Fontaine parameters

[Theorem PHT.1579](https://andrewodesky.com/rh/lean/GlobalTheory.T.fontaineParameter_twist_potentiallySemistable/)

Let $\ell$ be prime and choose local crystalline, de Rham and integral period data compatibly identified with Fontaine's rings as in ([An invariant crystalline period matrix for an unramified representation](https://andrewodesky.com/rh/lean/GlobalTheory.UnrPer.exists_period_unramified/)). Choose a field isomorphism $\iota:\overline{\mathbb Q}_\ell\simeq\mathbb C$. Let $E$ be a number field, $\Omega$ an algebraic closure of $E$, and $A\subset\Omega$ a valuation ring above a finite place $w$ of $E$. Choose a local place-comparison datum identifying the decomposition group $D_A$ with the absolute Galois group of the completion, and inducing the valuation ring $A$.

Let $a\ge0$ and let $r:D_A\to\operatorname{GL}_a(\overline{\mathbb Q}_\ell)$ and $c:D_A\to\operatorname{GL}_1(\overline{\mathbb Q}_\ell)$ be continuous matrix-valued representations. Assume $r$, $c$, and the scalar twist $r\otimes\det c$ are all potentially semistable for the chosen data. Their associated complex Weil–Deligne parameters satisfy $$\operatorname{WD}_\iota(r\otimes\det c)=\operatorname{WD}_\iota(r)\otimes\operatorname{WD}_\iota(c).$$
