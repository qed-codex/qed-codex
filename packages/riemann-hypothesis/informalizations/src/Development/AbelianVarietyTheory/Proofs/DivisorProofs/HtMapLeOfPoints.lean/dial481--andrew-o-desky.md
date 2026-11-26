---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/HtMapLeOfPoints.lean",
  "declarations": [
    "GlobalTheory.DescentFamily.descent"
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

## Descent of a slope bound through several maps

[Theorem ARAK.1119](https://andrewodesky.com/rh/lean/GlobalTheory.DescentFamily.descent/)

Let $K$ be a totally complex number field and $A\ne0$, $B$ be finitely generated $\mathcal O_K$-modules in finite-dimensional $K$-spaces with Hermitian norms at every embedding. Assume the norm families arise from invertible Hermitian Gram matrices. Fix real numbers $P,t$ and $\Lambda,\varepsilon\ge0$. Let $\varphi_h:A\otimes K\to B\otimes K$ for $1\le h\le n$ be jointly injective and integral on $A$. Suppose $$\sum_{h=1}^n\|\varphi_hx\|_\sigma^2\le e^{2P}\|x\|_\sigma^2$$ at every embedding $\sigma$, for every $x$, and suppose $B$ is spanned over $K$ by elements of $B$ of norm at most $e^\Lambda$ at all embeddings. Assume $$n\operatorname{rk}B\le(1+\varepsilon)\operatorname{rk}A,\qquad t\le\mu(A)-2P.$$ Then $$\mu(B)\ge t-\varepsilon(|t|+2\Lambda).$$ For a nonzero lattice $L$, put $r_L=\operatorname{rk}_{\mathcal O_K}L$ and let $C(L)$ be its Euclidean covolume using one embedding from each complex-conjugate pair. The normalization is $$\operatorname{covol}_{\mathrm{norm}}(L)=2^{[K:\mathbb Q]r_L/2}|\operatorname{disc}K|^{-r_L/2}C(L),\qquad \mu(L)=-\frac{2\log\operatorname{covol}_{\mathrm{norm}}(L)}{[K:\mathbb Q]r_L}.$$
