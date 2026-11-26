---
{
  "module": "src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/UnimodularLocalStandard/UnitVecRam.lean",
  "declarations": [
    "PI.UnitaryGroupMassFormula.UnimodLocStd.unitVecRam"
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

## A vector whose normalized norm is a unit at the ramified prime

[Theorem ALG.1755](https://andrewodesky.com/rh/lean/PI.UnitaryGroupMassFormula.UnimodLocStd.unitVecRam/)

Let $a,b,c,d,\lambda,L,H,\Lambda$ satisfy the conditions in ([Self-dual lattices from an imaginary quadratic period pair](https://andrewodesky.com/rh/lean/PI.ULS.CmOK/)), with finite coordinate set $M$. Put $\kappa=|\lambda|^2a/\operatorname{area}(L)$. Write $$\Lambda_{(d)}=\{z:\exists n\in\mathbb N,\ d\nmid n,\ nz\in\Lambda\}.$$

Choose $x_0,y_0\in\mathbb Z$, $T\subseteq M$, and $j_0\in M\setminus T$ such that $$d\nmid ax_0^2+bx_0y_0+cy_0^2,$$ and $\lambda(ax_0+y_0\theta)e_j\in\Lambda_{(d)}$ for every $j\in T$, where $e_j$ is the coordinate vector. Let $x\in\Lambda_{(d)}$ vanish on $T$ and suppose either $x=0$ or $$H(x,x)=\kappa\frac{p}{q}\quad\text{for some }p,q\in\mathbb Z\text{ with }d\nmid p,\ d\nmid q.$$ If a nonzero $z_0\in\Lambda_{(d)}$ vanishes on $T$ and satisfies $H(z_0,x)=0$, then there is $y\in\Lambda_{(d)}$, vanishing on $T$ and satisfying $H(y,x)=0$, for which $$H(y,y)=\kappa\frac{p'}{q'}\quad\text{with }p',q'\in\mathbb Z,\ d\nmid p',\ d\nmid q'.$$
