---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/SumHeckeIndicatorIntegralEqPrimitiveStatement.lean",
  "declarations": [
    "GlobalTheory.T.sum_hecke_indicator_integral_eq_primitive"
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

## An alternating Hecke count detecting full row rank

[Theorem ALG.0843](https://andrewodesky.com/rh/lean/GlobalTheory.T.sum_hecke_indicator_integral_eq_primitive/)

Let $\mathcal O$ be a discrete valuation domain with fraction field $K$, finite residue field $k$ of cardinality $q$, and uniformizer $\pi$. Fix $r,n\ge0$, an index set $I$, matrices $\alpha_j\in\operatorname{GL}_r(K)$, finite sets $R_j\subseteq I$, and a family $\rho_i\in\operatorname{GL}_r(K)$. Put $K_0=\operatorname{GL}_r(\mathcal O)$. For every $1\le j\le r$, assume that $\alpha_j$ and $\pi\alpha_j^{-1}$ have entries in $\mathcal O$, that $\det\alpha_j\in\pi^j\mathcal O^\times$, and that $$K_0\alpha_jK_0=\coprod_{i\in R_j}\rho_iK_0.$$ For $z\in M_{r\times n}(\mathcal O)$, let $$N_j(z)=\#\{i\in R_j:\rho_i^{-1}z\in M_{r\times n}(\mathcal O)\}.$$ Then $$1+\sum_{j=1}^r(-1)^jq^{j(j-1)/2}N_j(z) =\begin{cases}1,&\text{the rows of }z\bmod\pi\text{ are linearly independent over }k,\\0,&\text{otherwise.}\end{cases}$$
