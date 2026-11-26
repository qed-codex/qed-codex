---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/EtaleFunctorExactOnLatticesStatement.lean",
  "declarations": [
    "GlobalTheory.T.etaleFunctor_exact_on_lattices"
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

## Exactness of the associated etale module functor on lattices

[Theorem PHT.0914](https://andrewodesky.com/rh/lean/GlobalTheory.T.etaleFunctor_exact_on_lattices/)

Fix the source's global arithmetic datum and its local Wach-module system with an etale comparison package. Let $\ell$ be prime, $K,L\subseteq\overline{\mathbb Q}_\ell$ finite, and $s\ge1$, with $s\ge2$ if $\ell=2$. Put $K_s=K_0(\mu_{\ell^s})$, where $K_0$ is the maximal unramified subfield of $K$. Suppose $K\subseteq K_s$ and every $\mathbb Q_\ell$-embedding of $K_s$ into $\overline{\mathbb Q}_\ell$ has image in $L$. Write $O_L$ for the integers of $L$ and $\mathcal D$ for the associated etale module functor at $(K,s,L)$.

Let $T_0,T_1,T_2$ be stable $O_L$-lattices in finite-dimensional continuous $L$-representations of $G_K$. Let $\iota:T_0\to T_1$ and $\pi:T_1\to T_2$ be induced by continuous equivariant $L$-linear maps. Suppose the sequence of rational representations is exact, $\pi(T_1)=T_2$, and $\iota^{-1}(T_1)=T_0$. Then $$0\longrightarrow\mathcal D(T_0)\xrightarrow{\mathcal D(\iota)}\mathcal D(T_1)\xrightarrow{\mathcal D(\pi)}\mathcal D(T_2)\longrightarrow0$$ is exact.
