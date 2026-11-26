---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/GeometryProofs/SemiAbelianStatementHoldsStatement.lean",
  "declarations": [
    "GlobalTheory.T.semi_abelian_statement_holds"
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

## Density of isotropic special unitary groups in finite adeles

[Theorem AGR.0285](https://andrewodesky.com/rh/lean/GlobalTheory.T.semi_abelian_statement_holds/)

Let $E/F$ be a quadratic extension of number fields and $c\ne1$ an $F$-automorphism of $E$. Let $J\in M_N(E)$ satisfy $J^{\mathsf T}=c(J)$ and $\det J\ne0$, and suppose there is $e\in E^N\setminus\{0\}$ with $h_J(e,e)=0$. Put $G=\operatorname{SU}(J,c)$. Then $$G(\mathbb A_{F,f})\subseteq\overline{G(F)},$$ where $G(F)$ is diagonally embedded and $\mathbb A_{F,f}$ is the ring of finite adeles. The topology on $\mathbb A_{F,f}\otimes_FE$ is its finite-dimensional $\mathbb A_{F,f}$-module topology.
