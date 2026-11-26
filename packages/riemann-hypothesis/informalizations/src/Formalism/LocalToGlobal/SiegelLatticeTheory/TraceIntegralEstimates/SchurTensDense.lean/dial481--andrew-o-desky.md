---
{
  "module": "src/Formalism/LocalToGlobal/SiegelLatticeTheory/TraceIntegralEstimates/SchurTensDense.lean",
  "declarations": [
    "Formalism.L2.S.Pv.SchurTens.isSchur_tens"
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

## Schur orthogonality for a finite tensor product

[Theorem REP.1147](https://andrewodesky.com/rh/lean/Formalism.L2.S.Pv.SchurTens.isSchur_tens/)

Let $I$ be finite. For $v\in I$, let $G_v$ be a group with a topology and a sigma-algebra, let $\mu_v$ be a sigma-finite measure, and let $H_v$ be a complex inner product space. Suppose open subsets of $\prod_vG_v$ are measurable for the product sigma-algebra. Let $\sigma_v$ be strongly continuous unitary representations and let $d_v>0$ satisfy, for all $a,b,a',b'\in H_v$, $$\int_{G_v}\langle b,\sigma_v(g)a\rangle\overline{\langle b',\sigma_v(g)a'\rangle}\,d\mu_v(g)=\frac{\langle a',a\rangle\langle b,b'\rangle}{d_v},$$ with the integrands integrable. Let $H$ be a complex inner product space, let $\sigma(g)$ be bounded complex linear operators on $H$, and let $t:\prod_vH_v\to H$ satisfy $$\langle t(x),t(y)\rangle=\prod_v\langle x_v,y_v\rangle,\qquad \sigma(g)t(x)=t((\sigma_v(g_v)x_v)_v),$$ with the complex linear span of $t(\prod_vH_v)$ dense in $H$. Then the same Schur integral identity and integrability hold on $H$ for $\sigma$, the product measure $\prod_v\mu_v$, and the constant $d=\prod_vd_v$.
