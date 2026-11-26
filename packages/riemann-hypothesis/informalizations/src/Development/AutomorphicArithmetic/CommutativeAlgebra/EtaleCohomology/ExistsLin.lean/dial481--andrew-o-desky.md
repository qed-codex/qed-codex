---
{
  "module": "src/Development/AutomorphicArithmetic/CommutativeAlgebra/EtaleCohomology/ExistsLin.lean",
  "declarations": [
    "UpperTheory.Ru.crystallineComparison.geoLoc"
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

## A crystalline representation containing a geometric eigenspace

[Theorem PHT.0062](https://andrewodesky.com/rh/lean/UpperTheory.Ru.crystallineComparison.geoLoc/)

Assume the source's finite Frobenius-correspondence annihilation principle and crystallinity theorem for smooth proper models. Let $\ell$ be prime and fix compatible local period-ring and integral comparison data. Let $K\subseteq\overline{\mathbb Q}_\ell$ be finite over $\mathbb Q_\ell$, with its integer ring a discrete valuation ring and residue cardinality $q=\ell^f$, $f>0$.

Let $Z/K$ be smooth projective, with correspondences $Z\xleftarrow{s_\gamma}Y_\gamma\xrightarrow{t_\gamma}Z$, where every $s_\gamma$ is finite étale of a specified constant degree. Fix $\theta_\gamma\in\overline{\mathbb Q}_\ell$ and a surjective integral cover in the source's sense: a smooth projective model over $\mathcal O_K$, a finite étale cover of its generic fibre by $Z$, and a finite deck action whose transformations occur among the correspondences with eigenvalue one. Assume the cover satisfies the source's Frobenius graph-cycle congruence of order $n\ge0$, with eigenvalues $\vartheta_0,\ldots,\vartheta_n$ after division by the prescribed positive covering multiplicities. Let $\rho_1:G_K\to\operatorname{GL}_a(\overline{\mathbb Q}_\ell)$ be a matrix realization of the simultaneous $\theta$-eigenspace in the total geometric étale cohomology of $Z$, where $a\ge0$.

There are a finite-dimensional $\mathbb Q_\ell$-representation $V$ of $G_K$, endomorphisms $T_j\in\operatorname{End}_{\mathbb Q_\ell}V$ for $j\ge0$, and an injective equivariant map $b:\overline{\mathbb Q}_\ell^a\to\overline{\mathbb Q}_\ell\otimes V$ such that $V$ is crystalline, $$(1\otimes T_j)b(x)=\vartheta_j b(x)\qquad(0\le j\le n),$$ and for every $z\in D_{\mathrm{cris}}(V)$, $$\sum_{j=0}^{n}(-1)^j q^{\binom j2}(T_j\otimes\varphi^{f(n-j)})z=0.$$ Here $\varphi$ is the period-ring Frobenius, and $D_{\mathrm{cris}}(V)$ is the invariant subspace in the crystalline tensor product.
