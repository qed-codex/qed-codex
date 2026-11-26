---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/ThetaCoefficientOfConvergenceStatement.lean",
  "declarations": [
    "GlobalTheory.T.theta_coefficient_of_convergence"
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

## A nondegenerate theta coefficient as an orbital average

[Theorem THETA.1598](https://andrewodesky.com/rh/lean/GlobalTheory.T.theta_coefficient_of_convergence/)

Assume absolute theta-integral convergence for every source global theta datum and every Schwartz test function in the range $n\ge1$ and either Witt index zero or $n+\operatorname{Witt}(V)<\dim V$. Fix a complete global theta datum with CM fields $E/F$ and Hermitian space $V$ of dimension $m$. Let $$n<m\le2n,\qquad n+\operatorname{Witt}(V)<m.$$ Choose all the source's standard Schrodinger data: a continuous unitary nontrivial additive character $\psi$ of $\mathbb A_F/F$, a Hecke character $\chi$ of $E$ restricting to $\eta^m$ on $\mathbb A_F^\times$, compatible infinite embeddings, additive Haar measure $\mu$ on $V(\mathbb A_F)^n$ with rational covolume one, and a Weil action $\omega$ satisfying the prescribed Levi, unipotent and Weyl formulas. Here $\eta$ is the quadratic norm character. Also choose the prescribed Siegel height function $H$, real infinity parameters $l_\tau$ expressing the infinite character, Cartan involutions $s_\tau$, Haar measure $\nu$ on $U(V)(\mathbb A_F)$, and a Schwartz test function $\Phi$ in the polynomial Fock subspace.

Write $G$ for the rank-$n$ split skew-Hermitian unitary group in this datum, and $n(b)=\left(\begin{smallmatrix}1&b\\0&1\end{smallmatrix}\right)$ for its Siegel unipotent map, $b\in\operatorname{Herm}_n(\mathbb A_F\otimes_FE)$. Choose additive Haar measure $\lambda$ and a fundamental domain $\mathcal D$ for the rational Hermitian matrices with $\lambda(\mathcal D)=1$. Put $$I_\Phi(g)=\mathop{\operatorname{avg}}_{h\in U(V)(F)\backslash U(V)(\mathbb A_F)}\sum_{x\in V(E)^n}(\omega(g)\Phi)(h^{-1}x),$$ using the quotient measure induced by $\nu$ and normalized averaging. For every $\beta\in\operatorname{Herm}_n(E)$ with $\det\beta\ne0$ and every $g\in G$, $$\int_{\mathcal D}I_\Phi(n(b)g)\psi\!\left(-\tfrac12\operatorname{Tr}_{E/F}\operatorname{tr}(\beta b)\right)d\lambda(b)=\mathop{\operatorname{avg}}_h\sum_{\substack{x\in V(E)^n\\\operatorname{rank}x=n,\ (\langle x_i,x_j\rangle)_{i,j}=\beta}}(\omega(g)\Phi)(h^{-1}x).$$ The trace on adelic matrices is the scalar-extended field trace.
