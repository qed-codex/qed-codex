---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/PAdicWittLattices/TraceSplitHolds.lean",
  "declarations": [
    "UpperTheory.Gal.G3.hodgeBC_holds",
    "UpperTheory.Gal.G3.lowPiece_holds"
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

## Base change for Hodge cohomology and finite etale traces

[Theorem AG.1581](https://andrewodesky.com/rh/lean/UpperTheory.Gal.G3.hodgeBC_holds/)

Let $\varphi:k\to k'$ be a homomorphism of fields. For every $k$-scheme $X$, its base change $X'$ and the projection $g:X'\to X$, there are $\varphi$-semilinear maps $$\beta_X^{a,b}:H^b(X,\Omega^a_{X/k})\longrightarrow H^b(X',\Omega^a_{X'/k'})\qquad(a,b\ge0).$$ If $X\to\operatorname{Spec}k$ is proper, these maps send every $k$-basis to a $k'$-basis with the same indexing set. They commute with pullback: whenever $f:Y\to X$ and $f':Y'\to X'$ are morphisms over the respective fields in a commuting base-change square, $$\beta_Y^{a,b}f^*=(f')^*\beta_X^{a,b}.$$ If $f$ and $f'$ are both finite etale, they also commute with trace: $$\beta_X^{a,b}\operatorname{Tr}_f=\operatorname{Tr}_{f'}\beta_Y^{a,b}.$$

## An integral cover gives an inclusion of geometric eigenspaces

[Theorem AG.1608](https://andrewodesky.com/rh/lean/UpperTheory.Gal.G3.lowPiece_holds/)

Let $E$ be a number field with algebraic closure $\Omega$, let $\ell$ be prime, and put $L=\overline{\mathbb Q}_\ell$. Let $Z/E$ be smooth projective with correspondences $Z\xleftarrow{s_\gamma}Y_\gamma\xrightarrow{t_\gamma}Z$, each $s_\gamma$ finite étale of a specified constant degree. Fix eigenvalues $\theta_\gamma\in L$. Let $O$ be a commutative ring with $O\to E$, and let $C$ be a surjective integral cover of this correspondence system satisfying the integral-cover conditions in the conventions. For each $\gamma$ choose a descended correspondence on its smooth projective $O$-model, whose left leg is finite étale and whose comparison with the original correspondence is finite étale of positive degree $m_\gamma$.

Let $\rho_0:G_E\to\operatorname{GL}_{d_0}(L)$ realize the simultaneous $\theta_\gamma$-eigenspace in total geometric étale cohomology of $Z$, and let $\rho_1:G_E\to\operatorname{GL}_{d_1}(L)$ realize the simultaneous $\theta_\gamma/m_\gamma$-eigenspace for the descended generic-fibre system. There is a matrix $A\in M_{d_0\times d_1}(L)$ such that $$A:L^{d_1}\hookrightarrow L^{d_0},\qquad\rho_0(g)A=A\rho_1(g)\quad(g\in G_E).$$
