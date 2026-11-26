---
{
  "module": "src/Development/WeilBound/RepresentationTheoryGL/ConstantTermFiniteness/CuspidalConstantTerms/FormsSubsetFormsOnEmpty.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.Hypotheses₂.ConstFin.Rg.finite_constTerm"
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

## Finite-dimensional spaces of constant terms

[Theorem REP.0043](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.Hypotheses%E2%82%82.ConstFin.Rg.finite_constTerm/)

Assume the source's full arithmetic unitary datum, with CM extension $E/F$ and Hermitian space $V$. Put $G=U(V)(\mathbb A_F)$. Choose the source-compatible archimedean embeddings $\theta_\tau$, and frames $A_\tau$ with $$A_\tau^*J_{\varepsilon_\tau}A_\tau=\operatorname{Gram}(V)_\tau,$$ where $J_{\varepsilon_\tau}$ is diagonal with entries $\pm1$. These frames identify a maximal compact subgroup $K_\tau$ at each infinite place. Let $U$ be an open subgroup of $G$. For each $\tau$ let $\rho_\tau$ be a representation of $K_\tau$ on a finite-dimensional complex vector space, all of whose matrix coefficients are continuous, and prescribe numbers $c_{\tau,k}\in\mathbb C$ for $k\ge0$.

Let $\mathcal F$ consist of continuous left $U(V)(F)$-invariant functions $f:G\to\mathbb C$ with open finite adelic level, smooth in all archimedean directions, contained in a finite-dimensional space stable under every operator $D_{\tau,k}$ defined below, and with one common polynomial growth exponent in the source's matrix height for all archimedean derivatives on every fixed translate of the archimedean group. Require right invariance under $U\cap U(V)(\mathbb A_{F,f})$, require every $K_\tau$-orbit function $k\mapsto f(gk)$ to lie in the span of matrix coefficients of $\rho_\tau$, and require $$D_{\tau,k}f=c_{\tau,k}f\qquad(\tau,\ k\ge0),$$ where $D_{\tau,k}$ is the right differential operator corresponding to the trace of the $(k+1)$-st power of the matrix of Lie algebra generators. For every matrix $C$ over $E$ with a positive number of linearly independent columns and $C^*\operatorname{Gram}(V)C=0$, let $P_C$ be the parabolic stabilizing their span, $N_C$ its unipotent radical, and $$f_{P_C}(g)=\int_{N_C(F)\backslash N_C(\mathbb A_F)}f(ug)\,du$$ the constant term with quotient Haar measure normalized to mass one. Then $$\dim_{\mathbb C}\operatorname{span}\{f_{P_C}:f\in\mathcal F\}<\infty.$$
