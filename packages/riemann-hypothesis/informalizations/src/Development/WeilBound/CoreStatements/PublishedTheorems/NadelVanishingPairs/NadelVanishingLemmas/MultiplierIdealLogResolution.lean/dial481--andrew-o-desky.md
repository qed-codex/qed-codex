---
{
  "module": "src/Development/WeilBound/CoreStatements/PublishedTheorems/NadelVanishingPairs/NadelVanishingLemmas/MultiplierIdealLogResolution.lean",
  "declarations": [
    "GlobalTheory.Discrepancy.mem_support_multIdeal_iff"
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

## Support of the multiplier ideal and the non-klt locus

[Theorem AG.1397](https://andrewodesky.com/rh/lean/GlobalTheory.Discrepancy.mem_support_multIdeal_iff/)

Let $k$ have characteristic zero, and let $X/k$ be an integral, locally noetherian normal projective scheme of dimension $n$. Fix a rational coefficient function $\Delta:X\to\mathbb Q$, a nonzero rational $n$-form $\eta$, an integer $m>0$, and a Cartier divisor $G$ representing the local log-canonical multiple $m(K_X+\Delta)$ in the sense of ([Testing local klt and log canonical conditions on a resolution](https://andrewodesky.com/rh/lean/GlobalTheory.Discrepancy.kltAt_lcAt_iff_of_isLogRes/)), with $K_X$ computed from $\eta$.

Assume there is a dominant morphism $\pi:Y\to X$, with $Y$ integral and locally noetherian, such that $Y/k$ is smooth projective of dimension $n$, the map on function fields is bijective, $K_Y=\operatorname{div}(\pi^*\eta)$ is a Cartier divisor, and a closed simple normal-crossing set $B\subset Y$ contains the support of $\pi^*G-mK_Y$. Let $\mathcal J$ be an ideal sheaf satisfying the valuative multiplier-ideal condition below for these data. Then for every $x\in X$, $$x\in\operatorname{Supp}(\mathcal O_X/\mathcal J)\quad\Longleftrightarrow\quad(X,\Delta)\text{ is not klt at }x.$$
