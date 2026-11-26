---
{
  "module": "src/Development/WeilBound/CuspidalAdmissibility/OccPair.lean",
  "declarations": [
    "PositivityTheory.TfC.OccursIff.Pair.admissible_and_equiv"
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

## An invariant pairing identifies irreducible smooth representations

[Theorem REP.0210](https://andrewodesky.com/rh/lean/PositivityTheory.TfC.OccursIff.Pair.admissible_and_equiv/)

Let $G$ be a locally compact Hausdorff totally disconnected topological group. Let $\sigma$ on $X$ be a smooth irreducible complex representation and $\pi$ on $Y$ an admissible irreducible complex representation. Suppose there are nonzero sesquilinear forms $$B:X\times Y\to\mathbb C,\qquad C:Y\times Y\to\mathbb C,$$ linear in the first variable and conjugate-linear in the second, with $$B(\sigma(g)x,\pi(g)y)=B(x,y),\qquad C(\pi(g)y,\pi(g)y')=C(y,y')$$ for all $g,x,y,y'$. Then $\sigma$ is admissible and $\sigma\simeq\pi$ as complex $G$-representations.
