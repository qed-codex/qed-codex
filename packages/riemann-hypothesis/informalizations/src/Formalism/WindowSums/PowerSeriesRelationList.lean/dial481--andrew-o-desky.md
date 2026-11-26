---
{
  "module": "src/Formalism/WindowSums/PowerSeriesRelationList.lean",
  "declarations": [
    "Formalism.WindowSums.arc_WindowSum",
    "Formalism.WindowSums.arc_ZpowVal"
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

## Valuation of a nonzero integer power of a principal unit

[Theorem PHT.0958](https://andrewodesky.com/rh/lean/Formalism.WindowSums.arc_ZpowVal/)

Let $\ell$ be prime, $u\in\mathbb Z_\ell^\times$, and $s\in\mathbb N$ with $s\ge1$. If $\ell=2$, assume also $s\ge2$. Normalize $v_\ell(\ell)=1$ and suppose $v_\ell(u-1)=s$. For every nonzero integer $j$, $$u^j-1\ne0,\qquad v_\ell(u^j-1)=s+v_\ell(j).$$

## A bound for the sum of prime-adic valuations in an interval

[Theorem ANT.0993](https://andrewodesky.com/rh/lean/Formalism.WindowSums.arc_WindowSum/)

Let $\ell$ be prime, $a\in\mathbb Z$, $L,D\ge0$ integers, and $S\subseteq\mathbb Z\cap[a,a+L)$ a finite set with $0\notin S$ and $|s|\le D$ for every $s\in S$. Then $$\sum_{s\in S}v_\ell(s)\le\frac{L}{\ell-1}+\log_\ell D.$$
