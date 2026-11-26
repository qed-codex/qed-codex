---
{
  "module": "src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/ExistsConstantTwistOfThinDivisor.lean",
  "declarations": [
    "GlobalTheory.ThinTwist.exists_constant_twist_of_thin_divisor"
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

## Constant-norm removal of parallel and scalar weights

[Theorem ARAK.0123](https://andrewodesky.com/rh/lean/GlobalTheory.ThinTwist.exists_constant_twist_of_thin_divisor/)

A parallel weight and a nonnegative scalar weight can be removed from a cusp form while multiplying its pointwise norm on a prescribed component by one positive constant.

Assume ([Global hypotheses for Hodge-bundle estimates](https://andrewodesky.com/rh/s/k2-hodge-bundle-hypotheses.html)). Fix the arithmetic theta datum and a sequence of unitary moduli varieties with the comparison hypothesis specified below. Choose a stage $1\le j\le m$, a good cover with parameters $e\in\mathbb N$, $o\in\mathbb R$, and assume common-degree flat sections exist on that cover. Let $(p,q)$ be its signature, $K$ its coefficient field, $\Psi$ its fixed CM type, $u:\Psi\times\{0,\ldots,p+q-1\}\to\mathbb Z$ any weight, $w:\Psi\to\mathbb Z$ any function, and $s\in\mathbb N$.

For every component $Z$, every embedding $\sigma:K\hookrightarrow\mathbb C$ taking the distinguished coefficient-field root of $-d$ to $r_0$, and every algebraic cusp form $f$ of automorphic weight $W(u+w,s)$ on the whole cover, there are a cusp form $g$ of weight $W(u,0)$ supported on $Z$ and a real $A>0$ such that $$\|g\|_{W(u,0),\sigma}(z)=A\,\|f\|_{W(u+w,s),\sigma}(z)$$ for every uniformized frame $z$ belonging to $Z$. No dominance condition on $u$ or $u+w$ is imposed.
