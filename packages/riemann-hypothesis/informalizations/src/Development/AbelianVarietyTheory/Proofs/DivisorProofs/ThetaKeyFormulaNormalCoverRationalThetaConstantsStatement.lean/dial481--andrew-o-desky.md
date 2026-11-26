---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ThetaKeyFormulaNormalCoverRationalThetaConstantsStatement.lean",
  "declarations": [
    "GlobalTheory.T.thetaKeyFormula_normalCover_rational_thetaConstants"
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

## A Hodge-bundle identity for symmetric theta coordinates on a normal model

[Theorem AV.0824](https://andrewodesky.com/rh/lean/GlobalTheory.T.thetaKeyFormula_normalCover_rational_thetaConstants/)

Fix the source's full CM moduli datum with CM field $E$, signature parameters $p,q$, coefficient field $K$, generic moduli fibre $X_K$, and universal polarized abelian scheme of dimension $g=[E:\mathbb Q](p+q)/2$. Let $o$ be a commutative ring, $m\ge3$ odd and invertible in $o$, and put $N=m^{4g}$, $n=N-1$.

Let $f:X_K\to\mathbb P_o^n$ satisfy the symmetric theta-coordinate condition below. Let $Y$ be an integral model in the source's moduli system with generic-fibre inclusion $j:X_K\to Y$, and let $a:Y\to\mathbb P_o^n$ extend $f$. Let $\Omega/K$ be a field extension of characteristic zero, $(Z,\xi)$ a normal rational model of $\Omega$ over $K$, $\pi:Z\to Y$, and $y:\operatorname{Spec}\Omega\to X_K$, with $$\pi\circ\xi=j\circ y.$$ Assume there is a complete tuple $(d_1,\ldots,d_N)\in\Omega^N$ of theta constants for the universal polarized fibre at $y$, in the sense below. If $\lambda_Y=\det\operatorname{Lie}(G/Y)^\vee$ is the Hodge line of the model's universal semiabelian scheme, then $$\pi^*\bigl(a^*\mathcal O_{\mathbb P_o^n}(1)\bigr)^{\otimes8} \simeq\pi^*\lambda_Y^{\otimes 4N!}.$$
