---
{
  "module": "src/Development/WeilBound/CoreStatements/AutomorphicKernels/MoriwakiBigness/MoriwakiBigTheorem/Outright.lean",
  "declarations": [
    "PositivityTheory.Pf1.HilbertSamuelMoriwaki.moriwakiBig_outright"
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

## Arithmetic intersection and volume

[Theorem ARAK.0034](https://andrewodesky.com/rh/lean/PositivityTheory.Pf1.HilbertSamuelMoriwaki.moriwakiBig_outright/)

Use the coordinate rings, arithmetic varieties, Hermitian line data, homogeneous coordinate ideals $P_y$ and basic intersection systems of ([Arithmetic intersection systems in homogeneous coordinates](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Geo.IsIntersectionSystem/)), and the positivity conditions and real volume $V_D(y,A)$ of ([Small sections and positivity in homogeneous coordinates](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Geo.Birational/)). Let $B$ and $I_b$ be finite, let $\Omega$ be a field, and let $y\in\Omega^{\coprod_bI_b}$ be a coordinate tuple. Put $R=\mathbb Z[X_{b,i}]$ and $P=P_y$. Let $D\in\mathbb N$, let $A=(a,h)$ be a Hermitian line datum, let $I$ be an intersection system, and let $P_0\subseteq R$ be an ideal. Assume:

1. $P$ is an arithmetic variety of dimension $D+1$.
2. The coordinates $y$ are birational.
3. $P_0\subseteq P$, and $A$ is semipositive relative to $P_0$ on $P$ and invariant under conjugation.
4. $a$ is nef on the fibres of $P$.
5. For every arithmetic variety $W$ of dimension $2$ with $P\subseteq W$, the curvature integral $\mathcal I_W(A;1)$ defined in ([Arithmetic intersection systems in homogeneous coordinates](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Geo.IsIntersectionSystem/)) is nonnegative.
6. $I$ is a basic intersection system.

Then $$I_P(\underbrace{A,\ldots,A}_{D+1})\le V_D(y,A).$$
