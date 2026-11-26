---
{
  "module": "src/Formalism/LocalToGlobal/TorsionIntegrality/WeierstrassTwoTorsion/BridgeTwoMore.lean",
  "declarations": [
    "Formalism.L2.Th1.A.bridgeTwoMore"
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

## An even expansion at a Weierstrass two-torsion point

[Theorem PHT.0991](https://andrewodesky.com/rh/lean/Formalism.L2.Th1.A.bridgeTwoMore/)

Let $K$ be an ultrametric normed field of characteristic zero and let $$W:\ y^2+a_1xy+a_3y=x^3+a_2x^2+a_4x+a_6$$ be a Weierstrass equation over $K$. Suppose $(x_0,y_0)$ satisfies $W$ and $2y_0+a_1x_0+a_3=0$. Put $$b_2=a_1^2+4a_2,\quad b_4=a_1a_3+2a_4,\quad b_6=a_3^2+4a_6,$$ $$c_4=b_2^2-24b_4,\quad c_6=-b_2^3+36b_2b_4-216b_6,\quad g_2=c_4/12,\quad g_3=c_6/216,\quad z_0=x_0+b_2/12.$$ Then $$4z_0^3-g_2z_0-g_3=0.$$ In the formal parameter $T=-x/y$ at infinity, let $e(Z)$ be the inverse of the formal integral, with zero constant term, of the invariant differential $dx/(2y+a_1x+a_3)$. Every odd coefficient of $$\frac{1}{x(e(Z))-x_0}\in K[[Z]]$$ vanishes. If $|a_1|,|a_2|,|a_3|,|a_4|,|a_6|\le1$ and $|x_0|\le1$, then $$|y_0|\le1,\qquad|b_2/12-z_0|\le1,\qquad|3z_0^2-g_2/4|\le1.$$
