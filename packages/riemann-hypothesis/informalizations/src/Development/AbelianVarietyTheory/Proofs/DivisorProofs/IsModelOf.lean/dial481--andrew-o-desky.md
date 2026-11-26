---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/IsModelOf.lean",
  "declarations": [
    "GlobalTheory.ImageModel.IsModelOf"
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

## Arithmetic image models and Hermitian metrics

[Definition / hypothesis ARAK.D005](https://andrewodesky.com/rh/lean/GlobalTheory.ImageModel.IsModelOf/)

Let $K$ be a number field, let $X$ be an integral scheme, and let $p:X\to\operatorname{Spec}\mathcal O_K$ be a morphism. Write $K(X)$ for its function field and $X_\sigma(\mathbb C)$ for its complex points at an embedding $\sigma:K\hookrightarrow\mathbb C$.

**Hermitian metrics.** Present a line bundle $\mathscr L$ by an open cover $(U_i)_{i\in I}$ and units $g_{ij}$ on $U_i\cap U_j$, with $g_{ii}=1$ and $g_{ij}g_{jk}=g_{ik}$ on triple intersections. A section $s$ is represented by regular functions $s_i$ on $U_i$ satisfying $s_i=g_{ij}s_j$ on overlaps.

For every $\sigma$ and $i$, choose a real-valued function $\phi_{\sigma,i}$ on all of $X_\sigma(\mathbb C)$. On the overlaps require $$\phi_{\sigma,j}(y)=\phi_{\sigma,i}(y)-\log|g_{ij}(y)|^2.$$ At every point of $U_i(\mathbb C)$, the function $\phi_{\sigma,i}$ must locally be a smooth real function of finitely many regular functions: on a Zariski-open neighborhood choose $a_1,\ldots,a_r$ and a smooth real function $F$ on an open subset of $\mathbb C^r$, and require $\phi_{\sigma,i}(z)=F(a_1(z),\ldots,a_r(z))$ near that point. Require also $$\phi_{\bar\sigma,i}(\bar y)=\phi_{\sigma,i}(y)\qquad(y\in U_i(\mathbb C)).$$ Here $\bar y$ is the conjugate complex point, over $\bar\sigma$. These data give the pointwise norm $$\|s(y)\|_\sigma^2=|s_i(y)|^2\exp(-\phi_{\sigma,i}(y))\qquad(y\in U_i(\mathbb C)).$$

For $t\in\mathbb R$, write $\overline{\mathscr L}(t)$ for the same line bundle with every $\phi_{\sigma,i}$ replaced by $\phi_{\sigma,i}+2t$. For $h\in\mathbb N$, a small section of $\overline{\mathscr L}(t)^{\otimes h}$ is a section $s\in H^0(X,\mathscr L^{\otimes h})$ such that $$\|s(y)\|_{\sigma,\mathscr L^{\otimes h}}\le\exp(ht)\qquad(\sigma:K\hookrightarrow\mathbb C,\ y\in X_\sigma(\mathbb C)),$$ where the norm on the left is the unshifted tensor-power norm.

**Metrics from generating sections.** Let $r\in\mathbb N$ and let $b_0,\ldots,b_{r-1}$ be sections of $\mathscr L$ whose nonvanishing loci cover $X$. For every ring homomorphism $\tau:\mathcal O_K\to\mathbb C$, choose $A_\tau\in\mathrm{GL}_r(\mathbb C)$. For each $\tau$, require a unitary matrix $U_\tau$ such that $$A_{\bar\tau}=\overline{A_\tau}U_\tau,\qquad \bar\tau(a)=\overline{\tau(a)}.$$ The Fubini–Study metric defined by these sections and matrices has local potentials $$\phi_{\tau,i}(y)=\log\left(\sum_{a=0}^{r-1}\left|\sum_{j=0}^{r-1}(A_\tau)_{ja}b_{j,i}(y)\right|^2\right),$$ where $b_{j,i}$ is the local coefficient of $b_j$ on $U_i$, extended by zero outside $U_i$. Thus $\phi_{\tau,i}=0$ outside $U_i$. On projective space $\mathbb P^N_{\mathcal O_K}$, use the coordinate sections of $\mathcal O(1)$: on $U_i=\{X_i\ne0\}$ their local coefficients are $b_{j,i}=X_j/X_i$, for $0\le j\le N$. Restriction along a morphism pulls back the line bundle and these metric potentials.

**Models of linear evaluations.** Let $V$ be a $K$-vector space with a compatible $\mathcal O_K$-module structure, let $W\subseteq V$ be an $\mathcal O_K$-submodule, and let $\Omega$ be a field containing $K$. Choose a $K$-linear map $\operatorname{ev}:V\to\Omega$, a family of functions $\mathcal N=(N_\sigma:V\to\mathbb R)_\sigma$, a natural number $D$, a field homomorphism $\psi:\Omega\to K(X)$ and a map $$s:W\longrightarrow H^0(X,\mathscr L).$$ These data form an arithmetic image model if the following conditions hold.

- The scheme $X$ is projective over $\mathcal O_K$, flat over $\mathbb Z$, normal, and has absolute dimension $D+1$.
- The map $\psi$ is bijective. For every $a\in\mathcal O_K$, $\psi(a)$ is the rational function obtained by pulling back $a$ along $p$.
- For every $w,w'\in W$ and every chart $U_i$ containing the generic point of $X$, the local coefficients, viewed as rational functions, satisfy $$\psi(\operatorname{ev}(w))\,s(w')_i=\psi(\operatorname{ev}(w'))\,s(w)_i.$$
- The nonvanishing loci of the sections $s(w)$, for $w\in W$, cover $X$.
- There is a frame $(b,g,A)$ for $(\mathcal N,W)$ in ([Image degrees and Chow heights of linear evaluations](https://andrewodesky.com/rh/lean/GlobalTheory.CompHt.imageIdeal/)). If $N$ is its basis length and $n$ its number of integral generators, put $\ell_k=\sum_jg_{jk}b_j\in W$. There is a matrix $c\in M_{n\times N}(K)$ with $$b_j=\sum_{k=0}^{n-1}c_{kj}\ell_k\qquad(0\le j<N).$$ For every embedding $\sigma$, every chart $i$ and every $y\in X_\sigma(\mathbb C)$, require $$\phi_{\sigma,i}(y)=\log\left(\sum_{a=0}^{N-1}\left| \sum_{k=0}^{n-1}\left(\sum_{m=0}^{N-1}\sigma(c_{km})(A_\sigma)_{ma}\right)s(\ell_k)_i(y) \right|^2\right).$$ In this last identity, each local coefficient $s(\ell_k)_i$ is extended by zero outside $U_i$. Thus the identity also prescribes $\phi_{\sigma,i}(y)=0$ there.
