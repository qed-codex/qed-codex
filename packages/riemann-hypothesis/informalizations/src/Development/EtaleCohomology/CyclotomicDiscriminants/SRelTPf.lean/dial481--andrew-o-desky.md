---
{
  "module": "src/Development/EtaleCohomology/CyclotomicDiscriminants/SRelTPf.lean",
  "declarations": [
    "LateralTheory.Q.SRelT.gen_two",
    "LateralTheory.Q.SRelT.rel_bd"
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

## A generator bound for even homology of two cyclic groups

[Theorem ALG.0371](https://andrewodesky.com/rh/lean/LateralTheory.Q.SRelT.gen_two/)

Let $q\ge1$ and $r,e\ge0$ be integers, and let $C_q$ be a cyclic group of order $q$. With trivial action on $\mathbb Z/r\mathbb Z$, the abelian group $$H_{2e}(C_q\times C_q,\mathbb Z/r\mathbb Z)$$ is a quotient of a finite free abelian group of rank at most $2e+1$.

## An integral relation among more cycles than homology generators

[Theorem GC.0925](https://andrewodesky.com/rh/lean/LateralTheory.Q.SRelT.rel_bd/)

Let $k$ be a commutative ring, $G$ a group, and $m,r\ge0$. Suppose the abelian group $H_{m+1}(G,k)$, with trivial $G$-action on $k$, is a quotient of a finite free abelian group of rank at most $r$. Given $r+1$ cycles $z_0,\ldots,z_r$ in the inhomogeneous group chain complex $C_{m+1}(G,k)$ and any integer $\ell\ge2$, there are integers $n_0,\ldots,n_r$, at least one not divisible by $\ell$, for which $$\sum_{i=0}^r n_i z_i$$ is a boundary. The integer coefficients act through $\mathbb Z\to k$.
