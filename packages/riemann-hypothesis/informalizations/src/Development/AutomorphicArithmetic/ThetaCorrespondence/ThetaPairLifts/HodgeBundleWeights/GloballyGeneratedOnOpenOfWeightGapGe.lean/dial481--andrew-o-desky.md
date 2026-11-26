---
{
  "module": "src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/GloballyGeneratedOnOpenOfWeightGapGe.lean",
  "declarations": [
    "GlobalTheory.T.hodge_bundle_base_point_free_on_open"
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

## Cusp sections with sufficiently separated weights have no base points

[Theorem AV.1340](https://andrewodesky.com/rh/lean/GlobalTheory.T.hodge_bundle_base_point_free_on_open/)

Assume the source's arithmetic-geometric input package, deformation theorem, Hilbert–Samuel input package, Nadel vanishing and non-klt-divisor theorem, ([Principalization on a smooth projective variety](https://andrewodesky.com/rh/lean/PositivityTheory.ResPlug.WeightsCompactStabilizer.principalisation_closed/)), integral Siegel toroidal compactification theorem, toroidal-chart theorem, and ([Seminegativity of a semiabelian Lie bundle](https://andrewodesky.com/rh/lean/GlobalTheory.Nef.semiAbelianLieSeminegative/)).

Let $E$ be a CM field, and fix the source's Hermitian moduli datum over $E$, a level, its moduli scheme, a coefficient field $F$, a toroidal flag model $X$, a component $Z$, and compatible complex uniformizations at every embedding of $F$, all with the common rank parameter $r\ge0$. Assume $F$ is algebraically closed in the function field of every component of the moduli scheme. Let $d=[E:\mathbb Q]\binom{p+q}{2}/2\ge1$, where $(p,q)$ is the Hermitian signature in the moduli datum. Index weight coordinates by $j=0,\ldots,p+q-1$ and set $\kappa_{\tau,j}=q+2(j+1)-p-1$ for $j<p$, and $\kappa_{\tau,j}=-p+2(j-p+1)-q-1$ for $j\ge p$, at every chosen CM embedding $\tau$.

Let $\lambda$ be an integral weight at the chosen CM embeddings and suppose every adjacent gap of $\lambda-\kappa$ is at least $$\binom{d+1}{2}+1.$$ Assume every cusp section of weight $\lambda$ extends to a global section vanishing on the boundary, and every global section vanishing on the boundary restricts to such a cusp section. Then the space of global sections whose restriction is a cusp section of weight $\lambda$ has no base point on the open flag variety.
