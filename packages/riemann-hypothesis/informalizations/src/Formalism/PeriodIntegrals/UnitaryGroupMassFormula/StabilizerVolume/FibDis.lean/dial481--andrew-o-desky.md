---
{
  "module": "src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/StabilizerVolume/FibDis.lean",
  "declarations": [
    "PI.VolStabS.DiscreteGroups.disintStep_holds"
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

## Extending a fibre integration identity to all nonnegative functions

[Theorem ALG.0801](https://andrewodesky.com/rh/lean/PI.VolStabS.DiscreteGroups.disintStep_holds/)

Let $V,X$ be locally compact, second-countable Hausdorff spaces with their Borel structures, and let $Y$ be Hausdorff. Let $\mu,\nu$ be Borel measures on $V,X$, respectively, finite on compact sets, and suppose $\nu$ is positive on every nonempty open set. Let $f:V\to Y$ be continuous, $\iota:X\to Y$ a closed embedding, and $f(V)\subseteq\iota(X)$. Let $U\subseteq V$ be open, and assign to each $b\in X$ a Borel measure $\mu_b$ on $V$ such that $$\mu_b\bigl(V\setminus(f^{-1}\{\iota(b)\}\cap U)\bigr)=0,$$ and $\mu_b(K)<\infty$ for every compact $K\subseteq U$. Suppose that for every continuous real function $\varphi$ with compact support contained in $U$, $\varphi$ is integrable for every $\mu_b$, the function $b\mapsto\int\varphi\,d\mu_b$ is continuous, and for every compact $S\subseteq X$, $$\int_{f^{-1}(\iota(S))}\varphi\,d\mu=\int_S\!\left(\int_V\varphi\,d\mu_b\right)d\nu(b).$$ Then for every measurable $\varphi:V\to[0,\infty]$, $$\int_U\varphi\,d\mu=\int_X\!\left(\int_V\varphi\,d\mu_b\right)d\nu(b).$$
