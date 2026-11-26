---
{
  "module": "src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/RefExpPadicValLeShiftOfWeightFree.lean",
  "declarations": [
    "GlobalTheory.RefSum.WFree.refExp_padicVal_le_shift_of_weightFree"
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

## Reference exponents under parallel and scalar weight shifts

[Theorem ARAK.0125](https://andrewodesky.com/rh/lean/GlobalTheory.RefSum.WFree.refExp_padicVal_le_shift_of_weightFree/)

The local reference exponent at an unshifted weight is bounded by the reference exponent at a parallel-and-scalar shifted weight, with a cost supported on an explicit finite set of primes: $$R_\ell(c,W(u,0))\le R_\ell(c,W(u+w,s))+\begin{cases} sfr\,\dfrac{v_\ell(|\operatorname{disc}E|)}{[E:\mathbb Q]}+1,&\ell\in B,\\ 0,&\ell\notin B. \end{cases}$$

Assume ([Global hypotheses for Hodge-bundle estimates](https://andrewodesky.com/rh/s/k2-hodge-bundle-hypotheses.html)). Fix the arithmetic theta datum, a sequence of unitary moduli varieties satisfying the comparison hypothesis, a stage $1\le j\le m$, and a good cover with arbitrary parameters $e\in\mathbb N$, $o\in\mathbb R$, all as specified in ([Constant-norm removal of parallel and scalar weights](https://andrewodesky.com/rh/lean/GlobalTheory.ThinTwist.exists_constant_twist_of_thin_divisor/)). Require both stage signature entries $p,q$ to be at least $1$, and assume common-degree flat sections exist on the cover in the sense of ([Constant-norm removal of parallel and scalar weights](https://andrewodesky.com/rh/lean/GlobalTheory.ThinTwist.exists_constant_twist_of_thin_divisor/)). Then the displayed inequality holds for every integer weight $u$, every parallel shift $w:\Psi\to\mathbb Z$, every $s\in\mathbb N$, every $c\in\mathbb R$ and every rational prime $\ell$.

Here $f$ and $r$ are the rank parameters of the fixed theta datum, $W$ is defined in ([Constant-norm removal of parallel and scalar weights](https://andrewodesky.com/rh/lean/GlobalTheory.ThinTwist.exists_constant_twist_of_thin_divisor/)), and $$B=\{\ell:\ell\text{ is prime and }\ell\mid2d\,|\operatorname{disc}E|\,\operatorname{lcm}(M_{\mathrm{lev}},A_{\mathrm{lev}})\}.$$ The two integers in this least common multiple are those of the refined level; for a good cover $A_{\mathrm{lev}}=1$.
