---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/GeometryProofs/HodgeLatticeEigenDecompositionLocalStatement.lean",
  "declarations": [
    "GlobalTheory.T.hodge_lattice_eigen_decomposition_local"
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

## A local basis adapted to a Hodge eigenlattice

[Theorem AV.1099](https://andrewodesky.com/rh/lean/GlobalTheory.T.hodge_lattice_eigen_decomposition_local/)

Let $E$ be a number field, $\Omega$ a field of characteristic zero, $V$ a finite-dimensional $\Omega$-vector space, and $$\rho:\mathcal O_E\to\operatorname{End}_\Omega V,\qquad\rho_H:\mathcal O_E\to\operatorname{End}_\Omega(V\oplus V^*)$$ ring homomorphisms. Let $a\mapsto\bar a$ be an involutive automorphism of $\mathcal O_E$, $R\subseteq\Omega$ a local subring, and $\sigma,\sigma':E\hookrightarrow\Omega$ embeddings with images in $R$ and $\sigma'(a)=\sigma(\bar a)$ for $a\in\mathcal O_E$. Assume $$\operatorname{pr}_V\rho_H(a)y=\rho(a)\operatorname{pr}_Vy,\qquad\rho_H(a)(0,f)=(0,f\circ\rho(\bar a)).$$ Let $\ell_1,\ldots,\ell_g$ be an $\Omega$-basis of $V$, $L=\sum_iR\ell_i$, and $H\subseteq V\oplus V^*$ an $R$-submodule. Let $t_1,\ldots,t_{p+q}\in V\oplus V^*$ satisfy the following conditions. For an integral $\mathbb Z$-basis $(a_b)$ of $\mathcal O_E$, the vectors $\rho_H(a_b)t_i$ are $\Omega$-linearly independent, span $H$ over $R$, and $H$ spans $V\oplus V^*$ over $\Omega$. The projection of $H$ to $V$ is $L$, and $$(0,f)\in H\quad\Longleftrightarrow\quad f(L)\subseteq R.$$ Assume the simultaneous $\sigma$- and $\sigma'$-eigenspaces of $\rho$ have dimensions $p,q$.

There are $\Omega$-linearly independent families $b_1,\ldots,b_p$ and $c_1,\ldots,c_q$ spanning $L\cap V_\sigma$ and $L\cap V_{\sigma'}$ respectively over $R$, vectors $u_1,\ldots,u_{p+q}\in H\cap(V\oplus V^*)_\sigma$, and $A\in\operatorname{GL}_{p+q}(R)$ such that $$\operatorname{pr}_V u_i=b_i\ (i\le p),\qquad\operatorname{pr}_V u_{p+j}=0,\qquad (u_{p+j})_{V^*}(c_{j'})=\delta_{jj'},$$ and $$e_\sigma t_i=\sum_j A_{ij}u_j.$$
