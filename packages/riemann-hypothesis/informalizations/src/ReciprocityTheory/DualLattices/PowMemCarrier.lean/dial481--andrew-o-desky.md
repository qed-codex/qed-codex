---
{
  "module": "src/ReciprocityTheory/DualLattices/PowMemCarrier.lean",
  "declarations": [
    "ReciprocityTheory.PGsh.Up.u4"
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

## A determinant-colength bound for a Hopf order

[Theorem PHT.0249](https://andrewodesky.com/rh/lean/ReciprocityTheory.PGsh.Up.u4/)

Let $p$ be prime, $C$ an algebraically closed field of characteristic zero, and $v:C\to\mathbb R_{\ge0}$ a multiplicative valuation. Identify a commutative ring $R$ with its valuation ring $\{x\in C:v(x)\le1\}$, and assume $v(p)<1$. Let $N$ be a finite abelian group killed by $p$, and let $A\subseteq C^N$ be a Hopf order as specified below. Write $I=\{f\in A:f(0)=0\}$ and $\omega_A=I/I^2$.

Suppose $A$ is spanned over $R$ by the columns of a matrix $B\in M_N(C)$, and put $c=v(\det B)$. If there are $r\ge0$ and $a_1,\ldots,a_r\in R$ with $$\omega_A\simeq\bigoplus_{i=1}^r R/(a_i),\qquad b=\prod_{i=1}^r v(a_i),$$ then $$c^2\le b^{|N|}.$$
