---
{
  "module": "src/Development/ResolutionOfSingularities/EmbeddedResolution/ResolutionDescent/BlowupSequenceDescentDatum.lean",
  "declarations": [
    "FunctorialResolution.EmbeddedResolution.exists_isStrictPullback_of_isomorphic_baseChange"
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

## Descent of a blowup sequence from its two pullbacks

[Theorem AG.1201](https://andrewodesky.com/rh/lean/FunctorialResolution.EmbeddedResolution.exists_isStrictPullback_of_isomorphic_baseChange/)

Let $g:W\to Y$ be a flat quasi-compact morphism of schemes, and let $t$ be a finite sequence of blowups over $W$. Suppose the pullbacks of $t$ along the two projections $W\times_YW\rightrightarrows W$ are isomorphic as blowup sequences. There exists a finite blowup sequence $s$ over $Y$ such that $t$ is a strict pullback of $s$ along $g$: the lengths agree, there are morphisms from every stage of $t$ to the corresponding stage of $s$ extending $g$, every transition square is cartesian, and every center in $t$ is the pullback of the corresponding center in $s$.
