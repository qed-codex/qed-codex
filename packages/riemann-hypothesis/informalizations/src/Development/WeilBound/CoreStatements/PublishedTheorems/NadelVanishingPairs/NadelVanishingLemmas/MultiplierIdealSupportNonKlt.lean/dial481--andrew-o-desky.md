---
{
  "module": "src/Development/WeilBound/CoreStatements/PublishedTheorems/NadelVanishingPairs/NadelVanishingLemmas/MultiplierIdealSupportNonKlt.lean",
  "declarations": [
    "GlobalTheory.Discrepancy.exists_isMultIdeal_support_iff_not_kltAt"
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

## A multiplier ideal supported on the non-klt locus

[Theorem AG.1348](https://andrewodesky.com/rh/lean/GlobalTheory.Discrepancy.exists_isMultIdeal_support_iff_not_kltAt/)

Assume the following principalization assertion: for every smooth integral projective variety $Y$ over a characteristic-zero field and every nonzero ideal sheaf $I$ on $Y$, there is a smooth integral projective variety $Y'$ and a morphism $s:Y'\to Y$ obtained by a sequence of blow-ups with smooth centers over $V(I)$, which is an isomorphism off $V(I)$, such that $I\mathcal O_{Y'}$ defines an effective Cartier divisor with simple normal-crossing support. Let $k$ have characteristic zero and let $X$ be an integral, locally Noetherian normal projective $k$-scheme of dimension $n\ge0$. Let $\Delta:X\to\mathbb Q$ be a rational boundary datum. Fix a nonzero rational $n$-form $\eta$, an integer $m>0$, and a Cartier divisor $G$, satisfying the local logarithmic-multiple condition in ([Testing local klt and log canonical conditions on a resolution](https://andrewodesky.com/rh/lean/GlobalTheory.Discrepancy.kltAt_lcAt_iff_of_isLogRes/)).

There is an ideal sheaf $\mathcal J$ on $X$ with the following valuative membership rule. On an affine open $U$, a section $f\in\mathcal O_X(U)$ belongs to $\mathcal J(U)$ precisely when, for every $x\in U$, every nonzero rational function $u$ representing $f$, every local equation $g$ of $G$ at $x$, and every divisorial valuation $v$ over $X$ through $x$, $$v(u)+a(v;\eta,m,g)>-1.$$ Here $a(v;\eta,m,g)=\operatorname{ord}_v(\eta)-v(g)/m$ is the discrepancy. Its support satisfies $$x\in\operatorname{Supp}(\mathcal O_X/\mathcal J)\quad\Longleftrightarrow\quad (X,\Delta)\text{ is not klt at }x.$$
