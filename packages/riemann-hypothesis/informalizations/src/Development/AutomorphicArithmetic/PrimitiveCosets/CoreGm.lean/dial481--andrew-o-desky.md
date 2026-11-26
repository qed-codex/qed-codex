---
{
  "module": "src/Development/AutomorphicArithmetic/PrimitiveCosets/CoreGm.lean",
  "declarations": [
    "UpperTheory.Comparison₂.core_gm"
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

## Weighted prime-sum bound

[Theorem ANT.1.0102](https://andrewodesky.com/rh/lean/UpperTheory.Comparison%E2%82%82.core_gm/)

Let $\mathcal K$ be a finite set of primitive Dirichlet characters that contains the principal character $1$ of modulus $1$ and, with every $\chi$, its conjugate $\overline\chi$. Let $o\ge0$ be an integer. Either let $\xi\in\mathcal K$ be an odd real-valued character, or let no such character be chosen. Let $G_{\mathcal K}$ be the weighted sum of smoothed character sums that the introduction attaches to $\mathcal K$, $\xi$ and $o$. Let $E_D,E_P$ be real numbers and let $\varepsilon>0$.

1. Let $K,C_*,e_K,C$ be real numbers. There is a real number $x_1\ge1$ with the following property. Let $x\ge x_1$, let a group $A$, a number field $E$ and the further data of Hypothesis (abelian CM field with reciprocity map) of ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)) be given and satisfy that hypothesis, and let $T\subseteq A$. Suppose that both hypotheses of ([Character and counting conditions at a single scale](https://andrewodesky.com/rh/lean/Formalism.HC.EAtH/)) hold for these data and $T$ at $x$: Hypothesis (character conditions) for $\mathcal K,\xi,o$ with constants $\varepsilon,C$, and Hypothesis (counting conditions) with constants $\varepsilon,E_D,E_P,K,C_*,e_K$. Then $$G_{\mathcal K}(x)\le x^{1/2+(E_D+E_P+7)\varepsilon}.$$
2. Let $\mathcal F$ be an arithmetic family with exponent $\varepsilon$, as in ([Arithmetic families with local and theta data](https://andrewodesky.com/rh/s/family-arithmetic-data.html)), with member sets $I_x$ and set of occupied scales $\mathcal W$. Suppose that the following two conditions hold.

(a) There are real numbers $C$ and $x_0\ge1$ such that, for every $x\ge x_0$ and every member $i\in I_x$, Hypothesis (character conditions) of ([Character and counting conditions at a single scale](https://andrewodesky.com/rh/lean/Formalism.HC.EAtH/)) holds at $x$, with constants $\varepsilon,C$, for $\mathcal K,\xi,o$ and for the group, the field and the set $T$ of the member $i$.

(b) There are real numbers $K,C_*,e_K,C_L$ and $x_0\ge1$ such that, for every $x\in\mathcal W$ with $x\ge x_0$, the family $\mathcal F$ has tied counting data at $x$ with constants $E_D,E_P,K,C_*,e_K,C_L$, as defined in ([Counting data tied to an arithmetic family](https://andrewodesky.com/rh/lean/Formalism.MainNotions.ChainTied/)).

Then there is a real number $x_1\ge1$ such that $$G_{\mathcal K}(x)\le x^{1/2+(E_D+E_P+7)\varepsilon}\qquad\text{for every }x\in\mathcal W\text{ with }x\ge x_1.$$
