---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/ThetaLawProofs/ThetaKeyRuleValuationUnitOfFunctorialStatement.lean",
  "declarations": [
    "GlobalTheory.T.thetaKeyRule_valuationUnit_of_functorial"
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

## A functorial theta value is a unit over a normal domain

[Theorem AG.0706](https://andrewodesky.com/rh/lean/GlobalTheory.T.thetaKeyRule_valuationUnit_of_functorial/)

For every characteristic-zero field $K$, suppose a rule $\kappa$ assigns a nonzero scalar $\kappa_K(x)$ to each theta datum $x$ described below. Assume it commutes with all field extensions. Also assume the following discrete valuation property: if a datum over a discrete valuation ring $R$ has generic fibre $x$ over its characteristic-zero fraction field $K$, then some $u\in R^\times$ satisfies $\kappa_K(x)=u$ in $K$; for every surjective map $R\to k$ to a characteristic-zero field and every compatible fibre datum $x_k$, one also has $\kappa_k(x_k)=u$ in $k$.

Let $S$ be a commutative Noetherian ring, $V$ an integrally closed domain with characteristic-zero fraction field $K$, and $g:S\to V$ a homomorphism. If $y$ is a theta datum over $S$ and $x$ its base change along $S\to V\to K$, there is $u\in V^\times$ with $\kappa_K(x)=u$ in $K$.
