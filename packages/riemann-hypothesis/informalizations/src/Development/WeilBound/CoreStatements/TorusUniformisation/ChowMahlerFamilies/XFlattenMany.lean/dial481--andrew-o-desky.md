---
{
  "module": "src/Development/WeilBound/CoreStatements/TorusUniformisation/ChowMahlerFamilies/XFlattenMany.lean",
  "declarations": [
    "PositivityTheory.Xgn.A_flatten_many.locFree_of_minor",
    "PositivityTheory.Xgn.t_flatten_many"
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

## Making finitely many lattice families locally free on a refined model

[Theorem AG.0976](https://andrewodesky.com/rh/lean/GlobalTheory.T.lattice_family_model_bundles/)

Let $O$ be a discrete valuation domain, $\Omega$ a field with an $O$-algebra structure, and $x=(x_{ki})$ a coordinate family indexed by a finite set $K$ of finite blocks $I_k$. Let $d\in\mathbb N$. Assume the dimension-$d$ model conditions and field-generation condition of ([Coordinate models and compatible chart lattices](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.IndefiniteRowSideFullHecke.NumbersDVR.Bundles.IsModelOver/)), and use its chart notation $m_c(x),R_c(x)$.

Let $J$ be a finite set. For each $j\in J$, let $N_j\in\mathbb N$ and let $V_j$ be an $\Omega$-vector space with $\dim_\Omega V_j=N_j$, and let $(\Gamma_{j,c})$ be a compatible family in the sense of ([Coordinate models and compatible chart lattices](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.IndefiniteRowSideFullHecke.NumbersDVR.Bundles.IsModelOver/)). Suppose that, for every $j$ and every nonzero chart $c$, $\Gamma_{j,c}$ is the $R_c(x)$-span of a finite set spanning $V_j$ over $\Omega$.

There are finitely many additional finite coordinate blocks $z$ over $\Omega$ such that the joined coordinate family $(x,z)$ satisfies the same model conditions with dimension parameter $d$, and, on every chart $c$ with $m_c(x,z)\ne0$, the $R_c(x,z)$-span of $\Gamma_{j,c|_K}$ is locally free of rank $N_j$ inside $V_j$, in the sense of ([Coordinate models and compatible chart lattices](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.IndefiniteRowSideFullHecke.NumbersDVR.Bundles.IsModelOver/)), for every $j\in J$.

## Freeness from ratios of maximal minors

[Theorem ALG.0977](https://andrewodesky.com/rh/lean/PositivityTheory.Xgn.A_flatten_many.locFree_of_minor/)

Let $O$ be a commutative ring, $\Omega$ a field with an $O$-algebra structure, and $R_0\subseteq R\subseteq\Omega$ be $O$-subalgebras. Let $V$ be an $\Omega$-vector space with basis $B=(b_1,\ldots,b_N)$, let $v_1,\ldots,v_M\in V$, and let $p\in\Omega^\times$. For $J:\{1,\ldots,N\}\to\{1,\ldots,M\}$ write $\Delta_J$ for the determinant of $(v_{J(1)},\ldots,v_{J(N)})$ in the basis $B$. Suppose some $I$ satisfies $\Delta_I\ne0$ and $$\Delta_J/\Delta_I\in R\qquad\text{for every }J.$$ Then the $R$-span of the $R_0$-span of $pv_1,\ldots,pv_M$ is locally free of rank $N$ inside $V$.
