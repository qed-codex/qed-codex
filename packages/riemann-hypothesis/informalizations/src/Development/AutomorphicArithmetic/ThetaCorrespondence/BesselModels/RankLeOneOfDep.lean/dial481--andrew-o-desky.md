---
{
  "module": "src/Development/AutomorphicArithmetic/ThetaCorrespondence/BesselModels/RankLeOneOfDep.lean",
  "declarations": [
    "UpperTheory.Lit.Bur.BurPos.frame_normal"
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

## A Hermitian frame in split normal form

[Theorem ALG.1179](https://andrewodesky.com/rh/lean/UpperTheory.Lit.Bur.BurPos.frame_normal/)

Let $m,r\ge0$ and $n=2r+m+1$. Let $J\in M_n(\mathbb C)$ be invertible Hermitian, $J_0\in M_m(\mathbb C)$ invertible, $F\in M_{n,m}(\mathbb C)$, $e\in M_{n,r}(\mathbb C)$, and $z\in\mathbb C^n$. Assume $$F^*JF=J_0,\quad e^*Je=0,\quad F^*Je=0,\quad F^*Jz=e^*Jz=0,$$ that the columns of $e$ are linearly independent, that $\operatorname{Re}(z^*Jz)<0$, and that $\operatorname{Re}(x^*J_0x)>0$ for every $x\ne0$.

In the ordered coordinate basis $(u_1,\ldots,u_r,w_1,\ldots,w_m,w_-,v_r,\ldots,v_1)$, let $H$ pair $u_i$ with $v_i$ with value $1$, give each $w_j$ norm $1$ and $w_-$ norm $-1$, and have all other pairings zero. Let $E_0,W_0$ be the matrices with columns $u_i,w_j$, respectively. There exist $Q\in\operatorname{GL}_n(\mathbb C)$, $A\in\operatorname{GL}_m(\mathbb C)$, and $t>0$ such that $$A^*J_0A=1,\quad Q^*JQ=H,\quad QE_0=e,\quad QW_0=FA,\quad Q(tw_-)=z.$$
