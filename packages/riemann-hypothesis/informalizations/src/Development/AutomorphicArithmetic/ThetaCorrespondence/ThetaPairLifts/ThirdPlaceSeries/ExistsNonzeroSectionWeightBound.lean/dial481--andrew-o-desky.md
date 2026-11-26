---
{
  "module": "src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExistsNonzeroSectionWeightBound.lean",
  "declarations": [
    "GlobalTheory.ThetaSteep.exists_theta_section_alt_alt"
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

## A nonzero Hodge section with a boundary valuation bound

[Theorem AV.0045](https://andrewodesky.com/rh/lean/GlobalTheory.ThetaSteep.exists_theta_section_alt_alt/)

There is a nonzero section of Hodge weight $8r$ whose order at every compatible boundary valuation is at least $8/625$ times the degeneration invariant. Multiplication by this section preserves two specified cusp-section spaces after a weight shift.

Assume ([Global hypotheses for Hodge-bundle estimates](https://andrewodesky.com/rh/s/k2-hodge-bundle-hypotheses.html)). Assume also, uniformly for the families and compatible points of ([Covolume of integral cusp forms](https://andrewodesky.com/rh/lean/GlobalTheory.CovTop.CovolumeBoundOfX/)), the size-at-a-stage and lattices-on-a-cover hypotheses of ([Weight, size and lattice conditions at a unitary lift stage](https://andrewodesky.com/rh/lean/GlobalTheory.CovTop.GramAt/)), and the common-degree flat-section conclusion of ([Existence and common degree of flat CM sections](https://andrewodesky.com/rh/lean/GlobalTheory.CovTop.FlatDegProof.flatDeg_alt_alt/)). Each of these three assumptions has the small-$\varepsilon$, threshold-rule and eventual-point quantifiers stated in ([Existence and common degree of flat CM sections](https://andrewodesky.com/rh/lean/GlobalTheory.CovTop.FlatDegProof.flatDeg_alt_alt/)); size is required at every stage, while the two cover assumptions are required at every nonterminal stage and every good cover.

Then, with those same uniform quantifiers, the following holds at every nonterminal stage and good cover. For every component $Z$ and every smooth toroidal compactification with normal-crossing boundary, logarithmic Kodaira–Spencer identification and complete flags in the Lie eigenspaces, let $Y_Z$ be the compactified flag component, $U_Z$ its interior, and $\mathcal L(\eta)$ its weight line bundle. There is $$0\ne\theta\in H^0(Y_Z,\mathcal L(8rH))$$ such that, for $\eta=u_1$ and for $\eta=u_b$, $$\theta\,\mathcal S(\eta-8rH)\subseteq\mathcal S(\eta).$$ Here $\mathcal S(\eta)$ is the space of global sections whose restriction to $U_Z$ is the reading of an algebraic cusp form supported on $Z$. Moreover, for every $y\in Y_Z\setminus U_Z$, every faithful integer-valued valuation $v$ centered at $y$, every compatible degeneration invariant $\phi\in\mathbb R$, every local trivialization of $\mathcal L(8rH)$ containing $y$, and every $h\in\mathbb Z$ with $v(\theta_y)=h$, one has $$h\ge\frac{8\phi}{625}.$$ The valuation assertion applies when the local coefficient has finite value.
