---
{
  "module": "src/CompanionTheory/AutomorphicTheory/BesselOrbitBounds/BesselMapUniqueness/BesselMapUniqGapAlt.lean",
  "declarations": [
    "CompanionTheory.Bmu.bounded"
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

## Bounded group orbits under a smooth Bessel map

[Theorem REP.0096](https://andrewodesky.com/rh/lean/CompanionTheory.Bmu.bounded/)

Let $k\ge1$, $r\ge0$, and $n=2r+k+1$. In $\mathbb C^n$ take the Hermitian matrix $H$ with $H_{i,n+1-i}=H_{n+1-i,i}=1$ for $1\le i\le r$, middle diagonal entries $+1$ in positions $r+1,\ldots,r+k$ and $-1$ in position $r+k+1$, and all other entries zero. Put $G=\{g:g^*Hg=H\}$. Let $z$ be supported in these middle positions with $\Re(z^tH\bar z)<0$, and let $c_1,\ldots,c_r\in\mathbb C^\times$.

Let $K\subset G$ fix $z$ and each of the first and last $r$ coordinate vectors. Let $N\subset G$ consist of matrices satisfying $g_{ia}=\delta_{ia}$ for $1\le a\le r$ and $i\ge a$, and $g_{ij}=\delta_{ij}$ for $r+1\le j\le r+k+1$ and $i\ge r+1$. Define $$\chi(g)=\exp\left(i\Re\sum_{a=1}^r c_a\ell_a(g)\right),\qquad \ell_a(g)=\begin{cases}g_{a,a+1}&a<r,\\(gz)_r&a=r.\end{cases}$$ The sum is empty when $r=0$.

Let $\sigma$ be a unitary action of $G$ on a complex Hilbert space $\mathcal H$, given by bounded complex-linear operators, with $\sigma(1)=1$, $\sigma(gh)=\sigma(g)\sigma(h)$ for $g,h\in G$. Let $T$ be a finite-dimensional complex inner product space, and let $\pi(h)\in\operatorname{End}_{\mathbb C}(T)$ for $h\in K$ be a continuous family of norm-preserving operators with $\pi(1)=1$. Suppose $B:\mathcal H\to T$ is complex-linear on the smooth vectors, is bounded there by a finite sum of Lie-derivative seminorms, and satisfies $$B(\sigma(hm)v)=\chi(m)\pi(h)B(v)\qquad(h\in K,\ m\in N,\ v\in\mathcal H^\infty).$$ Then for every $w\in\mathcal H^\infty$ there is $C_w\in\mathbb R$ such that $$\|B(\sigma(g)w)\|\le C_w\qquad(g\in G).$$
