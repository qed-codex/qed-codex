---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/FoundationProofs/CupProductCoboundaryModStatement.lean",
  "declarations": [
    "GlobalTheory.T.cup_product_coboundary_mod"
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

## A cup product is a coboundary when either factor is

[Theorem GC.0681](https://andrewodesky.com/rh/lean/GlobalTheory.T.cup_product_coboundary_mod/)

Let $l$ be prime, $\Omega/\mathbb Q$ an algebraic closure, $G=\operatorname{Gal}(\Omega/\mathbb Q)$, and $\epsilon:G\to\overline{\mathbb Q}_l^\times$ the cyclotomic character. Let $O\subset\overline{\mathbb Q}_l$ be a $\mathbb Z_l$-subalgebra which is a discrete valuation ring finite over $\mathbb Z_l$. Let $n\ge0$, $H\le G$, and $W:G\to\operatorname{GL}_2(\overline{\mathbb Q}_l)$ be continuous, with all matrix entries in $O$ and $(\det W)^2=1$. Put $W^\dagger=W\otimes(\epsilon(\det W)^{-1})$ and $\omega(x,y)=x_1y_2-x_2y_1$.

Let $a,b:G\to\overline{\mathbb Q}_l^2$ take values in $O^2$, be continuous on $H$, and satisfy on $H$ $$a(st)\equiv a(s)+W(s)a(t),\qquad b(st)\equiv b(s)+W^\dagger(s)b(t).$$ Suppose either $a(s)\equiv W(s)x-x$ for some $x\in O^2$, or $b(s)\equiv W^\dagger(s)x-x$ for some $x\in O^2$, for every $s\in H$. Then there is $u:G\to O$, continuous on $H$, such that for $s,t\in H$, $$\omega(a(s),W^\dagger(s)b(t)) \equiv\epsilon(s)u(t)-u(st)+u(s).$$
