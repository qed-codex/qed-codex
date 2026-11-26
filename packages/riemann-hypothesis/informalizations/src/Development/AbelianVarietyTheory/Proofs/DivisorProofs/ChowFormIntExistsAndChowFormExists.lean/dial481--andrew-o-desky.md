---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ChowFormIntExistsAndChowFormExists.lean",
  "declarations": [
    "GlobalTheory.ChowExists.exists_isChowFormInt"
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

## Existence of a Chow form

[Theorem AG.1671](https://andrewodesky.com/rh/lean/GlobalTheory.ChowExists.exists_isChowFormInt/)

Let $K$ be a field of characteristic zero, $N,D\ge0$, and $P\subset K[x_1,\ldots,x_N]$ a homogeneous prime ideal with $$\dim K[x_1,\ldots,x_N]/P=D+1.$$ Write $\delta$ for its Hilbert degree. There is an irreducible polynomial $F\in K[u_{ij}:0\le i\le D,\ 1\le j\le N]$, homogeneous of degree $\delta$ in each block $(u_{ij})_j$, such that for every matrix $u$ over an algebraic closure $\overline K$, $$F(u)=0\ \Longleftrightarrow\ \exists y\in\overline K^N\setminus\{0\}:\quad f(y)=0\ (f\in P),\quad \sum_{j=1}^N u_{ij}y_j=0\ (0\le i\le D).$$
