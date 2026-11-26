---
{
  "module": "src/CompanionTheory/AutomorphicTheory/HeckeStandardModules/InvMemRl.lean",
  "declarations": [
    "ReciprocityTheory.ChartRestriction.L3H.heckeStd"
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

## Standard split Hecke operators and integrality away from the residue prime

[Theorem AGR.1514](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.L3H.heckeStd/)

Let $L$ be a CM number field, $F=L^+$, $n\ge0$, and $G=U_n$ for the standard Hermitian form over $L/F$. Let $W$ be a complex representation of $G(F)$ of algebraic weight: it is finite-dimensional and its matrix entries in some basis are polynomials in the matrix entries of rational group elements at all embeddings $L\hookrightarrow\mathbb C$. Take a subgroup $J\subset G(\mathbb A_{F,f})$, a character $\chi:J\to\mathbb C^\times$, and a set $B$ of finite places. Assume that for some integer $N>0$, every element of the standard maximal compact subgroup congruent to $1$ modulo $N$ belongs to $\ker\chi$. Also assume that for every element supported outside $B$, membership in $J$ is equivalent to membership in the standard maximal compact subgroup, and $\chi$ is trivial on those elements of $J$.

Let $\mathcal A(J,\chi,W)$ consist of functions $f:G(\mathbb A_{F,f})\to W$ invariant on the right under some principal congruence subgroup and satisfying $f(\gamma g)=\gamma f(g)$ for $\gamma\in G(F)$ and $f(gj)=\chi(j)f(g)$. Let $v\notin B$ be split in $L$, choose one splitting and a uniformizer $\varpi_v$, and let $1\le k\le n$. Let $D_{v,k}$ consist of elements supported at $v$ whose split component lies in the standard integral double coset of $\operatorname{diag}(\varpi_v,\ldots,\varpi_v,1,\ldots,1)$ with $k$ copies of $\varpi_v$. Define $$T_{v,k}f(g)=q_v^{-k(n-1)}\sum_{c\in D_{v,k}/J} f(gc),$$ where the sum is over the right $J$-cosets meeting $D_{v,k}$. Then $T_{v,k}$ preserves $\mathcal A(J,\chi,W)$ and is complex-linear there. All these operators commute, including different splittings or uniformizers. If $0\ne f\in\mathcal A(J,\chi,W)$ and $T_{v,k}f=\mu f$, then for every rational prime $\ell$ not below $v$ there is an integer $d\ge0$ with $\ell\nmid d$ such that $d\mu$ is an algebraic integer.
