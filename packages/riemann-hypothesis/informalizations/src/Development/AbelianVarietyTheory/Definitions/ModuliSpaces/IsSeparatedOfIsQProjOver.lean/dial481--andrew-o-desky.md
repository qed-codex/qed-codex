---
{
  "module": "src/Development/AbelianVarietyTheory/Definitions/ModuliSpaces/IsSeparatedOfIsQProjOver.lean",
  "declarations": [
    "GlobalTheory.ZM.SFam"
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

## Siegel moduli families and their level pairing

[Definition / hypothesis AV.D084](https://andrewodesky.com/rh/lean/GlobalTheory.ZM.SFam/)

Fix integers $g\ge0$ and $n\ge1$, and put $$R_n=\mathbb Z[\zeta_n,1/n]\subseteq\mathbb C,\qquad \zeta_n=e^{2\pi i/n},\qquad V_g=\mathbb Z^g\oplus\mathbb Z^g.$$ Write $$\omega(a,b)=\sum_{i=1}^g(a_i b_{g+i}-a_{g+i}b_i)\qquad(a,b\in V_g).$$

A level-$n$ family over an $R_n$-scheme $T$ consists of a commutative abelian scheme $A/T$, a line bundle $P$ on $A\times_T A$, and an additive map $\ell:V_g\to A(T)$. The restrictions of $P$ to $\{0\}\times_T A$ and $A\times_T\{0\}$ are trivial, and interchanging the two factors carries $P$ to an isomorphic line bundle. Put $L=\Delta_A^*P$.

The level map is killed by $n$. At every algebraically closed field-valued point $x:\operatorname{Spec}K\to T$, its specialization has kernel $nV_g$ and image $A_x(K)[n]$. For all $a,b\in V_g$, require the theta-group Weil commutator $$e_{L_x,n}(\ell_x(a),\ell_x(b))=\zeta_{n,x}^{\,2\omega(a,b)},$$ where $\zeta_{n,x}\in K^\times$ is the image of $\zeta_n$ and the commutator convention is specified below. A pullback identification of level families is a group-scheme pullback identification that identifies their double-product line bundles and their level maps.

The family is called **principally polarized** when $L$ is relatively ample and the following trivial-kernel condition holds: for every $T$-scheme $T'$ and every $a\in A(T')$, if the line bundle $P(a,-)$ on $A_{T'}$ is trivial, then $a=0$.

A **Siegel moduli family** of type $(g,n)$ is an $R_n$-scheme $U$, smooth and quasiprojective of relative dimension $g(g+1)/2$, with a principally polarized level-$n$ family over $U$, satisfying these two properties:

- For every reduced $R_n$-scheme $T$ whose generic fibre is dense in $T$, every principally polarized level-$n$ family over $T$ has a pullback identification with the family over $U$ along some $R_n$-morphism $T\to U$.
- For every commutative local ring $B$, two $R_n$-morphisms $f,h:\operatorname{Spec}B\to U$ are equal whenever their pulled-back level-$n$ families have a pullback identification with the same level-$n$ family over $\operatorname{Spec}B$.
