---
{
  "module": "src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/HodgeBundleAmpleOnRegularLocus.lean",
  "declarations": [
    "GlobalTheory.T.hodge_bundle_ample_on_regular_locus"
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

## Ample domination at interior points of a flag compactification

[Theorem AG.0378](https://andrewodesky.com/rh/lean/GlobalTheory.T.hodge_bundle_ample_on_regular_locus/)

Assume the source's compactification and positivity packages specified below. Fix its Hermitian moduli datum over a CM number field $E$: the CM host, signature $(p,q)$, lattice, level, moduli scheme $X$, and coefficient field $F$. Fix a smooth toroidal model with normal-crossings boundary, its logarithmic Kodaira–Spencer condition and flag model, and an irreducible component $Z$ of the generic moduli scheme. Assume $F$ is relatively algebraically closed in the function field of every such component.

Let $\Sigma$ be the CM-type embeddings selected by the host, $N=p+q$, and let $\lambda=(\lambda_{\tau,i})_{\tau\in\Sigma,0\le i<N}$ be an integral weight satisfying $\lambda_{\tau,i}-\lambda_{\tau,i+1}\ge1$. For every point $y$ of the interior of the flag component described below, there are a dominant integral weight $\mu$ and an integer $m>0$ such that $\mathcal L_{m\lambda-\mu}$ amply dominates at $y$.
