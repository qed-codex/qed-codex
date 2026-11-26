---
{
  "module": "src/Formalism/LocalToGlobal/CharacterGerms/RowTiePHaLeaves.lean",
  "declarations": [
    "Formalism.L2.FormalSeriesBounds.HaP.satRetr"
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

## A retraction onto a saturated integral submodule

[Theorem ALG.0897](https://andrewodesky.com/rh/lean/Formalism.L2.FormalSeriesBounds.HaP.satRetr/)

Let $I$ be a finite set and $W\subseteq\mathbb Z^I$ a submodule. Suppose that, for every nonzero $a\in\mathbb Z$ and $x\in\mathbb Z^I$, $ax\in W$ implies $x\in W$. There is a $\mathbb Z$-linear map $\rho:\mathbb Z^I\to\mathbb Z^I$ with $$\rho(x)\in W\quad(x\in\mathbb Z^I),\qquad \rho(x)=x\quad(x\in W).$$
