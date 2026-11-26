---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/RingsOfIntegers/DvdOfAppEqZero.lean",
  "declarations": [
    "GlobalTheory.GermDiv.main"
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

## Divisibility of sections detected on all infinitesimal thickenings

[Theorem AG.0380](https://andrewodesky.com/rh/lean/GlobalTheory.GermDiv.main/)

Let $R$ be a noetherian domain and $I\subseteq\operatorname{Jac}(R)$ an ideal. Let $H\to\operatorname{Spec}R$ be a smooth group scheme with geometrically connected fibres, $N$ a line bundle on $H$, $s\in\Gamma(H,N)$, and $0\ne r\in R$. Put $H_n=H\times_R\operatorname{Spec}(R/I^{n+1})$. Suppose that for every $n\ge0$, every point $x\in H_n$, and every trivializing open of $N$ containing its image in $H$, the germ of $r$ divides the germ of the pulled-back local function representing $s$ in $\mathcal O_{H_n,x}$. Then there is $s'\in\Gamma(H,N)$ with $s=rs'$.
