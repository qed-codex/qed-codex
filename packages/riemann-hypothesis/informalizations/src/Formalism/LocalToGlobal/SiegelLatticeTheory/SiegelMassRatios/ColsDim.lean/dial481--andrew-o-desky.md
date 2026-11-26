---
{
  "module": "src/Formalism/LocalToGlobal/SiegelLatticeTheory/SiegelMassRatios/ColsDim.lean",
  "declarations": [
    "Formalism.L2.SG.ColsDim.columns_dimension"
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

## Dimension of an equivariant function space over a finite class set

[Theorem ALG.0321](https://andrewodesky.com/rh/lean/Formalism.L2.SG.ColsDim.columns_dimension/)

Let $\Gamma,G_\infty,G_f$ be groups, $k$ a field, $V$ a finite-dimensional $k$-vector space, and $\pi:G_\infty\to\operatorname{GL}(V)$ a representation. Fix homomorphisms $\iota_\infty:\Gamma\to G_\infty$, $\iota_f:\Gamma\to G_f$, subgroups $K\le K_0\le G_f$, and a character $\psi:K\to k^\times$. Assume $\iota_f(\Gamma)\backslash G_f/K$ is finite and $$x^{-1}\iota_f(\gamma)x\in K_0\quad\Longrightarrow\quad\gamma=1\qquad(x\in G_f,\ \gamma\in\Gamma).$$ Let $\mathcal C$ consist of $k$-linear maps $T:V\to k^{G_\infty\times G_f}$ satisfying, for every $\xi\in V$, $y\in G_\infty\times G_f$, $\gamma\in\Gamma$, $\kappa\in K$, and $h\in G_\infty$, $$\begin{aligned}T\xi((\iota_\infty\gamma,\iota_f\gamma)y)&=T\xi(y),\\T\xi(y(1,\kappa))&=\psi(\kappa)T\xi(y),\\T(\pi(h)\xi)(y)&=T\xi(y(h,1)).\end{aligned}$$ Then $\mathcal C$ is finite-dimensional and $$\dim_k\mathcal C=(\dim_kV)\,\#(\iota_f(\Gamma)\backslash G_f/K).$$
