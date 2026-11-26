---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/WeilDeligneParamOfLadicRepTwistDetAwayFromLStatement.lean",
  "declarations": [
    "GlobalTheory.T.weilDeligneParamOfLadicRep_twist_det_awayFrom_l"
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

## Character twists of Weil–Deligne parameters away from the coefficient prime

[Theorem PHT.1115](https://andrewodesky.com/rh/lean/GlobalTheory.T.weilDeligneParamOfLadicRep_twist_det_awayFrom_l/)

Let $E$ be a number field, $\Omega$ an algebraic closure, $w$ a finite place, and $A\subseteq\Omega$ a valuation ring above $w$. Let $\ell$ be prime and different from the residue characteristic at $w$, and fix a field isomorphism $\iota:\overline{\mathbb Q}_\ell\simeq\mathbb C$. If $$\rho:G_E\to\operatorname{GL}_a(\overline{\mathbb Q}_\ell),\qquad\chi:G_E\to\operatorname{GL}_1(\overline{\mathbb Q}_\ell)$$ are continuous as matrix-valued maps, then their local Weil–Deligne parameters, constructed using $A$ and $\iota$, satisfy $$\operatorname{WD}_w(\rho\otimes\det\chi)=\operatorname{WD}_w(\rho)\otimes\operatorname{WD}_w(\chi).$$
