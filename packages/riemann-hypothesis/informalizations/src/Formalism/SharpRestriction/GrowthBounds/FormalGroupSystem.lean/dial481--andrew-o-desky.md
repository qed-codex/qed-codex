---
{
  "module": "src/Formalism/SharpRestriction/GrowthBounds/FormalGroupSystem.lean",
  "declarations": [
    "Formalism.MainNotions.FormalGroupSystem.ExpansionEquality"
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

## A finite expansion of a transition operator by theta kernels

[Definition / hypothesis PHT.D109](https://andrewodesky.com/rh/lean/Formalism.MainNotions.FormalGroupSystem.ExpansionEquality/)

Fix a prime $p$, a local formal-group system with its theta data, and a stage $j\in\mathbb N$. Write $K$ for its coefficient field, $C$ for the extension field of the theta data, $\iota:K\to C$ for the given map, and $O_C\subset C$ for its valuation ring. At stage $j$, let $\mathcal F_j^0$ be the integral module of polynomial-valued functions on pairs $(c,L)$ of a component and a tuple of local submodules, and put $\mathcal F_j=\operatorname{span}_K\mathcal F_j^0$. Let $A_j:\mathcal F_j^{\mathrm{all}}\to\mathcal F_{j+1}^{\mathrm{all}}$ be the supplied transition operator on all such functions.

The kernel-expansion condition at stage $j$ is the following assertion. There is $a\in C$ with $a,a^{-1}\in O_C$ such that, for every $F\in\mathcal F_j$, every component $c'$ at stage $j+1$ and every tuple $L'$ of lattices there, $$\iota_*\bigl((A_jF)(c',L')\bigr)=\sum_{(c,L)\in\mathcal R_j}\frac{a}{s_j(c,L)}\,\mathscr K_j\bigl((c,L),(c',L')\bigr)\bigl(F(c,L)\bigr).$$ Here $\iota_*$ applies $\iota$ to polynomial coefficients, $\mathcal R_j$ is the specified finite set of component–lattice pairs, and $s_j(c,L)$ is the cardinality of the subgroup of the component's arithmetic group fixing $L$.
