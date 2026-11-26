---
{
  "module": "src/Development/WeilBound/CoreStatements/TemperedRepresentationTheory/ArakelovCycleHeights/ExistsMetricExtB.lean",
  "declarations": [
    "GlobalTheory.ArithmeticHeightTower.Read1.exists_ambientZ"
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

## Extending Hermitian line bundles to products of projective spaces

[Theorem ARAK.1452](https://andrewodesky.com/rh/lean/GlobalTheory.ArithmeticHeightTower.Read1.exists_ambientZ/)

Let $X$ be integral, projective and flat over $\operatorname{Spec}\mathbb Z$, of dimension $D+1$, and let $(\overline L_i)_{i\in I}$ be a finite family of Hermitian line bundles on $X$. There are $m\ge0$, integers $n_0,\ldots,n_m\ge0$, a closed immersion over $\mathbb Z$ $$j:X\hookrightarrow P=\prod_{c=0}^{m}\mathbb P^{n_c}_{\mathbb Z},$$ and Hermitian line bundles $\overline M_i$ on $P$ with $j^*\overline M_i$ isometric to $\overline L_i$. For each $i$ there exist $c_i\in\{1,\ldots,m\}$ and $t_i\in\mathbb Z$ such that the underlying line bundle of $\overline M_i$ is isomorphic to $$\operatorname{pr}_{c_i}^*\mathcal O(1)\otimes\operatorname{pr}_0^*\mathcal O(t_i).$$
