---
{
  "module": "src/ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/InterDivSupp.lean",
  "declarations": [
    "ReciprocityTheory.ChartRestriction.G.Geo.divSuppArith"
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

## Horizontal and vertical components of an arithmetic divisor

[Theorem ARAK.1373](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Geo.divSuppArith/)

Let $B$ be a finite nonempty set of finite coordinate blocks $I_b$, and put $R=\mathbb Z[X_{b,i}]$. Let $P\subset R$ be a relevant multihomogeneous prime with $P\cap\mathbb Z=0$ and $$\dim(R/P)=n+1+|B|,\qquad n\ge0.$$ Relevant means that no coordinate block lies entirely in the ideal. Fix a Hermitian multidegree datum $\overline A$ of degree $(a_b)$, consisting of integers $a_b$ and a real function $h$ on the complex coordinate space, positive when every block is nonzero and satisfying $h((c_bz_b)_b)=\prod_b|c_b|^{a_b}h(z)$ whenever every $c_b\ne0$, and a polynomial $s\notin P$ homogeneous of multidegree $(a_b)$, with all $a_b\ge0$. Let $W$ be a relevant minimal prime of $P+(s)$.

If $W\cap\mathbb Z=0$, then $W$ is a relevant multihomogeneous horizontal prime with $\dim(R/W)=n+|B|$. Otherwise $W$ is a relevant multihomogeneous prime, its quotient has prime characteristic, and again $$\dim(R/W)=n+|B|.$$
