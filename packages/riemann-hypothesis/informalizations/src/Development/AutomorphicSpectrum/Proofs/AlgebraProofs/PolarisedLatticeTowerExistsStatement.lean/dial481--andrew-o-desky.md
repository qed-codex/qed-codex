---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/AlgebraProofs/PolarisedLatticeTowerExistsStatement.lean",
  "declarations": [
    "GlobalTheory.T.polarised_lattice_tower_exists"
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

## Extension of a polarized lattice to a valuation ring

[Theorem PHT.0661](https://andrewodesky.com/rh/lean/GlobalTheory.T.polarised_lattice_tower_exists/)

Let $p$ be prime, let $C$ be an algebraically closed field of characteristic zero with valuation $v:C\to\mathbb R_{\ge0}$, and let $O\subseteq C$ be its valuation ring. Assume $v(p)<1$ and that $O$ is complete for the powers of $(p)$. Let $E$ be a number field, $c:E\simeq E$ a field automorphism, and $\Lambda$ a finite free abelian group with an $\mathcal O_E$-action. Let $B:\Lambda\times\Lambda\to\mathbb Z$ be alternating and unimodular, with $$B(ax,y)=B(x,c(a)y).$$ Fix $u_1,\ldots,u_N\in\Lambda$ such that $$\operatorname{rank}_{\mathbb Z}\Lambda=N[E:\mathbb Q],\qquad \Lambda=\sum_i\mathcal O_Eu_i+p\Lambda.$$ There are an action $\rho:\mathcal O_E\to\operatorname{End}_C(V)$ on $V=C\otimes_{\mathbb Z}\Lambda$, an $O$-submodule $T\subseteq V$, and a $C$-bilinear form $b$ such that $$\rho(a)(1\otimes x)=1\otimes ax,\quad T=\operatorname{span}_O\{1\otimes x:x\in\Lambda\},\quad b(1\otimes x,1\otimes y)=B(x,y).$$ The form $b$ is alternating and nondegenerate, $T$ equals its $b$-dual, and $$b(\rho(a)x,y)=b(x,\rho(c(a))y).$$ For any fixed integral basis $(\beta_j)$ of $\mathcal O_E$, the vectors $\rho(\beta_j)(1\otimes u_i)$ form a $C$-basis of $V$ and generate $T$ over $O$.
