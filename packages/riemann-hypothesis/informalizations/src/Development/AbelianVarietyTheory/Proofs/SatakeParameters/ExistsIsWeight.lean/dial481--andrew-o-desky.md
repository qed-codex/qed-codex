---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/ExistsIsWeight.lean",
  "declarations": [
    "GlobalTheory.PolarizedWeight.exists_isWeight"
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

## Integral infinity weights and conjugation for polarized cusp forms

[Theorem AGR.0161](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Int.Row.exists_weights/)

Let $E$ be a CM field, $a\ge1$, $\ell$ prime, and $\iota:\overline{\mathbb Q}_\ell\simeq\mathbb C$. Let $\pi$ be a regular algebraic cuspidal representation of $\mathrm{GL}_a(\mathbb A_E)$ polarized by a Hecke character of the maximal totally real subfield.

There are an integer $w$ and multisets $J_\tau$ of integers, one for every embedding $\tau:E\to\overline{\mathbb Q}_\ell$, such that $$\{j:j\in J_\tau\}=\{(a-1)/2-z:z\in\operatorname{Inf}_{\iota\tau}(\pi)\},\qquad J_{\tau\circ c}=\{w-j:j\in J_\tau\}.$$ The first equality is in $\mathbb C$, using the usual embedding of $\mathbb Z$, and both equalities retain multiplicities. Here $c$ is complex conjugation on $E$. These multisets are defined without choosing a Galois representation or imposing local hypotheses.
